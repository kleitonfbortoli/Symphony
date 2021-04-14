from pydantic import BaseModel
from database.symphony_db import Symphony_Db, Nota
from service.database.database_service import DataBaseService
class NotaService:
    entity = Nota

    @staticmethod
    @Symphony_Db.atomic()
    def storeNota(data: BaseModel):
        DataBaseService.store(NotaService.entity, data)
        return data