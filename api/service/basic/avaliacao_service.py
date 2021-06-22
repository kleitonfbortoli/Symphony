import json
from pydantic import BaseModel
from database.symphony_db import Symphony_Db, Avaliacao
from service.database.database_service import DataBaseService

class AvaliacaoService:
    entity = Avaliacao
    
    @staticmethod
    @Symphony_Db.atomic()
    def get(id: int):
        entity = Avaliacao.get(Avaliacao.id == id)
        return entity.__data__
    
    @staticmethod
    @Symphony_Db.atomic()
    def store(data: BaseModel):
        DataBaseService.store(AvaliacaoService.entity, data)
        return json.dumps(data.__dict__)