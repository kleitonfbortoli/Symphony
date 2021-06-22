import json
from pydantic import BaseModel
from database.symphony_db import Symphony_Db, Grupo_Usuario, Grupo
from service.database.database_service import DataBaseService
from service.basic.grupo_service import GrupoService
from constants.request_model import *
from peewee import fn

class GrupoUsuarioService:
    entity = Grupo_Usuario

    @staticmethod
    @Symphony_Db.atomic()
    def get(id: int):
        entity = Grupo_Usuario.get(Grupo_Usuario.id == id)
        return entity.__data__
    
    @staticmethod
    @Symphony_Db.atomic()
    def saveGrupoNaPessoa(data: BaseModel):
        obj = {
            'ref_pessoa': data.key,
            'ref_grupo': data.relation
        }
        
        GrupoUsuarioService.entity.create(**obj)

        return json.dumps(data.__dict__)
    
    @staticmethod
    @Symphony_Db.atomic()
    def deleteGrupoNaPessoa(data: BaseModel):
        
        GrupoUsuarioService.entity.delete().where(GrupoUsuarioService.entity.id == data.key).execute()

        return json.dumps(data.__dict__)
    
    @staticmethod
    @Symphony_Db.atomic()
    def listGroupByPessoa(data: RequestPostGrupoListByPessoa):
        select = Grupo_Usuario.select()

        select = select.where(Grupo_Usuario.ref_pessoa == data.key)
        
        count_results = select.count()

        return_data = []
        
        for result in select.execute():
            grupo = GrupoService.get(result.ref_grupo)
            return_data.append(
                {
                    'data': [ grupo['descricao']],
                    'key': result.id
                }
            )

        response = {
            'count_results': count_results,
            'header': ['Descrição'],
            'body': return_data
        }
        return response
    
    @staticmethod
    @Symphony_Db.atomic()
    def listGroupLivreByPessoa(data: RequestPostGrupoListByPessoa):
        sub_select = Grupo_Usuario.select()

        sub_select = sub_select.where(Grupo_Usuario.ref_pessoa == data.key)
        sub_select = sub_select.where(Grupo_Usuario.ref_grupo == Grupo.id)
        
        select = Grupo.select()
        select = select.where(~fn.EXISTS(sub_select))

        count_results = select.count()

        return_data = []
        
        for result in select.execute():
            return_data.append(
                {
                    'label': result.descricao,
                    'value': result.id
                }
            )

        return return_data