from fastapi import (
    APIRouter,
    Request,
    Depends
)

from fastapi.responses import RedirectResponse


from fastapi.templating import (
    Jinja2Templates
)
from sqlalchemy import func

from sqlalchemy.orm import (
    Session
)

from app.db.database import (get_db)
from app.models.item import (Item)
from app.models.center import (Center)
from app.models.inventory import (Inventory)
from app.core.auth import (current_user)
from app.core.constants import (
    CATEGORY_LABELS,
    PRIORITY_LABELS
)


router = APIRouter()

templates = Jinja2Templates(
    directory="app/templates"
)


@router.get("/")
def volunteer_page(
    request: Request,
    selected_center: int | None = None,
    user=Depends(
        current_user
    ),
    db: Session = Depends(
        get_db
    )
):
    
    if not request.session.get("user_id"):
        return RedirectResponse("/login", 302)

    if user.role == "director":

        center_id = (
            selected_center
            or
            user.center_id
        )

        centers = (
            db.query(
                Center
            )
            .order_by(
                Center.name
            )
            .all()
        )

    else:

        center_id = (
            user.center_id
        )
        centers = []

    items = (

        db.query(
            Item,
            func.coalesce(
                Inventory.quantity,
                0
            ).label(
                "total"
            )
        )

        .outerjoin(

            Inventory,
            (
                Inventory.item_id
                ==
                Item.id
            )

            &

            (
                Inventory.center_id
                ==
                center_id
            )

        )

        .filter(
            Item.active == True
        )

        .order_by(
            Item.name
        )

        .all()

    )

    return templates.TemplateResponse(
        request,
        "volunteer.html",

        {
            "request": request,
            "items": [
                {
                "item": i,
                "total": t
                }

                for i, t
                    in items

            ],
            "user": user,
            "centers": centers,
            "selected_center": center_id,
            "categories": CATEGORY_LABELS,
            "priorities": PRIORITY_LABELS
        }

    )