from sqlalchemy import func
from sqlalchemy.orm import Session

from app.models.item import Item
from app.models.movement import Movement


def center_dashboard(
    db: Session,
    center_id: int,
):

    rows = (
        db.query(
            Item.name,
            Item.priority,
            func.sum(
                Movement.quantity
            ).label("total"),
        )
        .join(
            Movement,
            Movement.item_id == Item.id,
        )
        .filter(
            Movement.center_id == center_id
        )
        .group_by(
            Item.id,
            Item.name,
            Item.priority,
        )
        .order_by(
            Item.priority.desc()
        )
        .all()
    )

    result = []

    for row in rows:

        result.append(
            {
                "name": row.name,
                "priority": row.priority,
                "total": int(row.total),
            }
        )

    return result