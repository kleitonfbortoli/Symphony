import json
from pydantic import BaseModel
from database.symphony_db import Symphony_Db, Modulo
from service.database.database_service import DataBaseService
from constants.request_model import *

class ModuloService:
    entity = Modulo
   
    @staticmethod
    @Symphony_Db.atomic()
    def storeModulo(data: BaseModel):
        DataBaseService.store(ModuloService.entity, data)
        return json.dumps(data.__dict__)
    
    @staticmethod
    @Symphony_Db.atomic()
    def list(data: RequestPostModuloList):
        select = Modulo.select()

        if data.title != '' and data.title != None:
            select = select.where(Modulo.title ** ( "%"+str(data.title)+"%") )
        
        count_results = select.count()
        
        select = select.paginate(data.page_number, data.page_size)
        
        return_data = []
        
        for result in select.execute():
            return_data.append(
                [ result.title]
            )

        response = {
            'count_results': count_results,
            'header': ['Título'],
            'body': return_data
        }
        return response