
from fastapi import (
    APIRouter,
    Request,
    Form,
    Depends
)

from app.core.security import (
    verify_password
)

from fastapi.responses import (
    RedirectResponse
)

from fastapi.templating import (
    Jinja2Templates
)

from sqlalchemy.orm import (
    Session
)

from app.db.database import (
    get_db
)

from app.models.user import User


router = APIRouter()

templates = Jinja2Templates(
    directory="app/templates"
)


@router.get(
    "/login"
)
def login_page(
    request: Request
):

    return templates.TemplateResponse(

        request,

        "login.html",

        {}

    )


@router.post("/login")
def login(

    request: Request,

    username: str = Form(...),

    password: str = Form(...),

    db: Session = Depends(
    get_db
    )

    ):

        user = (

            db.query(
                User
            )

            .filter(
                User.username
                ==
                username
            )

            .first()

        )

        if not user:

            return templates.TemplateResponse(

                request,

                "login.html",

                {

                    "error":

                    "Credenciales inválidas"

                }

            )

        if not verify_password(

            password,

            user.password_hash

        ):

            return templates.TemplateResponse(

                request,

                "login.html",

                {

                    "error":

                    "Credenciales inválidas"

                }

            )

        request.session[
            "user_id"
        ] = user.id

        return RedirectResponse(
            "/",
            302
        )

@router.get("/logout")
def logout(request: Request):

    request.session.clear()

    return RedirectResponse(
        "/login",
        302
    )