from sqlalchemy.orm import Session

from app.models.item import Item


def create_item(
    db: Session,
    name: str,
    category: str,
    priority: int,
):

    normalized = (
        name
        .strip()
        .lower()
    )

    existing = (
        db.query(Item)
        .filter(
            Item.name.ilike(
                normalized
            )
        )
        .first()
    )

    if existing:

        return existing

    item = Item(
        name=name.strip(),
        category=category,
        priority=priority,
    )

    db.add(item)

    db.commit()

    db.refresh(item)

    return item