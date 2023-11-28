from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from pydantic import BaseModel


app = FastAPI(title="meme test api")
api_app = FastAPI(title="api app")
app.mount("/api",api_app)




class Item(BaseModel):
    item_id: int


@app.get("/meow/")
async def root():
    return {"message": "Hello World HEH"}


@app.get('/favicon.ico', include_in_schema=False)
async def favicon():
    return FileResponse('favicon.ico')


@app.get("/item/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}


@app.get("/items/")
async def list_items():
    return [{"item_id": 1, "name": "Foo"}, {"item_id": 2, "name": "Bar"}]


@app.post("/items/")
async def create_item(item: Item):
    return item


app.mount("/",StaticFiles(directory="gui",html=True),name="gui")