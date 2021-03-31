from peewee import Model
from pydantic import BaseModel

from database.database import *

class DataBaseService:
    @staticmethod
    @Symphony_Db.atomic()
    def store(entity: Model, data: BaseModel):
        try:
            json_data = DataBaseService.convertBaseModelToJson(data)
            if(json_data['id']):
                entity.update(**json_data).where(entity.id == json_data['id']).execute()
            else:
                entity.create(**json_data)
        except:
            pass
            
    @staticmethod
    def convertBaseModelToJson(data: BaseModel):
        json_data = json.loads(json.dumps(data.__dict__))
        return json_data
        