import json
from pydantic import BaseModel
from database.symphony_db import Symphony_Db, Log_Api
from service.database.database_service import DataBaseService
from constants.request_model import *

class AuditoriaService:
    entity = Log_Api
    
    @staticmethod
    @Symphony_Db.atomic()
    def getAuditoriaList(data: RequestPostAuditoriaList):
        select = Log_Api.select()

        if data.api_name != '' and data.api_name != None:
            select = select.where(Log_Api.api_name ** ( "%"+str(data.api_name)+"%") )

        count_results = select.count()
        
        select = select.paginate(data.page_number, data.page_size)
        
        print(select)
        
        return_data = []
        
        for log in select.execute():
            return_data.append(
                [
                    log.api_name,
                    (log.success and 'Sim' or 'Não'),
                    str(log.start_time),
                    str(log.end_time)
                ]
            )

        response = {
            'count_results': count_results,
            'header': ['Api', 'Sucesso', 'Tempo de início', 'Tempo de fim'],
            'body': return_data
        }
        print(response)
        return response