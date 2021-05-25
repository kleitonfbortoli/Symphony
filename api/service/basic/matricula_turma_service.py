import json
from pydantic import BaseModel
from database.symphony_db import Symphony_Db, Matricula_Turma
from service.database.database_service import DataBaseService

class MatriculaTurmaService:
    entity = Matricula_Turma
    
    @staticmethod
    @Symphony_Db.atomic()
    def store(data: BaseModel):
        DataBaseService.store(MatriculaTurmaService.entity, data)
        return json.dumps(data.__dict__)