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
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.units import cm
from reportlab.platypus import Paragraph
from reportlab.lib.styles import ParagraphStyle

from sqlalchemy import func

from app.models.inventory import Inventory
from app.models.item import Item
from app.core.constants import CATEGORY_LABELS


def generate_pdf_report(db, center, is_global=False):

    # =========================
    # TITLE
    # =========================
    styles = getSampleStyleSheet()

    heading = styles["Heading1"]
    heading.alignment = TA_CENTER

    normal = styles["Normal"]
    normal.alignment = TA_CENTER

    if is_global:
        report_title = "Recaudación consolidada - Gerencia Estadal Bolívar"
    else:
        report_title = center.name

    # =========================
    # QUERY DATA
    # =========================
    if is_global:

        rows = (
            db.query(
                Item,
                func.coalesce(func.sum(Inventory.quantity), 0)
            )
            .join(
                Inventory,
                Inventory.item_id == Item.id
            )
            .group_by(Item.id)
            .order_by(Item.name)
            .all()
        )

    else:

        rows = (
            db.query(
                Item,
                func.coalesce(Inventory.quantity, 0)
            )
            .join(
                Inventory,
                Inventory.item_id == Item.id
            )
            .filter(
                Inventory.center_id == center.id
            )
            .order_by(Item.name)
            .all()
        )

    # =========================
    # PDF BUILD
    # =========================
    buffer = BytesIO()

    doc = SimpleDocTemplate(
        buffer,
        topMargin=2 * cm,
        bottomMargin=2 * cm
    )

    content = []

    # =========================
    # LOGO
    # =========================
    logo_path = "app/static/Logo El Sistema.jpg"

    if exists(logo_path):

        logo = Image(
            logo_path,
            width=3.5 * cm,
            height=3.5 * cm
        )

        logo.hAlign = "CENTER"
        content.append(logo)
        content.append(Spacer(1, 15))

    # =========================
    # TITLE
    # =========================
    content.append(
        Paragraph(
            report_title,
            heading
        )
    )

    content.append(Spacer(1, 20))

    # =========================
    # TABLE HEADER
    # =========================
    data = [
        ["Donación", "Categoría", "Unidades recaudadas"]
    ]

    # =========================
    # TABLE ROWS
    # =========================

    cell_style = ParagraphStyle(
        name="cell",
        fontSize=10,
        leading=12
    )
    
    for item, qty in rows:

        category_key = str(item.category).split(".")[-1].lower()
        category_label = CATEGORY_LABELS.get(category_key, category_key)

        data.append([

            Paragraph(item.name, cell_style),

            Paragraph(category_label, cell_style),

            str(int(qty or 0))

        ])

    # =========================
    # TABLE STYLE
    # =========================
    table = Table(
        data,
        colWidths=[7*cm, 5*cm, 4*cm]
    )

    table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#1565C0")),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
        ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("ALIGN", (0, 0), (-1, 0), "CENTER"),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
    ]))

    content.append(table)
    content.append(Spacer(1, 80))

    # =========================
    # SIGNATURE
    # =========================
    content.append(Paragraph("___________________________", normal))
    content.append(Paragraph("Firma de la Gerencia", normal))

    doc.build(content)

    buffer.seek(0)
    return buffer