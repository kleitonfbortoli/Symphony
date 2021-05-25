import json
from pydantic import BaseModel
from database.symphony_db import Symphony_Db, Log_Api
from service.database.database_service import DataBaseService
from constants.request_model import RequestPostAuditoriaList

class AuditoriaService:
    entity = Log_Api
    
    @staticmethod
    @Symphony_Db.atomic()
    def getAuditoria(id: int):
        auditoria = Log_Api.get(Log_Api.id == id)
        return {
            'ref_session': str(auditoria.ref_session),
            'api_name': str(auditoria.api_name),
            'success': (auditoria.success and 'Sim' or 'Não'),
            'input_data': str(auditoria.input_data),
            'output_data': str(auditoria.output_data),
            'start_time': str(auditoria.start_time),
            'end_time': str(auditoria.end_time)
        }
    
    @staticmethod
    @Symphony_Db.atomic()
    def getAuditoriaList(data: RequestPostAuditoriaList):
        select = Log_Api.select()

        if data.api_name != '' and data.api_name != None:
            select = select.where(Log_Api.api_name ** ( "%"+str(data.api_name)+"%") )

        count_results = select.count()
        
        select = select.paginate(data.page_number, data.page_size)
        
        
        return_data = []
        
        for log in select.execute():
            return_data.append(
                {
                    'data': [
                        log.api_name,
                        (log.success and 'Sim' or 'Não'),
                        str(log.start_time),
                        str(log.end_time)
                    ],
                    'key': log.id
                }
            )

        response = {
            'count_results': count_results,
            'header': ['Api', 'Sucesso', 'Tempo de início', 'Tempo de fim'],
            'body': return_data
        }
        return response