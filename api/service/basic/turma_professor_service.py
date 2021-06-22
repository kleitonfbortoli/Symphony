import json
from pydantic import BaseModel
from database.symphony_db import Symphony_Db, Turma_Professor, Pessoa
from service.database.database_service import DataBaseService
from constants.request_model import *
from service.basic.pessoa_service import PessoaService
from peewee import fn

class TurmaProfessorService:
    entity = Turma_Professor
    
    @staticmethod
    @Symphony_Db.atomic()
    def get(id: int):
        entity = Turma_Professor.get(Turma_Professor.id == id)
        return entity.__data__

    @staticmethod
    @Symphony_Db.atomic()
    def store(data: BaseModel):
        obj = {
            'ref_turma_ocorrencia': data.key,
            'ref_pessoa': data.relation
        }
        
        TurmaProfessorService.entity.create(**obj)
        
        return json.dumps(data.__dict__)
    
    @staticmethod
    @Symphony_Db.atomic()
    def delete(data: BaseModel):
        
        TurmaProfessorService.entity.delete().where(TurmaProfessorService.entity.id == data.key).execute()

        return json.dumps(data.__dict__)
    
    @staticmethod
    @Symphony_Db.atomic()
    def ListProfessorByTurmaOcorrencia(data: RequestPostProfessorListByTurmaOcorrencia):
        select = Turma_Professor.select()

        select = select.where(Turma_Professor.ref_turma_ocorrencia == data.key)
        
        count_results = select.count()

        return_data = []
        
        for result in select.execute():
            pessoa = PessoaService.get(result.ref_pessoa)
            return_data.append(
                {
                    'data': [ pessoa['nome'], pessoa['email']],
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
    def listProfessorLivreByTurmaOcorrencia(data: RequestPostProfessorListByTurmaOcorrencia):
        sub_select = Turma_Professor.select()

        sub_select = sub_select.where(Turma_Professor.ref_turma_ocorrencia == data.key)
        sub_select = sub_select.where(Turma_Professor.ref_pessoa == Pessoa.id)
        
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