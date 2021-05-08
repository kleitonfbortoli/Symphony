import json
from pydantic import BaseModel
from database.symphony_db import Symphony_Db, Log_Error
from service.database.database_service import DataBaseService
from constants.request_model import *

class ErrorService:
    entity = Log_Error

    @staticmethod
    @Symphony_Db.atomic()
    def getErrorList(data: RequestPostErrorList):
        select = Log_Error.select()

        if data.error_message != '' and data.error_message != None:
            select = select.where(Log_Error.error_message ** ( "%"+str(data.error_message)+"%") )
        
        count_results = select.count()
        
        select = select.paginate(data.page_number, data.page_size)
        
        return_data = []
        
        for erro in select.execute():
            return_data.append(
                [ erro.error_message, str(erro.time_error)]
            )

        response = {
            'count_results': count_results,
            'header': ['Mensagem','Horário'],
            'body': return_data
        }
        return response