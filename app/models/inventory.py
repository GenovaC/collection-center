from datetime import datetime

from sqlalchemy import (
    ForeignKey,
    DateTime
)

from sqlalchemy.orm import (
    Mapped,
    mapped_column
)

from app.db.database import Base


class Inventory(Base):

    __tablename__="inventory"

    id: Mapped[int] = mapped_column(
        primary_key=True
    )

    center_id: Mapped[int] = mapped_column(
        ForeignKey(
            "centers.id"
        )
    )

    item_id: Mapped[int] = mapped_column(
        ForeignKey(
            "items.id"
        )
    )

    quantity: Mapped[int] = mapped_column(
        default=0
    )

    updated_by: Mapped[int]

    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )