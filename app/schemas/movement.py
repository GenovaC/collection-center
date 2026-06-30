from pydantic import BaseModel


class MovementCreate(BaseModel):

    center_id: int
    item_id: int
    user_id: int
    quantity: int


class MovementResponse(BaseModel):

    id: int
    center_id: int
    item_id: int
    user_id: int
    quantity: int

    class Config:
        from_attributes = True