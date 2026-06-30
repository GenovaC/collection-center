from fastapi import (
    Request,
    Depends,
    HTTPException
)

from sqlalchemy.orm import (
    Session
)

from app.db.database import (
    get_db
)

from app.models.user import User


def current_user(
    request: Request,
    db: Session = Depends(
        get_db
    )
):

    user_id = (
        request
        .session
        .get(
            "user_id"
        )
    )

    if not user_id:

        raise HTTPException(
            401
        )

    return (
        db.query(
            User
        )

        .get(
            user_id
        )
    )