from bson.objectid import ObjectId
from pydantic import BaseModel

class UserIn(BaseModel):
    username: str
    password: str


class User(UserIn):
    _Id: ObjectId = None
    uploaded_datasets: list = ()
    label_datasets: list = ()
    token: str = ""



