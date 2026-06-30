from sqlalchemy import String, ForeignKey, CheckConstraint
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.orm import relationship
from app.db.database import Base
from app.models.center import Center


class User(Base):

    __tablename__ = "users"

    __table_args__ = (
        CheckConstraint(
            "role IN ('volunteer','director')",
            name="valid_role"
        ),
    )

    id: Mapped[int] = mapped_column(
        primary_key=True
    )

    name: Mapped[str] = mapped_column(
        String(100)
    )

    role: Mapped[str] = mapped_column(
        String(50)
    )

    center_id: Mapped[int] = mapped_column(
        ForeignKey("centers.id")
    )

    username: Mapped[str] = mapped_column(
        unique=True,
        index=True
    )

    password_hash: Mapped[str]

    center: Mapped["Center"] = relationship()

    
    