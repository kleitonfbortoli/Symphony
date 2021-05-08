import json
from pydantic import BaseModel
from database.symphony_db import Symphony_Db, Serie
from service.database.database_service import DataBaseService
class SerieService:
    entity = Serie
    
    @staticmethod
    @Symphony_Db.atomic()
    def storeSerie(data: BaseModel):
        DataBaseService.store(SerieService.entity, data)
        return json.dumps(data.__dict__)