from pydantic import BaseModel
from typing import Literal


class UserCreate(
    BaseModel
):

    name: str

    role: Literal[
        "volunteer",
        "director",
    ]

    center_id: int


class UserResponse(
    BaseModel
):

    id: int

    name: str

    role: Literal[
        "volunteer",
        "director",
    ]

    center_id: int

    model_config = {
        "from_attributes": True
    }