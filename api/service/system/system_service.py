import datetime
import json
from peewee import Model
from fastapi import Request
from service.login.session_service import SessionService
from database.symphony_db import Session, Symphony_Db, Log_Api, Log_Error
from constants.request_model import BaseRequestModel
from exceptions.SymphonyException import LoginException
from playhouse.shortcuts import model_to_dict
from constants.status_model import return_constants as return_constants

class SystemService:
    url = ""
    api_name = ""
    request = ''
    response = ''
    session = None
    start_time = ''
    end_time = ''
    success = True
    token_access = ''
    log_api = Log_Api
    
    def __init__(self, data: BaseRequestModel, request: Request):
        self.url = str(request.url)
        self.api_name = self.url.replace(str(request.base_url), '')
        self.request = json.dumps(data.__dict__)
        self.start_time = str(datetime.datetime.now())
        self.token_access = data.token_access
        
    def validate_user(self):
        try:
            # Verifica se a pessoa está logada e se a sessão é valida
            session = SessionService.isLoged( token=self.token_access )
            self.session = session
        except Exception as e:
            raise LoginException("Usuário não econtrado");
    
    @Symphony_Db.atomic()
    def storeAudit(self):
        log = Log_Api(
            api_name=self.api_name,
            success=self.success,
            input_data=self.request,
            output_data=self.response,
            start_time=self.start_time,
            end_time = self.end_time
        )
        
        if not self.session is None:
            log.ref_session = self.session
            
        log.save()
        self.log_api = log
    
    @Symphony_Db.atomic()
    def storeErrorLog(self, error: Exception):
        print(error)
        log = Log_Error(
            ref_log_api = self.log_api,
            time_error = str(datetime.datetime.now()),
            error_message = str(error)
        )

        if not self.session is None:
            log.ref_session = self.session

        log.save()

    
    def make_return_data(self, status, response):
        self.response = response
        self.end_time = str(datetime.datetime.now())
        
        self.storeAudit();
        
        return {"status":status, "response":response}

    def make_error_return(self, e: Exception):
        self.success = False
        self.response = str(e)
        self.end_time = str(datetime.datetime.now())
        
        self.storeAudit();
        self.storeErrorLog(e)
        return {"status": return_constants.STATUS_INTERNAL_ERROR, 'message' : str(e) }