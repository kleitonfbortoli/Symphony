from pydantic import BaseModel
from database.database import Symphony_Db, Pessoa
from service.database.database_service import DataBaseService
class PessoaService:
    entity = Pessoa
    
    @staticmethod
    @Symphony_Db.atomic()
    def storePessoa(data: BaseModel):
        DataBaseService.store(PessoaService.entity, data)
        return True