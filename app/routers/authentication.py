from datetime import datetime, timedelta

import jwt
from fastapi import APIRouter, HTTPException, Request
from fastapi.security import OAuth2PasswordBearer

from ..database import *
from ..models import user

router = APIRouter()

SECRET = "6BAECEA0DDF8957C1DE295284545968261F553C5C39C211412EF04D46AB20C90"
DATE_TIME_TEMPLATE = "%d/%m/%Y %H:%M:%S"

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


def create_token(data: dict, expire_time: timedelta = timedelta(minutes=30)):
    copy_data = data.copy()
    expire = datetime.utcnow() + expire_time
    copy_data.update({"expire": expire.strftime(DATE_TIME_TEMPLATE)})
    return jwt.encode(copy_data, SECRET, algorithm="HS256")


def verify_token(token: str):
    print(token)
    try:
        payload = jwt.decode(token, SECRET, algorithms=["HS256"])
        print(payload)
        # Perform additional validation as needed
        # Example: Check token expiration
        if datetime.utcnow() > datetime.fromtimestamp(payload["exp"]):
            raise HTTPException(status_code=404, detail="Token has expired")
        return payload["username"]
    except:
        raise HTTPException(status_code=404, detail="Invalid token")


@router.post("/register")
async def register(user_in_data: user.UserIn):
    if is_there_user(user_in_data.username):
        raise HTTPException(status_code=404, detail="User already exists")
    if not create_user(user_in_data):
        raise HTTPException(status_code=404, detail="The user could not create.")
    return {"message": "User registered successfully", "data": user_in_data.dict()}


@router.post("/login")
async def login(user_in_data: user.UserIn):
    selected_keys = ["_id", "username"]
    found_user = get_user(user_in_data)
    if found_user is None:
        raise HTTPException(status_code=404, detail="User have not found")
    found_user["_id"] = str(found_user["_id"])
    token = create_token({key: found_user[key] for key in selected_keys})
    found_user.update({'token': token})
    return {"message": "User logged in successfully", "data": found_user}


@router.get("/protected")
def protected(request: Request):
    auth_header = request.headers.get("Authorization")
    return {"auth_header": auth_header}
