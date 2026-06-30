from sqlalchemy import (
    String,
    Integer,
    Boolean
)

from sqlalchemy.orm import (
    Mapped,
    mapped_column
)

from app.db.database import Base


class Item(Base):

    __tablename__ = "items"

    id: Mapped[int] = mapped_column(
        primary_key=True
    )

    name: Mapped[str] = mapped_column(
        String(200),
        unique=True
    )

    category: Mapped[str] = mapped_column(
        String(100)
    )

    priority: Mapped[str] = mapped_column(
        String(10),
        nullable=False,
    )

    active: Mapped[bool] = mapped_column(
        Boolean,
        default=True
    )