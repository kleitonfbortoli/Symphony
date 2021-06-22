
import json
from pydantic import BaseModel
from database.symphony_db import Symphony_Db, Turma_Ocorencia, Disciplina
from constants.request_model import *
from service.basic.disciplina_service import DisciplinaService
from peewee import fn

class TurmaOcorrenciaService:
    entity = Turma_Ocorencia
    
    @staticmethod
    @Symphony_Db.atomic()
    def get(id: int):
        entity = Turma_Ocorencia.get(Turma_Ocorencia.id == id)
        return entity.__data__

    @staticmethod
    @Symphony_Db.atomic()
    def store(data: BaseModel):
        obj = {
            'ref_turma': data.key,
            'ref_disciplina': data.relation
        }
        
        TurmaOcorrenciaService.entity.create(**obj)
        
        return json.dumps(data.__dict__)
    
    @staticmethod
    @Symphony_Db.atomic()
    def delete(data: BaseModel):

        TurmaOcorrenciaService.entity.delete().where(TurmaOcorrenciaService.entity.id == data.key).execute()

        return json.dumps(data.__dict__)
    
    @staticmethod
    @Symphony_Db.atomic()
    def ListDisciplinaByTurma(data: RequestPostDisciplinaListByTurma):
        select = Turma_Ocorencia.select()

        select = select.where(Turma_Ocorencia.ref_turma == data.key)
        
        count_results = select.count()

        return_data = []
        
        for result in select.execute():
            disciplina = DisciplinaService.get(result.ref_disciplina)
            return_data.append(
                {
                    'data': [ disciplina['nome'], disciplina['ch']],
                    'key': result.id
                }
            )

        print(return_data)
        response = {
            'count_results': count_results,
            'header': ['Nome', 'Carga Horária'],
            'body': return_data
        }
        return response
    
    @staticmethod
    @Symphony_Db.atomic()
    def listDisciplinaLivreByTurma(data: RequestPostDisciplinaListByTurma):
        sub_select = Turma_Ocorencia.select()

        sub_select = sub_select.where(Turma_Ocorencia.ref_turma == data.key)
        sub_select = sub_select.where(Turma_Ocorencia.ref_disciplina == Disciplina.id)
        
        select = Disciplina.select()
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