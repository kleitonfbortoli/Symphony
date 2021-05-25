import json
from pydantic import BaseModel
from database.symphony_db import Symphony_Db, Horario
from service.database.database_service import DataBaseService
from constants.request_model import RequestPostHorarioList
class HorarioService:
    entity = Horario

    @staticmethod
    @Symphony_Db.atomic()
    def storeHorario(data: BaseModel):
        DataBaseService.store(HorarioService.entity, data)
        return json.dumps(data.__dict__)
    
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
                [ result.descricao, result.dia_semana, result.turno, result.hora_ini, result.hora_fim]
            )

        response = {
            'count_results': count_results,
            'header': ['Descrição', 'Dia da Semana', 'Turno', 'Hora  início', 'Hora fim'],
            'body': return_data
        }
        return response