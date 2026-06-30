from fastapi import (
    APIRouter,
    Depends
)

from sqlalchemy.orm import Session

from app.db.database import (
    get_db
)

from app.services.dashboard_service import (
    center_dashboard
)

router = APIRouter()


@router.get(
    "/dashboard/{center_id}"
)
def dashboard(
    center_id: int,
    db: Session = Depends(
        get_db
    )
):

    return center_dashboard(
        db,
        center_id
    )