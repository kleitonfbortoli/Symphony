import json
from pydantic import BaseModel
from database.symphony_db import Symphony_Db, Turma_Professor
from service.database.database_service import DataBaseService

class TurmaProfessorService:
    entity = Turma_Professor
    
    @staticmethod
    @Symphony_Db.atomic()
    def store(data: BaseModel):
        DataBaseService.store(TurmaProfessorService.entity, data)
        return json.dumps(data.__dict__)