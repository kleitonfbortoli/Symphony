import bson
import json
from pydantic import BaseModel
from database.symphony_db import Symphony_Db, Periodo
from service.database.database_service import DataBaseService
from constants.request_model import *
class PeriodoService:
    entity = Periodo

    @staticmethod
    @Symphony_Db.atomic()
    def get(id: int):
        entity = Periodo.get(Periodo.id == id)

        return json.dumps(entity.__data__)

    @staticmethod
    @Symphony_Db.atomic()
    def storePeriodo(data: BaseModel):
        DataBaseService.store(PeriodoService.entity, data)
        return json.dumps(data.__dict__, default=bson.json_util.default)
    
    @staticmethod
    @Symphony_Db.atomic()
    def list(data: RequestPostPeriodoList):
        select = Periodo.select()

        if data.descricao != '' and data.descricao != None:
            select = select.where(Periodo.descricao ** ( "%"+str(data.descricao)+"%") )
        
        count_results = select.count()
        
        select = select.paginate(data.page_number, data.page_size)
        
        return_data = []
        
        for result in select.execute():
            return_data.append(
                {
                    'data': [ result.descricao, str(result.dt_inicio), str(result.dt_final)],
                    'key': result.id
                }
                
            )

        response = {
            'count_results': count_results,
            'header': ['Nome','Data de Início','Data de Fim'],
            'body': return_data
        }
        return response
    
    @staticmethod
    @Symphony_Db.atomic()
    def getAll():
        select = Periodo.select()

        return_data = []
        
        for result in select.execute():
            return_data.append(
                {
                    'label': result.descricao + " (" + str(result.dt_inicio) + " á " + str(result.dt_final) + ")",
                    'key': result.id
                }
                
            )

        return return_data