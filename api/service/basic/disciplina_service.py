import json
from pydantic import BaseModel
from database.symphony_db import Symphony_Db, Disciplina
from service.database.database_service import DataBaseService
from constants.request_model import RequestPostDisciplinaList

class DisciplinaService:
    entity = Disciplina

    @staticmethod
    @Symphony_Db.atomic()
    def get(id: int):
        entity = Disciplina.get(Disciplina.id == id)
        return entity.__data__
    
    @staticmethod
    @Symphony_Db.atomic()
    def store(data: BaseModel):
        DataBaseService.store(DisciplinaService.entity, data)
        return json.dumps(data.__dict__)

    @staticmethod
    @Symphony_Db.atomic()
    def get(id: int):
        disciplina = Disciplina.get(Disciplina.id == id)
        return {
            'id':disciplina.id,
            'nome':disciplina.nome,
            'ch':disciplina.ch,
        }
    
    @staticmethod
    @Symphony_Db.atomic()
    def list(data: RequestPostDisciplinaList):
        select = Disciplina.select()

        if data.nome != '' and data.nome != None:
            select = select.where(Disciplina.nome ** ( "%"+str(data.nome)+"%") )
        
        count_results = select.count()
        
        select = select.paginate(data.page_number, data.page_size)
        
        return_data = []
        
        for result in select.execute():
            return_data.append(
                {
                    'data': [ result.nome, str(result.ch)],
                    'key': result.id
                    
                }
            )

        response = {
            'count_results': count_results,
            'header': ['Nome','Carga Horária'],
            'body': return_data
        }
        return response