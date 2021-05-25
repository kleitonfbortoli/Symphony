import json
from pydantic import BaseModel
from database.symphony_db import Symphony_Db, Tipo_Nota
from service.database.database_service import DataBaseService
from constants.request_model import *
class TipoNotaService:
    entity = Tipo_Nota

    @staticmethod
    @Symphony_Db.atomic()
    def storeTipoNota(data: BaseModel):
        DataBaseService.store(TipoNotaService.entity, data)
        return json.dumps(data.__dict__)
    
    @staticmethod
    @Symphony_Db.atomic()
    def list(data: RequestPostTipoNotaList):
        select = Tipo_Nota.select()

        if data.descricao != '' and data.descricao != None:
            select = select.where(Tipo_Nota.descricao ** ( "%"+str(data.descricao)+"%") )
        
        count_results = select.count()
        
        select = select.paginate(data.page_number, data.page_size)
        
        return_data = []
        
        for result in select.execute():
            return_data.append(
                [ result.descricao]
            )

        response = {
            'count_results': count_results,
            'header': ['Descrição'],
            'body': return_data
        }
        return response