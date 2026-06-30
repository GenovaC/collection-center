from datetime import datetime

from sqlalchemy import (
    Integer,
    ForeignKey,
    DateTime
)

from sqlalchemy.orm import (
    Mapped,
    mapped_column
)

from app.db.database import Base


class Movement(Base):

    __tablename__ = "movements"

    id: Mapped[int] = mapped_column(
        primary_key=True
    )

    center_id: Mapped[int] = mapped_column(
        ForeignKey("centers.id")
    )

    item_id: Mapped[int] = mapped_column(
        ForeignKey("items.id")
    )

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id")
    )

    quantity: Mapped[int] = mapped_column(
        Integer
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )