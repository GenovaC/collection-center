from io import BytesIO
from os.path import exists

from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
    Image
)

from reportlab.lib import colors

from reportlab.lib.styles import (
    getSampleStyleSheet
)

from reportlab.lib.enums import (
    TA_CENTER
)

from reportlab.lib.units import cm



from reportlab.pdfgen.canvas import Canvas

from app.models.inventory import Inventory
from app.models.item import Item

from app.core.constants import (
    CATEGORY_LABELS
)


def generate_pdf_report(

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

            Inventory.item_id
            ==
            Item.id

        )

        .filter(

            Inventory.center_id
            ==
            center.id,

            Inventory.quantity
            >
            0

        )

        .order_by(
            Item.name
        )

        .all()

    )

    buffer = BytesIO()

    doc = SimpleDocTemplate(

        buffer,

        topMargin=2*cm,

        bottomMargin=2*cm

    )

    styles = getSampleStyleSheet()

    title = styles["Heading1"]

    title.alignment = TA_CENTER

    normal = styles["Normal"]

    normal.alignment = TA_CENTER

    content = []

    # logo

    logo_path = "app/static/Logo El Sistema.jpg"

    if exists(
        logo_path
    ):

        logo = Image(

            logo_path,

            width=3.5*cm,

            height=3.5*cm

        )

        logo.hAlign = "CENTER"

        content.append(
            logo
        )

        content.append(
            Spacer(
                1,
                15
            )
        )

    content.append(
        Paragraph(
            center.name,
            title
        )
    )

    content.append(
        Spacer(
            1,
            20
        )
    )

    data = [

        [

            "Donación",

            "Categoría",

            "Unidades recaudadas"

        ]

    ]

    print(rows)
    for item, qty in rows:

        category_key = (
            str(item.category)
            .split(".")[-1]
            .lower()
        )

        data.append(

            [

                item.name,

                CATEGORY_LABELS.get(
                    category_key,
                    category_key
                ),

                str(qty)

            ]

        )

    table = Table(

        data,

        colWidths=[
            8*cm,
            4*cm,
            4*cm
        ]

    )

    table.setStyle(

        TableStyle([

            (

                "BACKGROUND",

                (
                    0,
                    0
                ),

                (
                    -1,
                    0
                ),

                colors.HexColor(
                    "#1565C0"
                )

            ),

            (

                "TEXTCOLOR",

                (
                    0,
                    0
                ),

                (
                    -1,
                    0
                ),

                colors.white

            ),

            (

                "GRID",

                (
                    0,
                    0
                ),

                (
                    -1,
                    -1
                ),

                1,

                colors.black

            ),

        ])

    )

    content.append(
        table
    )

    content.append(
        Spacer(
            1,
            80
        )
    )

    content.append(

        Paragraph(

            "________________________",

            normal

        )

    )

    content.append(

        Paragraph(

            "Responsable del Centro de Acopio",

            normal

        )

    )

    doc.build(
        content
    )

    buffer.seek(
        0
    )

    return buffer