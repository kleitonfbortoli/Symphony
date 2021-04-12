import datetime
import json
from peewee import Model
from fastapi import Request
from service.login.session_service import SessionService
from database.symphony_db import Session, Symphony_Db, Log_Api
from constants.request_model import BaseRequestModel
from exceptions.SymphonyException import LoginException
from playhouse.shortcuts import model_to_dict

class SystemService:
    url = ""
    api_name = ""
    request = ''
    response = ''
    session = Session
    start_time = ''
    end_time = ''
    success = True
    
    def __init__(self, data: BaseRequestModel, request: Request):
        self.url = str(request.url)
        self.api_name = self.url.replace(str(request.base_url), '')
        self.request = json.dumps(data.__dict__)
        self.start_time = str(datetime.datetime.now())
        
        try:
            # Verifica se a pessoa está logada e se a sessão é valida
            session = SessionService.isLoged( token=data.token )
            self.session = session
        except Exception as e:
            print(e)
            self.storePermissionErrorLog();
            raise LoginException("Usuário não econtrado");
    
    @Symphony_Db.atomic()
    def storeAudit(self):
        log = Log_Api()
        log.ref_session = self.session
        log.api_name = self.api_name
        log.success = self.success
        log.input_data = self.request
        log.output_data = self.response
        log.start_time = self.start_time
        log.end_time = self.end_time
        log.save()
    
    def storeErrorLog(self, error: Exception):
        pass
    
    def storePermissionErrorLog(self):
        pass
    
    def make_return_data(self, status, response):
        self.response = json.dumps(response.__dict__)
        self.end_time = str(datetime.datetime.now())
        self.storeAudit();
        return {"status":status, "response":response}

    def make_error_return(self, e: Exception):
        self.storeErrorLog(e)
        # return {"status":status}
        pass
    
    # def convertToJson(self, object):
    #     json = ''
    #     if(isinstance(object, SymphonyModel)):
    #         json = json.dumps(model_to_dict(object))
    #     elif(isinstance(object, BaseRequestModel)):
    #         json = object.json()
    #     else:
    #         json = json.dumps(object.__dict__)
            
    #     return json
            