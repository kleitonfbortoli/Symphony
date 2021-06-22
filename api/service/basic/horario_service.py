import json
from pydantic import BaseModel
from database.symphony_db import Symphony_Db, Horario
from service.database.database_service import DataBaseService
from constants.request_model import RequestPostHorarioList
class HorarioService:
    entity = Horario

    @staticmethod
    @Symphony_Db.atomic()
    def get(id: int):
        entity = Horario.get(Horario.id == id)
        return entity.__data__
    
    @staticmethod
    @Symphony_Db.atomic()
    def storeHorario(data: BaseModel):
        DataBaseService.store(HorarioService.entity, data)
        return json.dumps(data.__dict__)
    
    @staticmethod
    @Symphony_Db.atomic()
    def get(id: int):
        horario = Horario.get(Horario.id == id)
        return {
            'id':horario.id,
            'descricao':horario.descricao,
            'dia_semana':str(horario.dia_semana),
            'turno':horario.turno,
            'hora_ini':horario.hora_ini,
            'hora_fim':horario.hora_fim
        }
    
    @staticmethod
    @Symphony_Db.atomic()
    def list(data: RequestPostHorarioList):
        select = Horario.select()

        if data.descricao != '' and data.descricao != None:
            select = select.where(Horario.descricao ** ( "%"+str(data.descricao)+"%") )
        
        if data.dia_semana != '' and data.dia_semana != None:
            select = select.where(Horario.dia_semana ** ( "%"+str(data.dia_semana)+"%") )
            
        if data.turno != '' and data.turno != None:
            select = select.where(Horario.turno ** ( "%"+str(data.turno)+"%") )
        
        count_results = select.count()
        
        select = select.paginate(data.page_number, data.page_size)
        
        return_data = []
        
        for result in select.execute():
            return_data.append(
                {
                    'data': [result.descricao, result.dia_semana, result.turno, result.hora_ini, result.hora_fim],
                    'key': result.id
                    
                }
            )

        response = {
            'count_results': count_results,
            'header': ['Descrição', 'Dia da Semana', 'Turno', 'Hora  início', 'Hora fim'],
            'body': return_data
        }
        return response