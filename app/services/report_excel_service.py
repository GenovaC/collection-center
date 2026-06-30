from io import BytesIO

from openpyxl import Workbook

from openpyxl.styles import (
    Font,
    Alignment
)

from openpyxl.drawing.image import (
    Image
)

from app.models.inventory import Inventory
from app.models.item import Item

from app.core.constants import (
    CATEGORY_LABELS
)


def generate_excel_report(
    db,
    center,
):

    rows = (

        db.query(
            Item,
            Inventory.quantity
        )

        .join(
            Inventory,
            Inventory.item_id == Item.id
        )

        .filter(
            Inventory.center_id == center.id,
            Inventory.quantity > 0
        )

        .order_by(
            Item.name
        )

        .all()

    )

    wb = Workbook()

    ws = wb.active

    ws.title = "Donaciones"

    # Logo
    try:

        logo = Image(
            "app/static/Logo El Sistema.jpg"
        )

        logo.width = 120
        logo.height = 120

        ws.add_image(
            logo,
            "B1"
        )

    except:
        pass

    # título
    ws.merge_cells(
        "A8:C8"
    )

    cell = ws["A8"]

    cell.value = center.name

    cell.font = Font(
        size=18,
        bold=True
    )

    cell.alignment = Alignment(
        horizontal="center"
    )

    # encabezados
    start = 10

    headers = [

        "Donación",

        "Categoría",

        "Unidades recaudadas"

    ]

    for col, value in enumerate(
        headers,
        start=1
    ):

        c = ws.cell(
            row=start,
            column=col
        )

        c.value = value

        c.font = Font(
            bold=True
        )

    # contenido
    row_num = start + 1

    for item, qty in rows:

        category = CATEGORY_LABELS.get(

            str(
                item.category
            )
            .split(".")[-1]
            .lower(),

            item.category

        )

        ws.cell(
            row=row_num,
            column=1
        ).value = item.name

        ws.cell(
            row=row_num,
            column=2
        ).value = category

        ws.cell(
            row=row_num,
            column=3
        ).value = qty

        row_num += 1

    # ancho columnas
    ws.column_dimensions["A"].width = 40
    ws.column_dimensions["B"].width = 22
    ws.column_dimensions["C"].width = 18

    # firma
    row_num += 4

    ws.merge_cells(

        f"A{row_num}:C{row_num}"

    )

    ws.cell(

        row=row_num,

        column=1

    ).value = (

        "Responsable del Centro de Acopio"

    )

    ws.cell(

        row=row_num,

        column=1

    ).alignment = Alignment(

        horizontal="center"

    )

    output = BytesIO()

    wb.save(
        output
    )

    output.seek(
        0
    )

    return output