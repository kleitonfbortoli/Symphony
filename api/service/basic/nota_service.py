import json
from pydantic import BaseModel
from database.symphony_db import Symphony_Db, Nota
from service.database.database_service import DataBaseService
from service.basic.serie_service import SerieService
from constants.request_model import *
class NotaService:
    entity = Nota

    @staticmethod
    @Symphony_Db.atomic()
    def get(id: int):
        entity = Nota.get(Nota.id == id)
        return entity.__data__

    @staticmethod
    @Symphony_Db.atomic()
    def storeNota(data: BaseModel):
        DataBaseService.store(NotaService.entity, data)
        return json.dumps(data.__dict__)
    
    @staticmethod
    @Symphony_Db.atomic()
    def list(data: RequestPostNotaList):
        select = Nota.select()

        if data.descricao != '' and data.descricao != None:
            select = select.where(Nota.descricao ** ( "%"+str(data.descricao)+"%") )
        
        count_results = select.count()
        
        select = select.paginate(data.page_number, data.page_size)
        
        return_data = []
        
        for result in select.execute():
            serie = SerieService.get(result.ref_serie)
            return_data.append(
                [ result.descricao, result.ordem, serie.descricao]
            )

        response = {
            'count_results': count_results,
            'header': ['Descrição','Ordem','Série'],
            'body': return_data
        }
        return response