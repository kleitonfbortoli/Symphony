import json
from pydantic import BaseModel
from database.symphony_db import Symphony_Db, Pessoa
from service.database.database_service import DataBaseService

from constants.request_model import *

class PessoaService:
    entity = Pessoa

    @staticmethod
    @Symphony_Db.atomic()
    def getPessoa(id: int):
        pessoa = Pessoa.get(Pessoa.id == id)
        return {
            'nome':pessoa.nome,
            'dt_nascimento':str(pessoa.dt_nascimento),
            'email':pessoa.email
        }

    @staticmethod
    @Symphony_Db.atomic()
    def storePessoa(data: BaseModel):
        DataBaseService.store(PessoaService.entity, data)
        return json.dumps(data.__dict__)

    @staticmethod
    @Symphony_Db.atomic()
    def getByEmailAndSenha(email: str, password:str):
        user = Pessoa.select().where(Pessoa.email == email, Pessoa.password == password).first()
        return user

    @staticmethod
    @Symphony_Db.atomic()
    def getPessoasList(data: RequestPostPessoasList):
        select = Pessoa.select()

        if data.nome != '' and data.nome != None:
            select = select.where(Pessoa.nome ** ( "%"+str(data.nome)+"%") )
    
        if data.email != '' and data.email != None:
            select = select.where(Pessoa.email ** ( "%"+str(data.email)+"%") )

        count_results = select.count()
        
        select = select.paginate(data.page_number, data.page_size)
        
        return_data = []
        
        for pessoa in select.execute():
            return_data.append(
                {
                    'data': [ pessoa.nome, pessoa.email],
                    'key': pessoa.id
                }
            )

        response = {
            'count_results': count_results,
            'header': ['Nome','E-mail'],
            'body': return_data
        }

        return response