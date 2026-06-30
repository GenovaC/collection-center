from fastapi import (
    APIRouter,
    Depends, 
    Form
)

from sqlalchemy import func
from sqlalchemy.orm import Session

from app.db.database import (
    get_db
)

from app.schemas.movement import (
    MovementCreate,
    MovementResponse
)

from app.services.movement_service import (
    create_movement
)

from fastapi.responses import Response
from fastapi.responses import HTMLResponse

from app.models.movement import Movement
from app.models.item import Item

router = APIRouter()


@router.post(
    "/movements",
    response_model=MovementResponse
)
def register_movement(
    data: MovementCreate,
    db: Session = Depends(get_db)
):

    return create_movement(
        db,
        data.center_id,
        data.item_id,
        data.user_id,
        data.quantity,
    )

@router.post("/movements/htmx")
def register_movement_htmx(
    center_id: int = Form(...),
    item_id: int = Form(...),
    user_id: int = Form(...),
    quantity: int = Form(...),
    db: Session = Depends(get_db),
):

    create_movement(
        db,
        center_id,
        item_id,
        user_id,
        quantity,
    )

    return Response(status_code=204)

@router.get("/movements/total/{item_id}", response_class=HTMLResponse)
def get_item_total(
    item_id: int,
    center_id: int,
    db: Session = Depends(get_db),
):

    total = (
        db.query(func.sum(Movement.quantity))
        .filter(
            Movement.item_id == item_id,
            Movement.center_id == center_id
        )
        .scalar()
    )
    print("TOTAL REQUEST:", item_id, center_id)

    if total is None:
        total = 0

    return str(total)