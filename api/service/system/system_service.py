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
    session = Session
    start_time = ''
    end_time = ''
    success = True
    token_access = ''
    log_api_id = int
    
    def __init__(self, data: BaseRequestModel, request: Request):
        self.url = str(request.url)
        self.api_name = self.url.replace(str(request.base_url), '')
        self.request = json.dumps(data.__dict__)
        self.start_time = str(datetime.datetime.now())
        self.token_access = data.token_access
        
    def validate_user(self):
        pass
        # try:
        #     # Verifica se a pessoa está logada e se a sessão é valida
        #     session = SessionService.isLoged( token=data.token_access )
        #     self.session = session
        # except Exception as e:
        #     raise LoginException("Usuário não econtrado");
    
    @Symphony_Db.atomic()
    def storeAudit(self):
        log = Log_Api()
        # log.ref_session = self.session
        log.api_name = self.api_name
        log.success = self.success
        log.input_data = self.request
        log.output_data = self.response
        log.start_time = self.start_time
        log.end_time = self.end_time
        log.save()
        self.log_api = log
    
    @Symphony_Db.atomic()
    def storeErrorLog(self, error: Exception):
        log = Log_Error()
        # log.ref_session = self.session
        log.ref_log_api = self.log_api
        log.time_error = str(datetime.datetime.now())
        log.error_message = str(error)
        a = log.save()
        print(log.id)

    
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
        
    def convertToJson(self, object):
        retorno = ''

        if isinstance(object, BaseRequestModel):
            retorno = object.json()
        elif self.is_json(object):
            retorno = object
        else:
            retorno = json.dumps(object.__dict__)
            
        return retorno
    
    def is_json(self, x) :
        try:
            print(x)
            json.loads(x)
            return True
        except:
            return False

        return True