from enum import Enum

from fastapi import FastAPI


class ModelName(str, Enum):
    uno = "uno"
    due = "due"
    tre = "tre"


app = FastAPI()

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/items/")
async def read_item_query(skip:int =0, limit: int = 10):
    return fake_items_db[skip + limit]


@app.get("/items/{item_id}")
async def read_item(item_id:int):
    return {"item_id": item_id}



@app.get("/get_model/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.uno:
        return {"model_name": model_name, "message": "E' uno!"}
    
    if model_name.value == "due":
        return {"model_name": model_name, "message": "E' due!"}
    
    return {"model_name": model_name, "message": "Mmmmm secondo me è 3!"}