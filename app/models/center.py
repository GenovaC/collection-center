from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from app.db.database import Base


class Center(Base):

    __tablename__ = "centers"

    id: Mapped[int] = mapped_column(
        primary_key=True
    )

    name: Mapped[str] = mapped_column(
        String(100)
    )

    logo: Mapped[str | None] = mapped_column(
        String,
        nullable=True
    )