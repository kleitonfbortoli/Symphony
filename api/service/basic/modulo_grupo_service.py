import json
from pydantic import BaseModel
from database.symphony_db import Symphony_Db, Modulo_Grupo
from service.database.database_service import DataBaseService

class ModuloGrupoService:
    entity = Modulo_Grupo
    
    @staticmethod
    @Symphony_Db.atomic()
    def store(data: BaseModel):
        DataBaseService.store(ModuloGrupoService.entity, data)
        return json.dumps(data.__dict__)