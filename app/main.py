from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from app.db.database import (
    Base,
    engine
)

from starlette.middleware.sessions import (
    SessionMiddleware
)

from app.api.movements import router

from app.api.auth import (router as auth_router)


from app.models.center import *
from app.models.user import *
from app.models.item import *
from app.models.movement import *
from app.api.dashboard import router as dashboard_router
from app.api.items import (router as items_router)
from app.api.pages import (router as page_router)
from app.api.inventory import router as inventory_router
from app.api.report_pdf import (router as report_router)
from app.api.report_excel import (router as report_excel_router)




Base.metadata.create_all(
    bind=engine
)

app = FastAPI()

app.add_middleware(
    SessionMiddleware,
    secret_key="centro-acopio-2026"
)

app.mount(
    "/static",
    StaticFiles(directory="app/static"),
    name="static"
)

templates = Jinja2Templates(
    directory="app/templates"
)


app.include_router(router)
app.include_router(dashboard_router)
app.include_router(items_router)
app.include_router(page_router)
app.include_router(auth_router)
app.include_router(inventory_router)
app.include_router(report_router)
app.include_router(report_excel_router)


@app.get("/")
def root():

    return {
        "status": "ok"
    }