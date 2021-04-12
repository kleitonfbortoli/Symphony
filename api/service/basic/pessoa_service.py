from pydantic import BaseModel
from database.symphony_db import Symphony_Db, Pessoa
from service.database.database_service import DataBaseService

class PessoaService:
    entity = Pessoa
    
    @staticmethod
    @Symphony_Db.atomic()
    def storePessoa(data: BaseModel):
        DataBaseService.store(PessoaService.entity, data)
        return True    
    
    @staticmethod
    @Symphony_Db.atomic()
    def getByEmailAndSenha(email: str, password:str):
        user = Pessoa.select().where(Pessoa.email == email, Pessoa.password == password).first()
        return user

