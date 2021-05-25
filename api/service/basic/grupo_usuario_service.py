import json
from pydantic import BaseModel
from database.symphony_db import Symphony_Db, Grupo_Usuario
from service.database.database_service import DataBaseService

class GrupoUsuarioService:
    entity = Grupo_Usuario
    
    @staticmethod
    @Symphony_Db.atomic()
    def store(data: BaseModel):
        DataBaseService.store(GrupoUsuarioService.entity, data)
        return json.dumps(data.__dict__)