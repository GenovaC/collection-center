from fastapi import (
    APIRouter,
    Depends, 
    HTTPException,
    Form
)

from sqlalchemy.orm import Session

from app.db.database import (
    get_db
)

from app.schemas.item import (
    ItemCreate,
    ItemResponse
)

from app.services.item_service import (
    create_item
)

from app.models.item import Item

from fastapi.responses import (RedirectResponse)


router = APIRouter()


@router.post(
    "/items"
)
def create_new_item(

    name: str = Form(...),
    category: str = Form(...),
    priority: str = Form(...),
    db: Session = Depends(
        get_db
    )
):

    create_item(
        db,
        name,
        category,
        priority,
    )

    return RedirectResponse(
        url="/",
        status_code=303
    )


@router.get(
    "/items",
    response_model=list[ItemResponse]
)
def get_items(
    db: Session = Depends(
        get_db
    )
):

    items = (
        db.query(Item)

        .filter(
            Item.active == True
        )

        .order_by(
            Item.priority.desc()
        )

        .all()
    )

    return items

@router.get(
    "/items/{item_id}",
    response_model=ItemResponse
)
def get_item(
    item_id: int,
    db: Session = Depends(
        get_db
    )
):

    item = (
        db.query(Item)

        .filter(
            Item.id == item_id
        )

        .first()
    )

    if not item:
        raise HTTPException(
            status_code=404,
            detail="Item no encontrado"
        )

    return item