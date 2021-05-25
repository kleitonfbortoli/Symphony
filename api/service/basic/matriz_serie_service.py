import json
from pydantic import BaseModel
from database.symphony_db import Symphony_Db, Matriz_Serie
from service.database.database_service import DataBaseService

class MatrizSerieService:
    entity = Matriz_Serie
    
    @staticmethod
    @Symphony_Db.atomic()
    def store(data: BaseModel):
        DataBaseService.store(MatrizSerieService.entity, data)
        return json.dumps(data.__dict__)