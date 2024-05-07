from fastapi import APIRouter
from schemas.api_schemas import Item
from fastapi.responses import FileResponse

api_app = APIRouter()



@api_app.get("/meow/")
async def meow():
    return {"message": "Hello World HEH"}


@api_app.get('/favicon.ico', include_in_schema=False)
async def favicon():
    return FileResponse('gui/favicon.ico')


@api_app.get("/item/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}


@api_app.get("/items/")
async def list_items():
    return [{"item_id": 1, "name": "Foo"}, {"item_id": 2, "name": "Bar"}]


@api_app.post("/items/")
async def create_item(item: Item):
    return item


