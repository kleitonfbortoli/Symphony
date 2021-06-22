import json
from pydantic import BaseModel
from database.symphony_db import Symphony_Db, Turma
from service.database.database_service import DataBaseService
from constants.request_model import *
from service.basic.serie_service import SerieService

class TurmaService:
    entity = Turma
    
    @staticmethod
    @Symphony_Db.atomic()
    def get(id: int):
        entity = Turma.get(Turma.id == id)
        return entity.__data__
    
    @staticmethod
    @Symphony_Db.atomic()
    def store(data: BaseModel):
        DataBaseService.store(TurmaService.entity, data)
        return json.dumps(data.__dict__)
    
    @staticmethod
    @Symphony_Db.atomic()
    def list(data: RequestPostTurmaList):
        select = Turma.select()

        if data.descricao != '' and data.descricao != None:
            select = select.where(Turma.descricao ** ( "%"+str(data.descricao)+"%") )
        
        count_results = select.count()
        select = select.paginate(data.page_number, data.page_size)
        
        return_data = []
        
        for result in select.execute():
            serie = SerieService.get(result.ref_serie)
            return_data.append(
                {
                    'data': [ result.descricao, serie['nome']],
                    'key': result.id
                    
                }
            )

        response = {
            'count_results': count_results,
            'header': ['Descrição','Série'],
            'body': return_data
        }
        print(response)
        return response