from pydantic import BaseModel
from datetime import datetime
from bson.objectid import ObjectId


class Metadata(BaseModel):
    title: str
    description: str
    number_of_line: int
    owner_id: ObjectId
    labeled_line: int = 0


class Datasets(BaseModel):
    x: str
    metadata_id: ObjectId
    y: str = ""
    is_labeled: bool = False
    labeler_Id: ObjectId = None
    labeled_date: datetime = None