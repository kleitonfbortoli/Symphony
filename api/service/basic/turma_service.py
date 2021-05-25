import json
from pydantic import BaseModel
from database.symphony_db import Symphony_Db, Turma
from service.database.database_service import DataBaseService

class TurmaService:
    entity = Turma
    
    @staticmethod
    @Symphony_Db.atomic()
    def store(data: BaseModel):
        DataBaseService.store(TurmaService.entity, data)
        return json.dumps(data.__dict__)