import json
from pydantic import BaseModel
from database.symphony_db import Symphony_Db, Modulo
from service.database.database_service import DataBaseService
from constants.request_model import *

class ModuloService:
    entity = Modulo
   
    @staticmethod
    @Symphony_Db.atomic()
    def storeModulo(data: BaseModel):
        DataBaseService.store(ModuloService.entity, data)
        return json.dumps(data.__dict__)