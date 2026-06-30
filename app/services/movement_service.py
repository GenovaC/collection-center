from sqlalchemy.orm import Session

from app.models.movement import Movement


def create_movement(
    db: Session,
    center_id: int,
    item_id: int,
    user_id: int,
    quantity: int,
):

    movement = Movement(
        center_id=center_id,
        item_id=item_id,
        user_id=user_id,
        quantity=quantity,
    )

    db.add(movement)

    db.commit()

    db.refresh(movement)

    return movement