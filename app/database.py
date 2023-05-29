from bson.objectid import ObjectId

from app import client
from .models import user


def is_there_user(username: str) -> bool:
    user_collection = client['etiketle'].user
    return user_collection.find_one({"username": username}) is not None


def create_user(user_data: user.User):
    user_collection = client['etiketle'].user
    return user_collection.insert_one(user_data.dict())


def get_user(user_data: user.User):
    user_collection = client['etiketle'].user
    return user_collection.find_one({"$and": [{"username": user_data.username},
                                              {"password": user_data.password}]})


def create_dateset(title: str, description: str, number_of_Line: int):
    metadata_collection = client['etiketle'].dataset_metadata
    return metadata_collection.insert_one({
        "title": title,
        "description": description,
        "number_of_line": number_of_Line,
        "labeled_line": 0
    })


def get_dataset(title: str):
    metadata_collection = client['etiketle'].dataset_metadata
    return metadata_collection.find_one({"title": title})


def create_many_data(id: str, data: list):
    datasets_collection = client['etiketle'].datasets
    for d in data:
        datasets_collection.insert_one({
            "metadata_Id": id,
            "X": d,
            "Y": "",
            "is_labeled": False
        })

    return True


def get_all_datasets():
    metadata_collection = client['etiketle'].dataset_metadata
    response = list(metadata_collection.find({}))
    for i in range(len(response)):
        response[i]["_id"] = str(response[i]["_id"])
    return response


def get_data_by_id(id: str):
    datasets_collection = client['etiketle'].datasets
    data = datasets_collection.find_one({"$and": [{"metadata_Id": id},
                                                  {"is_labeled": False}]})
    data["_id"] = str(data["_id"])
    return data


def update_data(id: str, label: str):
    datasets_collection = client['etiketle'].datasets
    filter = {'_id': ObjectId(id)}
    values = {"$set": {'Y': label,
                       'is_labeled': True}}
    return datasets_collection.update_one(filter, values)


def get_user_by_id(_id: ObjectId):
    user_collection = client['etiketle'].user
    return user.User(**user_collection.find_one({"id": _id}))


def get_user_with_username(username: str):
    user_collection = client['etiketle'].user
    return user.User(**user_collection.find_one({"username": username}))

def get_all_data_with_dataset_title(title: str):
    metadata_collection = client['etiketle'].dataset_metadata
    metadata = metadata_collection.find_one({"title": title})
    id = str(metadata['_id'])
    datasets_collection = client['etiketle'].datasets
    return datasets_collection.find({"metadata_Id": id})
