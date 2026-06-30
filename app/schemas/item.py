from pydantic import BaseModel
from typing import Literal


class ItemCreate(BaseModel):

    name: str
    category: Literal[
        "medicine",
        "pediatric_medications",
        "clothing",
        "textiles",
        "food",
        "hygiene",
        "cleaning",
        "tools",
        "medical_supplies",
        "for_children",
        "for_rescuers",
        "veterinary_use",
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
        "pediatric_medications",
        "clothing",
        "textiles",
        "food",
        "hygiene",
        "cleaning",
        "tools",
        "medical_supplies",
        "for_children",
        "for_rescuers",
        "veterinary_use",
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