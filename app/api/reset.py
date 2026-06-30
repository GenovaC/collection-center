from fastapi import (
    APIRouter,
    Depends,
    Request
)

from fastapi.responses import (
    RedirectResponse
)

from sqlalchemy.orm import (
    Session
)

from app.db.database import (
    get_db
)

from app.models.user import (
    User
)

from app.services.inventory_reset_service import (
    reset_inventory
)

router = APIRouter()


@router.post("/inventory/reset")
def reset_center(

    request: Request,

    center_id:int,

    db:Session=Depends(
    get_db
    )

):

    user_id = request.session.get(
        "user_id"
    )

    if not user_id:

        return RedirectResponse(
            "/login"
        )

    user=(

        db.query(
            User
        )

        .filter(
            User.id
            ==
            user_id
        )

        .first()

    )

    if user.role=="director":

        target_center=center_id

    else:

        target_center=user.center_id

    reset_inventory(

        db,

        target_center

    )

    return RedirectResponse(

        f"/?center_id={target_center}",

        status_code=302

    )