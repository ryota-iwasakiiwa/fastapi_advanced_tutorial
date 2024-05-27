from dataclasses import field
from typing import Annotated

from fastapi import FastAPI
from pydantic.dataclasses import dataclass

@dataclass
class Item:
    name: str
    price: float
    tag: list[str] = field(default_factory=list)
    description: Annotated[str | None, ()] = None
    tax: Annotated[float | None, ()] = None

@dataclass
class Author:
    name: str
    items: list[Item] = field(default_factory=list)

app = FastAPI()

@app.post("/items/", response_model=Item)
async def create_item(item: Item):
    return item

@app.post("/authors/{author_id}/items/", response_model=Author)
async def create_author_items(author_id: str, items: list[Item]):
    return {"name": author_id, "items": items}

@app.get("/authors", response_model=list[Author])
def get_authors():
    return [
        {
            "name": "Breaters",
            "items": [
                {
                    "name": "Island In The Moon",
                    "description": "A place to be be playin' and havin' fun",
                },
                {"name": "Holy Buddies"},
            ],
        },
        {
            "name": "System of an Up",
            "items": [
                {
                    "name": "Salt",
                    "description": "The kombucha mushroom people's favorite",
                },
                {"name": "Pad Thai"},
                {
                    "name": "Lonely Night",
                    "description": "The mostests lonliest nightiest of allest",
                },
            ],
        },
    ]