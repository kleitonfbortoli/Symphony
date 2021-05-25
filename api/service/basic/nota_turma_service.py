import json
from pydantic import BaseModel
from database.symphony_db import Symphony_Db, Nota_Turma
from service.database.database_service import DataBaseService

class NotaTurmaService:
    entity = Nota_Turma
    
    @staticmethod
    @Symphony_Db.atomic()
    def store(data: BaseModel):
        DataBaseService.store(NotaTurmaService.entity, data)
        return json.dumps(data.__dict__)