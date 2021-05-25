import json
from pydantic import BaseModel
from database.symphony_db import Symphony_Db, Log_Error
from service.database.database_service import DataBaseService
from constants.request_model import RequestPostErrorList

class ErrorService:
    entity = Log_Error

    @staticmethod
    @Symphony_Db.atomic()
    def getError(id: int):
        error = Log_Error.get(Log_Error.id == id)
        
        return {
            'id': str(error.id),
            'time_error': str(error.time_error),
            'error_message': str(error.error_message),
            'ref_log_api': str(error.ref_log_api)
        }
    
    @staticmethod
    @Symphony_Db.atomic()
    def getErrorByAuditoria(id_auditoria: int):
        print()
        try:
            error = Log_Error.get(Log_Error.ref_log_api == id_auditoria)
            return {
                'id': str(error.id),
                'time_error': str(error.time_error),
                'error_message': str(error.error_message)
            }
        except:
            return {
                'id': str(),
                'time_error': str(),
                'error_message': str()
            }
    
        
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
                {
                    'data': [erro.error_message, str(erro.time_error)],
                    'key': erro.id
                }
            )

        response = {
            'count_results': count_results,
            'header': ['Mensagem','Horário'],
            'body': return_data
        }
        return response