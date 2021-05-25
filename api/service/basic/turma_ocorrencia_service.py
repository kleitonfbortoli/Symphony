
import json
from pydantic import BaseModel
from database.symphony_db import Symphony_Db, Turma_Ocorencia
from service.database.database_service import DataBaseService

class TurmaOcorenciaService:
    entity = Turma_Ocorencia
    
    @staticmethod
    @Symphony_Db.atomic()
    def store(data: BaseModel):
        DataBaseService.store(TurmaOcorenciaService.entity, data)
        return json.dumps(data.__dict__)