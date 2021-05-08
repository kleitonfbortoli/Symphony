import json
from pydantic import BaseModel
from database.symphony_db import Symphony_Db, Periodo_Academico
from service.database.database_service import DataBaseService
class PeriodoService:
    entity = Periodo_Academico

    @staticmethod
    @Symphony_Db.atomic()
    def storePeriodo(data: BaseModel):
        DataBaseService.store(PeriodoService.entity, data)
        return json.dumps(data.__dict__)