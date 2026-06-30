from fastapi import (
    APIRouter,
    Depends,
    Request
)

from fastapi.responses import (
    StreamingResponse, RedirectResponse
)

from sqlalchemy.orm import (
    Session
)

from app.core.auth import require_login
from app.db.database import (
    get_db
)

from app.models.user import User
from app.models.center import Center

from app.services.report_excel_service import (
    generate_excel_report
)

router = APIRouter()


@router.get(
    "/export/excel"
)
def export_excel(

    request: Request,

    center_id: int | None = None,

    db: Session = Depends(
        get_db
    )

):
    
    redirect = require_login(
        request
    )

    if redirect:
        return redirect

    user_id = request.session.get(
        "user_id"
    )

    user = (

        db.query(
            User
        )

        .filter(
            User.id == user_id
        )

        .first()

    )

    if (

        user.role
        ==
        "director"

        and

        center_id

    ):

        center = (

            db.query(
                Center
            )

            .filter(
                Center.id == center_id
            )

            .first()

        )

    else:

        center = user.center

    file = generate_excel_report(
        db,
        center
    )

    return StreamingResponse(

        file,

        media_type=(

            "application/"

            "vnd.openxmlformats-"

            "officedocument."

            "spreadsheetml.sheet"

        ),

        headers={

            "Content-Disposition":

            f'attachment; filename="{center.name}.xlsx"'

        }

    )   