from fastapi import (
    APIRouter,
    Depends,
    Form
)

from fastapi.responses import (
    Response
)

from sqlalchemy.orm import (
    Session
)

from app.db.database import (
    get_db
)

from app.services.inventory_service import (
    set_quantity
)

router = APIRouter()


@router.post(
    "/inventory"
)
def update_inventory(

    center_id: int = Form(...),

    item_id: int = Form(...),

    user_id: int = Form(...),

    quantity: int = Form(...),

    db: Session = Depends(
        get_db
    )

):

    if center_id == 0:
        return Response(
            status_code=204
        )

    if quantity < 0:
        quantity = 0

    set_quantity(

        db,

        center_id,

        item_id,

        user_id,

        quantity

    )

    return Response(
        status_code=204
    )