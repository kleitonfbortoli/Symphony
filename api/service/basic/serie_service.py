import json
from pydantic import BaseModel
from database.symphony_db import Symphony_Db, Serie
from service.database.database_service import DataBaseService
from constants.request_model import *
class SerieService:
    entity = Serie

    @staticmethod
    @Symphony_Db.atomic()
    def get(id: int):
        entity = Serie.get(Serie.id == id)
        return entity.__data__
    
    @staticmethod
    @Symphony_Db.atomic()
    def storeSerie(data: BaseModel):
        DataBaseService.store(SerieService.entity, data)
        return json.dumps(data.__dict__)
    
    @staticmethod
    @Symphony_Db.atomic()
    def list(data: RequestPostSerieList):
        select = Serie.select()

        if data.nome != '' and data.nome != None:
            select = select.where(Serie.nome ** ( "%"+str(data.nome)+"%") )
        
        if data.ch_total != '' and data.ch_total != None:
            select = select.where(Serie.ch_total == data.ch_total )

        count_results = select.count()
        
        select = select.paginate(data.page_number, data.page_size)
        
        return_data = []
        
        for result in select.execute():
            return_data.append(
                {
                    'data': [ result.nome, str(result.ch_total)],
                    'key': result.id
                }
            )

        response = {
            'count_results': count_results,
            'header': ['Nome','Carga Horária Total'],
            'body': return_data
        }
        return response
    
    @staticmethod
    @Symphony_Db.atomic()
    def getAll():
        select = Serie.select()

        return_data = []
        
        for result in select.execute():
            return_data.append(
                {
                    'label': result.nome,
                    'key': result.id
                }
                
            )

        return return_data