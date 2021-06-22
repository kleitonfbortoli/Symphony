import json
from pydantic import BaseModel
from database.symphony_db import Symphony_Db, Matriz, Disciplina
from service.database.database_service import DataBaseService
from constants.request_model import *
from service.basic.disciplina_service import DisciplinaService
from peewee import fn

class MatrizService:
    entity = Matriz

    @staticmethod
    @Symphony_Db.atomic()
    def get(id: int):
        entity = Matriz.get(Matriz.id == id)
        return entity.__data__
    
    @staticmethod
    @Symphony_Db.atomic()
    def store(data: BaseModel):
        obj = {
            'ref_serie': data.key,
            'ref_disciplina': data.relation
        }
        
        MatrizService.entity.create(**obj)
        
        return json.dumps(data.__dict__)
    
    @staticmethod
    @Symphony_Db.atomic()
    def delete(data: BaseModel):
        
        MatrizService.entity.delete().where(MatrizService.entity.id == data.key).execute()

        return json.dumps(data.__dict__)
    
    @staticmethod
    @Symphony_Db.atomic()
    def ListDiciplinaBySerie(data: RequestPostDisciplinaListBySerie):
        select = Matriz.select()

        select = select.where(Matriz.ref_serie == data.key)
        
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

        response = {
            'count_results': count_results,
            'header': ['Nome', 'Carga Horária'],
            'body': return_data
        }
        return response
    
    @staticmethod
    @Symphony_Db.atomic()
    def listDisciplinaLiveBySerie(data: RequestPostDisciplinaListBySerie):
        sub_select = Matriz.select()

        sub_select = sub_select.where(Matriz.ref_serie == data.key)
        sub_select = sub_select.where(Matriz.ref_disciplina == Disciplina.id)
        
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