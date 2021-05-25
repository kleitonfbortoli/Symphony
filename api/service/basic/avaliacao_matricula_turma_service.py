import json
from pydantic import BaseModel
from database.symphony_db import Symphony_Db, Avaliacao_Matricula_Turma
from service.database.database_service import DataBaseService

class AvaliacaoMatriculaTurmaService:
    entity = Avaliacao_Matricula_Turma
    
    @staticmethod
    @Symphony_Db.atomic()
    def store(data: BaseModel):
        DataBaseService.store(AvaliacaoMatriculaTurmaService.entity, data)
        return json.dumps(data.__dict__)