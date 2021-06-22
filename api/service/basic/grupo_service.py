import json
from pydantic import BaseModel
from database.symphony_db import Symphony_Db, Grupo
from service.database.database_service import DataBaseService
from constants.request_model import RequestPostGrupoList

class GrupoService:
    entity = Grupo

    @staticmethod
    @Symphony_Db.atomic()
    def get(id: int):
        entity = Grupo.get(Grupo.id == id)
        return entity.__data__
   
    @staticmethod
    @Symphony_Db.atomic()
    def storeGrupo(data: BaseModel):
        DataBaseService.store(GrupoService.entity, data)
        return json.dumps(data.__dict__)
    
    @staticmethod
    @Symphony_Db.atomic()
    def get(id: int):
        grupo = Grupo.get(Grupo.id == id)
        return {
            'id':grupo.id,
            'descricao':grupo.descricao,
        }
    
    @staticmethod
    @Symphony_Db.atomic()
    def list(data: RequestPostGrupoList):
        select = Grupo.select()

        if data.descricao != '' and data.descricao != None:
            select = select.where(Grupo.descricao ** ( "%"+str(data.descricao)+"%") )
        
        count_results = select.count()
        
        select = select.paginate(data.page_number, data.page_size)
        
        return_data = []
        
        for result in select.execute():
            return_data.append(
                {
                    'data': [ result.descricao ],
                    'key': result.id
                }
            )

        response = {
            'count_results': count_results,
            'header': ['Descrição'],
            'body': return_data
        }
        return response