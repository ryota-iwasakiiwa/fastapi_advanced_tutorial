from contextlib import asynccontextmanager

from fastapi import FastAPI

items = {}

@asynccontextmanager
async def lifespan(app: FastAPI):
    items["foo"] = {"name": "Fighters"}
    items["bar"] = {"name": "Tenders"}
    yield

app = FastAPI(lifespan=lifespan)

# @app.on_event("startup")
# async def startup_event():
#     items["foo"] = {"name": "Fighters"}
#     items["bar"] = {"name": "Tenders"}

@app.get("/items/{item_id}")
async def read_item(item_id: str):
    return items[item_id]