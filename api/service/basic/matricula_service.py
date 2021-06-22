import json
from pydantic import BaseModel
from database.symphony_db import Symphony_Db, Matricula, Pessoa
from constants.request_model import *
from service.basic.pessoa_service import PessoaService
from peewee import fn

class MatriculaService:
    entity = Matricula

    @staticmethod
    @Symphony_Db.atomic()
    def get(id: int):
        entity = Matricula.get(Matricula.id == id)
        return entity.__data__
    
    @staticmethod
    @Symphony_Db.atomic()
    def store(data: BaseModel):
        obj = {
            'ref_turma': data.key,
            'ref_pessoa': data.relation
        }
        
        MatriculaService.entity.create(**obj)
        
        return json.dumps(data.__dict__)
    
    @staticmethod
    @Symphony_Db.atomic()
    def delete(data: BaseModel):
        
        MatriculaService.entity.delete().where(MatriculaService.entity.id == data.key).execute()

        return json.dumps(data.__dict__)
    
    @staticmethod
    @Symphony_Db.atomic()
    def ListPessoaByTurma(data: RequestPostPessoaListByTurma):
        select = Matricula.select()

        select = select.where(Matricula.ref_turma == data.key)
        
        count_results = select.count()

        return_data = []
        
        for result in select.execute():
            pesssa = PessoaService.get(result.ref_pessoa)
            return_data.append(
                {
                    'data': [ pesssa['nome'], pesssa['email']],
                    'key': result.id
                }
            )

        response = {
            'count_results': count_results,
            'header': ['Nome', 'E-Mail'],
            'body': return_data
        }
        return response
    
    @staticmethod
    @Symphony_Db.atomic()
    def listPessoaLiveByTurma(data: RequestPostPessoaListByTurma):
        sub_select = Matricula.select()

        sub_select = sub_select.where(Matricula.ref_turma == data.key)
        sub_select = sub_select.where(Matricula.ref_pessoa == Pessoa.id)
        
        select = Pessoa.select()
        select = select.where(~fn.EXISTS(sub_select))

        return_data = []
        
        for result in select.execute():
            return_data.append(
                {
                    'label': result.nome,
                    'value': result.id
                }
            )
        return return_data