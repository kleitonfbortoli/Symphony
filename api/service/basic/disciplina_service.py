import json
from pydantic import BaseModel
from database.symphony_db import Symphony_Db, Disciplina
from service.database.database_service import DataBaseService
from constants.request_model import *

class DisciplinaService:
    entity = Disciplina
    
    @staticmethod
    @Symphony_Db.atomic()
    def store(data: BaseModel):
        DataBaseService.store(DisciplinaService.entity, data)
        return json.dumps(data.__dict__)
    
    @staticmethod
    @Symphony_Db.atomic()
    def getList(data: RequestPostDisciplinaList):
        select = Disciplina.select()

        # if data.error_message != '' and data.error_message != None:
        #     select = select.where(Disciplina.error_message ** ( "%"+str(data.error_message)+"%") )
        
        count_results = select.count()
        
        select = select.paginate(data.page_number, data.page_size)
        
        return_data = []
        
        for result in select.execute():
            return_data.append(
                [ result.nome, str(result.ch)]
            )

        response = {
            'count_results': count_results,
            'header': ['Nome','Carga Horária'],
            'body': return_data
        }
        return response