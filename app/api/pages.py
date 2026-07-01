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
from app.models.user import (User)


router = APIRouter()

templates = Jinja2Templates(
    directory="app/templates"
)


@router.get("/")
def volunteer_page(

    request: Request,

    selected_center: int | None = None,

    db: Session = Depends(
        get_db
    )

):

    user_id = request.session.get(
        "user_id"
    )

    if not user_id:

        return RedirectResponse(
            "/login",
            status_code=302
        )

    user = (

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

    if not user:

        request.session.clear()

        return RedirectResponse(
            "/login",
            status_code=302
        )

    if user.role == "director":

        center_id = (

            selected_center

            if selected_center is not None

            else user.center_id

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

    if center_id == 0:

        items = (

            db.query(

                Item,

                func.coalesce(

                    func.sum(
                        Inventory.quantity
                    ),

                    0

                ).label(
                    "total"
                )

            )

            .outerjoin(

                Inventory,

                Inventory.item_id
                ==
                Item.id

            )

            .filter(
                Item.active == True
            )

            .group_by(
                Item.id
            )

            .order_by(
                Item.name
            )

            .all()

        )

    else:

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

            "items":[

                {

                    "item":i,

                    "total":t

                }

                for i,t

                in items

            ],

            "user":user,

            "centers":centers,

            "selected_center":center_id,

            "categories":CATEGORY_LABELS,

            "priorities":PRIORITY_LABELS

        }

    )