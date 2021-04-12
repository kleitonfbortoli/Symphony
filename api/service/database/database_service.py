from peewee import Model
from pydantic import BaseModel

from database.symphony_db import *

class DataBaseService:
    @staticmethod
    @Symphony_Db.atomic()
    def store(entity: Model, data: BaseModel):
        try:
            json_data = DataBaseService.convertBaseModelToJson(data)
            if(json_data['id']):
                entity.update(**json_data).where(entity.id == json_data['id']).execute()
            else:
                print(json_data)
                print(entity.create(**json_data))
        except Exception as e:
            print(str(e))
            
    @staticmethod
    def convertBaseModelToJson(data: BaseModel):
        json_data = json.loads(json.dumps(data.__dict__))
        return json_data
        