import io
from enum import Enum

import pandas as pd
from fastapi import FastAPI
from typing import Dict, Optional

from fastapi.responses import ORJSONResponse
from pydantic import BaseModel
from starlette.responses import HTMLResponse, StreamingResponse

app = FastAPI()

class RoleName(str, Enum):
    admin = 'Admin'
    writer = 'Writer'
    reader = 'Reader'

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None

@app.get("/")
def root():
    return {"message": "Hello world"}

## Parametros de path

#@app.get("/items/{item_id}")
#def read_item(item_id: int) -> Dict[str, int]:
    #return {"item_id": item_id}

@app.get("/users/me")
def read_current_user():
    return {"user_id":"The current logged user"}

@app.get("/users/{user_id}")
def read_user(user_id: str):
    return {"user_id": user_id}


@app.get("/roles/{role_name}")
def get_rol_permissions(role_name: RoleName):
    #return role permissions

    if role_name == RoleName.admin:
        return {"rol_name": role_name, "permissions": "Full Access"}

    if role_name == RoleName.writer:
        return {"role_name": role_name, "permissions": "Write Access"}

    return {"role_name": role_name, "permissions": "Read access only"}


# query params

fake_items_db = [{"item_name":"uno"},
                 {"item_name":"dos"},
                 {"item_name":"tres"}]


@app.get("/items/")
def read_items(skip: int=0, limit: int=10):
    return fake_items_db[skip: skip+limit]

@app.get("/items/{item_id}")
def read_item_query(item_id: int, query: Optional[str] = None):
    message = {"item_id": item_id}

    if query:
        message['query'] = query

    return message


@app.get("/users/{user_id}/items/{item_id}")
def read_user_item(user_id: int, item_id: int, query: Optional[str] = None, describe: bool = False):
    item = {"item_id": item_id, "owner_id": user_id}

    if query:
        item['query'] = query

    if describe:
        item['description'] = "This is a long description for the item"

    return item


@app.post("/items/")
def create_item(item: Item):
    return {
        "message": "The item was successfully created",
        "item": item.dict()
    }


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):

    if item.tax == 0 or item.tax is None:
        item.tax = item.price * 0.12

    return {
        "message": "The item was updated",
        "item_id": item_id,
        "item": item.dict()
    }


@app.get("/itemsall", response_class=ORJSONResponse)
def read_long_json():
    return [{"item_id": "item"},
            {"item_id": "item"},
            {"item_id": "item"},
            {"item_id": "item"},
            {"item_id": "item"},
            {"item_id": "item"},
            {"item_id": "item"},
            {"item_id": "item"},
            {"item_id": "item"},
            {"item_id": "item"},
            {"item_id": "item"},
            {"item_id": "item"},
            {"item_id": "item"},
            {"item_id": "item"},
            {"item_id": "item"},
            {"item_id": "item"}]

@app.get("/html", response_class=HTMLResponse)
def read_html():
    return """
    <html>
        <head></head>
        <body>
            <h1>Response with HTML</h1>
        </body>
    </html>
    """

@app.get("/csv")
def get_csv():

    df = pd.DataFrame({"Column A": [1,2], "Column B": [3,4]})

    stream = io.StringIO()

    df.to_csv(stream, index = False)

    response = StreamingResponse(iter([stream.getvalue()]), media_type = 'text/csv')

    response.headers['Content-Disposition'] = "attachment; filename=my_awesome_report.csv"

    return response


## Tarea
@app.get("/operacion/suma")
def get_suma(f_value: int, s_value: int):
    return {"message": f"The result of the sum is: {f_value + s_value}"}

@app.post("/operacion/suma")
def get_suma(f_value: int, s_value: int):
    return {"message": f"The result of the sum is: {f_value + s_value}"}

@app.get("/operacion/resta")
def get_suma(f_value: int, s_value: int):
    return {"message": f"The result of subtraction sum is: {f_value - s_value}"}

@app.post("/operacion/resta")
def get_suma(f_value: int, s_value: int):
    return {"message": f"The result of the subtraction is: {f_value - s_value}"}


@app.get("/operacion/multiplicacion")
def get_suma(f_value: int, s_value: int):
    return {"message": f"The result of multiplication sum is: {f_value * s_value}"}

@app.post("/operacion/multiplicacion")
def get_suma(f_value: int, s_value: int):
    return {"message": f"The result of the multiplication is: {f_value * s_value}"}


@app.get("/operacion/divison")
def get_suma(f_value: int, s_value: int):
    return {"message": f"The result of division sum is: {f_value / s_value}"}

@app.post("/operacion/division")
def get_suma(f_value: int, s_value: int):
    return {"message": f"The result of the division is: {f_value / s_value}"}