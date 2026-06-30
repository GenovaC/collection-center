from pydantic import BaseModel
from typing import Literal


class ItemCreate(BaseModel):

    name: str
    category: Literal[
        "medicine",
        "clothing",
        "textiles",
        "food",
        "hygiene",
        "cleaning",
        "tools",
        "medical_supplies",
        "others"
    ]
    priority: Literal[
        "critic",
        "high",
        "mid",
        "low"
    ]
    


class ItemResponse(BaseModel):

    id: int
    name: str
    category: Literal[
        "medicine",
        "clothing",
        "textiles",
        "food",
        "hygiene",
        "cleaning",
        "tools",
        "medical_supplies",
        "others"
    ]
    priority: Literal[
        "critic",
        "high",
        "mid",
        "low"
    ]
    active: bool

    class Config:
        from_attributes = True