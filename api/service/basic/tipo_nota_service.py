from pydantic import BaseModel
from database.symphony_db import Symphony_Db, Tipo_Nota
from service.database.database_service import DataBaseService
class TipoNotaService:
    entity = Tipo_Nota

    @staticmethod
    @Symphony_Db.atomic()
    def storeTipoNota(data: BaseModel):
        DataBaseService.store(TipoNotaService.entity, data)
        return data