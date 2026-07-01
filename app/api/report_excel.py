from fastapi import (
    APIRouter,
    Depends,
    Request
)

from fastapi.responses import StreamingResponse

from sqlalchemy.orm import Session

from app.core.auth import require_login
from app.db.database import get_db

from app.models.user import User
from app.models.center import Center

from app.services.report_excel_service import (
    generate_excel_report
)

router = APIRouter()


@router.get("/export/excel")
def export_excel(
    request: Request,
    center_id: int | None = None,
    db: Session = Depends(get_db)
):

    redirect = require_login(request)
    if redirect:
        return redirect

    user_id = request.session.get("user_id")

    user = (
        db.query(User)
        .filter(User.id == user_id)
        .first()
    )

    if not user:
        return RedirectResponse("/login", status_code=302)

    is_global = (
        user.role == "director"
        and center_id == 0
    )

    if is_global:

        center = None

    elif (
        user.role == "director"
        and center_id
    ):

        center = (
            db.query(Center)
            .filter(Center.id == center_id)
            .first()
        )

    else:

        center = user.center

    file = generate_excel_report(
        db,
        center,
        is_global=is_global
    )

    filename = (
        "reporte_global"
        if is_global
        else center.name
    ).replace(" ", "_")

    return StreamingResponse(
        file,
        media_type=(
            "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        ),
        headers={
            "Content-Disposition": f'attachment; filename="{filename}.xlsx"'
        }
    )