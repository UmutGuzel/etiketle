from fastapi import APIRouter, UploadFile, File, Form, Request
from fastapi.responses import StreamingResponse
from ..database import *
import pandas as pd
import io

router = APIRouter()

@router.post('/upload')
async def upload(file: UploadFile = File(...), text: str = Form(...), title: str = Form(...)):
    dataframe = pd.read_csv(file.file)
    data = dataframe.iloc[:, 0].tolist()
    print(data)
    print(text)
    print(title)
    create_dateset(title, text, len(data))
    dataset_metadata = get_dataset(title)
    dataset_metadata["_id"] = str(dataset_metadata["_id"])
    create_many_data(dataset_metadata["_id"], data)

@router.get("/datasets")
async def get_datasets():
    return get_all_datasets()

@router.post('/data')
async def get_data(request: Request):
    body = await request.json()
    id = body.get('id')
    data = get_data_by_id(id)
    return {"message": "The data was found", "data": data}

@router.post('/dataupdate')
async def data_update(request: Request):
    body = await request.json()
    id = body.get('id')
    Y = body.get('Y')
    update_data(id, Y)

@router.post("/download")
async def download(title: str = Form(...)):
    data = get_all_data_with_dataset_title(title)
    df = pd.DataFrame(columns=["X", "Y"])
    for d in data:
        df.loc[len(df)] = {"X": d["X"], "Y": d["Y"]}

    csv_file_name = "dataset.csv"

    csv_data = df.to_csv(index=False)
    file_like = io.StringIO(csv_data)
    response = StreamingResponse(file_like, media_type="text/csv")
    response.headers["Content-Disposition"] = f"attachment; filename={csv_file_name}"
    return response

