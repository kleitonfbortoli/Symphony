import json
from pydantic import BaseModel
from database.symphony_db import Symphony_Db, Matricula_Serie
from service.database.database_service import DataBaseService

class MatriculaSerieService:
    entity = Matricula_Serie
    
    @staticmethod
    @Symphony_Db.atomic()
    def store(data: BaseModel):
        DataBaseService.store(MatriculaSerieService.entity, data)
        return json.dumps(data.__dict__)