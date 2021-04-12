from pydantic import BaseModel
<<<<<<< HEAD
from database.symphony_db import Symphony_Db, Pessoa
from service.database.database_service import DataBaseService

=======
from database.database import Symphony_Db, Pessoa
from service.database.database_service import DataBaseService
>>>>>>> 2754f82295d7d6c16b659e137b2a72cf9cbe0175
class PessoaService:
    entity = Pessoa
    
    @staticmethod
    @Symphony_Db.atomic()
    def storePessoa(data: BaseModel):
        DataBaseService.store(PessoaService.entity, data)
<<<<<<< HEAD
        return True    
    
    @staticmethod
    @Symphony_Db.atomic()
    def getByEmailAndSenha(email: str, password:str):
        user = Pessoa.select().where(Pessoa.email == email, Pessoa.password == password).first()
        return user
=======
        return True
>>>>>>> 2754f82295d7d6c16b659e137b2a72cf9cbe0175
