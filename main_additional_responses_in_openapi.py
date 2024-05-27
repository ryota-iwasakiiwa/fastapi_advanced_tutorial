from typing import Annotated, Union
from fastapi import FastAPI
from fastapi.responses import JSONResponse, FileResponse
from pydantic import BaseModel

class Item(BaseModel):
    id: str
    value: str

class Message(BaseModel):
    message: str

responses = {
    404: {"description": "Item not found"},
    302: {"description": "The item was moved"},
    403: {"description": "Not enough privileges"},
}

app = FastAPI()

@app.get(
    "/items/{item_id}",
    response_model=Item,
    responses={404: {"model": Message}},
)
async def read_item(item_id: str):
    if item_id == "foo":
        return {"id": "foo", "value": "There goes my hero"}
    return JSONResponse(status_code=404, content={"message": "Item not found"})

@app.get(
    "/items/{item_id}/image",
    response_model=Item,
    responses={
        200: {
            "content": {"image/png": {}},
            "description": "Return the JSON item or an image.",
        }
    },
)
async def read_item_image(item_id: str, img: Union[str | None] = None):
    if img:
        return FileResponse("image.png", media_type="image/png")
    else:
        return {"id": item_id, "value": "There goes my hero"}

@app.get(
    "/items/{item_id}/info",
    response_model=Item,
    responses={
        404: {"model": Message, "description": "The item was not found"},
        200: {
            "description": "Item requestd by ID",
            "content": {
                "application/json": {
                    "example": {"id": "bar", "value": "The var tenders"}
                }
            }
        }
    }
)
async def read_item_info(item_id: str):
    if item_id == "foo":
        return {"id": "foo", "value": "There goes my hero"}
    else:
        return JSONResponse(status_code=404, content={"message": "Item not found"})
    
@app.get(
    "/item/{item_id}/combine",
    response_model=Item,
    responses={**responses, 200: {"content": {"image/png": {}}}}
)
async def read_item_combine(item_id: str, img: Union[str | None] = None):
    if img:
        return FileResponse("image.png", media_type="image/png")
    else:
        return {"id": item_id, "value": "There goes my hero"}