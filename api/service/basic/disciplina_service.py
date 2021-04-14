from pydantic import BaseModel
from database.symphony_db import Symphony_Db, Disciplina
from service.database.database_service import DataBaseService
class DisciplinaService:
    entity = Disciplina
    
    @staticmethod
    @Symphony_Db.atomic()
    def storeDisciplina(data: BaseModel):
        DataBaseService.store(DisciplinaService.entity, data)
        return data