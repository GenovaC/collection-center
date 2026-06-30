from app.models.inventory import (
    Inventory
)


def reset_inventory(

    db,

    center_id

):

    (

        db.query(
            Inventory
        )

        .filter(

            Inventory.center_id
            ==
            center_id

        )

        .update(

            {

                Inventory.quantity:0

            }

        )

    )

    db.commit()