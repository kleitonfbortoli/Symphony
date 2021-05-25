import json
from pydantic import BaseModel
from database.symphony_db import Symphony_Db, Periodo_Academico
from service.database.database_service import DataBaseService
from constants.request_model import *
class PeriodoService:
    entity = Periodo_Academico

    @staticmethod
    @Symphony_Db.atomic()
    def storePeriodo(data: BaseModel):
        DataBaseService.store(PeriodoService.entity, data)
        return json.dumps(data.__dict__)
    
    @staticmethod
    @Symphony_Db.atomic()
    def list(data: RequestPostPeriodoAcademicoList):
        select = Periodo_Academico.select()

        if data.descricao != '' and data.descricao != None:
            select = select.where(Periodo_Academico.descricao ** ( "%"+str(data.descricao)+"%") )
        
        count_results = select.count()
        
        select = select.paginate(data.page_number, data.page_size)
        
        return_data = []
        
        for result in select.execute():
            return_data.append(
                [ result.nome, str(result.inicio), str(result.dt_final)]
            )

        response = {
            'count_results': count_results,
            'header': ['Nome','Data de Início','Data de Fim'],
            'body': return_data
        }
        return response