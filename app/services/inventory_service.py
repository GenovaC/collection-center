from datetime import (
    datetime
)

from app.models.inventory import (
    Inventory
)


def set_quantity(

    db,

    center_id,

    item_id,

    user_id,

    quantity

):

    row = (

        db.query(
            Inventory
        )

        .filter(

            Inventory.center_id
            ==
            center_id,

            Inventory.item_id
            ==
            item_id

        )

        .first()

    )

    if row:

        row.quantity = quantity

        row.updated_by = user_id

        row.updated_at = datetime.utcnow()

    else:

        row = Inventory(

            center_id=center_id,

            item_id=item_id,

            quantity=quantity,

            updated_by=user_id

        )

        db.add(
            row
        )

    db.commit()

    db.refresh(
        row
    )

    return row