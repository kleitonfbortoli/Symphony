import json
from pydantic import BaseModel
from database.symphony_db import Symphony_Db, Horario
from service.database.database_service import DataBaseService
class HorarioService:
    entity = Horario

    @staticmethod
    @Symphony_Db.atomic()
    def storeHorario(data: BaseModel):
        DataBaseService.store(HorarioService.entity, data)
        return json.dumps(data.__dict__)