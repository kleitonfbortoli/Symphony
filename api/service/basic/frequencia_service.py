import json
from pydantic import BaseModel
from database.symphony_db import Symphony_Db, Frequencia
from service.database.database_service import DataBaseService

class FrequenciaService:
    entity = Frequencia

    @staticmethod
    @Symphony_Db.atomic()
    def get(id: int):
        entity = Frequencia.get(Frequencia.id == id)
        return entity.__data__

    @staticmethod
    @Symphony_Db.atomic()
    def store(data: BaseModel):
        DataBaseService.store(FrequenciaService.entity, data)
        return json.dumps(data.__dict__)