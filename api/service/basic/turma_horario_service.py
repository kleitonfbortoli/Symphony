
import json
from pydantic import BaseModel
from database.symphony_db import Symphony_Db, Turma_Horario, Horario
from constants.request_model import *
from service.basic.horario_service import HorarioService
from peewee import fn

class TurmaHorarioService:
    entity = Turma_Horario

    @staticmethod
    @Symphony_Db.atomic()
    def get(id: int):
        entity = Turma_Horario.get(Turma_Horario.id == id)
        return entity.__data__
    
    @staticmethod
    @Symphony_Db.atomic()
    def store(data: BaseModel):
        obj = {
            'ref_turma_ocorrencia': data.key,
            'ref_horario': data.relation
        }
        
        TurmaHorarioService.entity.create(**obj)
        
        return json.dumps(data.__dict__)
    
    @staticmethod
    @Symphony_Db.atomic()
    def delete(data: BaseModel):
        
        TurmaHorarioService.entity.delete().where(TurmaHorarioService.entity.id == data.key).execute()

        return json.dumps(data.__dict__)
    
    @staticmethod
    @Symphony_Db.atomic()
    def ListHorarioByTurmaOcorrencia(data: RequestPostHorarioListByTurmaOcorrencia):
        select = Turma_Horario.select()

        select = select.where(Turma_Horario.ref_turma_ocorrencia == data.key)
        
        count_results = select.count()

        return_data = []
        
        for result in select.execute():
            horario = HorarioService.get(result.ref_horario)
            return_data.append(
                {
                    'data': [ horario['descricao'], horario['dia_semana'], horario['turno'], horario['hora_ini'], horario['hora_fim']],
                    'key': result.id
                }
            )

        response = {
            'count_results': count_results,
            'header': ['Nome', 'Dia da Semana', 'Turno', 'Hora Início', 'Hora Fim'],
            'body': return_data
        }
        return response
    
    @staticmethod
    @Symphony_Db.atomic()
    def listHorarioLivreByTurmaOcorrencia(data: RequestPostHorarioListByTurmaOcorrencia):
        sub_select = Turma_Horario.select()

        sub_select = sub_select.where(Turma_Horario.ref_turma_ocorrencia == data.key)
        sub_select = sub_select.where(Turma_Horario.ref_horario == Horario.id)
        select = Horario.select()
        select = select.where(~fn.EXISTS(sub_select))

        return_data = []
        
        for result in select.execute():
            return_data.append(
                {
                    'label': result.descricao + " - " + result.dia_semana + " (" +  result.turno + "; " + result.hora_ini + " - "+ result.hora_fim + ")",
                    'value': result.id
                }
            )

        return return_data