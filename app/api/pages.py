from fastapi import (
    APIRouter,
    Request,
    Depends
)

from fastapi.responses import RedirectResponse

from fastapi.templating import (
    Jinja2Templates
)
from sqlalchemy import func, case

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
    sort_by: str = "name",
    order: str = "asc",
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

    priority_order = case(
        {
            "critic": 1,
            "high": 2,
            "mid": 3,
            "low": 4
        },
        value=Item.priority,
        else_=5
    )

    category_order = case(
    *[
        (
            key,
            label
        )

        for key, label
        in CATEGORY_LABELS.items()
    ],
    value=Item.category
)

    sort_map = {
        "category": category_order,
        "name": Item.name,
        "priority": priority_order,
        "quantity": "quantity"
    }

    sort_column = sort_map.get(
        sort_by,
        Item.name
    )

    if center_id == 0:

        quantity_total = func.coalesce(
            func.sum(
                Inventory.quantity
            ),
            0
        )

        query = (
            db.query(
                Item,
                quantity_total.label(
                    "total"
                )
            )

            .outerjoin(
                Inventory,
                Inventory.item_id == Item.id
            )

            .filter(
                Item.active == True
            )

            .group_by(
                Item.id
            )

        )

    else:

        quantity_total = func.coalesce(
            Inventory.quantity,
            0
        )

        query = (

            db.query(
                Item,
                quantity_total.label(
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
        )

    if sort_by == "quantity":

        sort_expression = quantity_total

    else:

        sort_expression = sort_column

    if order == "desc":

        query = query.order_by(
            sort_expression.desc()
        )

    else:

        query = query.order_by(
            sort_expression.asc()
        )

    items = query.all()

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
            "priorities":PRIORITY_LABELS,
            "sort_by": sort_by,
            "order": order
        }

    )