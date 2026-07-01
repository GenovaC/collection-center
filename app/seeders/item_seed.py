from app.models.item import Item


def seed_items(db):
    print("🌱 Seeding items...")

    items_data = [

        # ==========================
        # medical_supplies
        # ==========================

        {"name": "Vendas elásticas (unidades)", "category": "medical_supplies", "priority": "high"},
        {"name": "Gasas (paquetes)", "category": "medical_supplies", "priority": "high"},
        {"name": "Algodón (paquetes)", "category": "medical_supplies", "priority": "mid"},
        {"name": "Guantes desechables (cajas)", "category": "medical_supplies", "priority": "critic"},
        {"name": "Jeringas con agujas (unidades)", "category": "medical_supplies", "priority": "high"},
        {"name": "Tensiómetros (unidades)", "category": "medical_supplies", "priority": "mid"},
        {"name": "Oxímetros (unidades)", "category": "medical_supplies", "priority": "high"},
        {"name": "Kits de primeros auxilios (unidades)", "category": "medical_supplies", "priority": "critic"},
        {"name": "Pañales para adultos (paquetes)", "category": "medical_supplies", "priority": "mid"},


        # ==========================
        # medicine
        # ==========================

        {"name": "Acetaminofén (cajas)", "category": "medicine", "priority": "high"},
        {"name": "Ibuprofeno (cajas)", "category": "medicine", "priority": "high"},
        {"name": "Paracetamol (cajas)", "category": "medicine", "priority": "high"},
        {"name": "Amoxicilina (cajas)", "category": "medicine", "priority": "high"},
        {"name": "Ciprofloxacina (cajas)", "category": "medicine", "priority": "high"},
        {"name": "Solución fisiológica (suero) (unidades)", "category": "medicine", "priority": "critic"},
        {"name": "Alcohol al 70% (frascos)", "category": "medicine", "priority": "critic"},
        {"name": "Loratadina (cajas)", "category": "medicine", "priority": "mid"},
        {"name": "Cetirizina (cajas)", "category": "medicine", "priority": "mid"},
        {"name": "Antiinflamatorios (cajas)", "category": "medicine", "priority": "high"},

        {"name": "Losartán (cajas)", "category": "medicine", "priority": "critic"},
        {"name": "Captopril (cajas)", "category": "medicine", "priority": "critic"},
        {"name": "Valsartán (cajas)", "category": "medicine", "priority": "critic"},
        {"name": "Omesartan (cajas)", "category": "medicine", "priority": "critic"},
        {"name": "Enalapril (cajas)", "category": "medicine", "priority": "critic"},
        {"name": "Amlodipina (cajas)", "category": "medicine", "priority": "critic"},
        {"name": "Nifedipina (cajas)", "category": "medicine", "priority": "critic"},
        {"name": "Metformina (cajas)", "category": "medicine", "priority": "critic"},
        {"name": "Levotiroxina (cajas)", "category": "medicine", "priority": "critic"},

        {"name": "Artrodar (cajas)", "category": "medicine", "priority": "low"},
        {"name": "Metilprednisolona (cajas)", "category": "medicine", "priority": "high"},


        # ==========================
        # pediatric_medications
        # ==========================

        {"name": "Acetaminofén (jarabe o gotas) (frascos)", "category": "pediatric_medications", "priority": "high"},
        {"name": "Ibuprofeno (suspensión) (frascos)", "category": "pediatric_medications", "priority": "high"},
        {"name": "Salbutamol (inhalador) (unidades)", "category": "pediatric_medications", "priority": "critic"},
        {"name": "Loratadina/Desloratadina (jarabe) (frascos)", "category": "pediatric_medications", "priority": "mid"},
        {"name": "Amoxicilina/Cefalexina (suspensión) (frascos)", "category": "pediatric_medications", "priority": "high"},
        {"name": "Suero de rehidratación oral (sobres)", "category": "pediatric_medications", "priority": "critic"},


        # ==========================
        # textiles
        # ==========================

        {"name": "Centros de cama (unidades)", "category": "textiles", "priority": "high"},
        {"name": "Cobijas (unidades)", "category": "textiles", "priority": "high"},


        # ==========================
        # for_children
        # ==========================

        {"name": "Pañales (paquetes)", "category": "for_children", "priority": "critic"},
        {"name": "Toallitas húmedas (paquetes)", "category": "for_children", "priority": "high"},
        {"name": "Fórmula para bebés (latas)", "category": "for_children", "priority": "critic"},
        {"name": "Biberones (unidades)", "category": "for_children", "priority": "high"},
        {"name": "Jabón neutro (unidades)", "category": "for_children", "priority": "high"},
        {"name": "Shampoo para niños (frascos)", "category": "for_children", "priority": "mid"},
        {"name": "Crema antipañalitis (tubos)", "category": "for_children", "priority": "high"},


        # ==========================
        # for_rescuers
        # ==========================

        {"name": "Botas de seguridad (pares)", "category": "for_rescuers", "priority": "critic"},
        {"name": "Medias gruesas (pares)", "category": "for_rescuers", "priority": "critic"},
        {"name": "Cascos resistentes (unidades)", "category": "for_rescuers", "priority": "critic"},
        {"name": "Tapabocas KN95 (unidades)", "category": "for_rescuers", "priority": "critic"},
        {"name": "Guantes de trabajo (pares)", "category": "for_rescuers", "priority": "critic"},
        {"name": "Linternas (unidades)", "category": "for_rescuers", "priority": "critic"},
        {"name": "Lentes de seguridad (unidades)", "category": "for_rescuers", "priority": "critic"},
        {"name": "Bebidas hidratantes (unidades)", "category": "for_rescuers", "priority": "critic"},
        {"name": "Alimentos de fácil consumo (unidades)", "category": "for_rescuers", "priority": "critic"},


        # ==========================
        # veterinary_use
        # ==========================

        {"name": "Suero de hidratación (unidades)", "category": "veterinary_use", "priority": "critic"},
        {"name": "Complejos vitamínicos (frascos)", "category": "veterinary_use", "priority": "mid"},
        {"name": "Relajantes musculares (cajas)", "category": "veterinary_use", "priority": "high"},
        {"name": "Comida húmeda y seca (unidades)", "category": "veterinary_use", "priority": "critic"},
        {"name": "Alimento para perros y gatos (seco y húmedo) (unidades)", "category": "veterinary_use", "priority": "critic"},
        {"name": "Cobijas para mascotas (unidades)", "category": "veterinary_use", "priority": "mid"},
        {"name": "Correas o arnés para perros y gatos (unidades)", "category": "veterinary_use", "priority": "high"},
        {"name": "Camitas (unidades)", "category": "veterinary_use", "priority": "low"},
        {"name": "Antibióticos de uso veterinario (cajas)", "category": "veterinary_use", "priority": "critic"},
        {"name": "Analgésicos de uso veterinario (cajas)", "category": "veterinary_use", "priority": "critic"},

    ]

    items = [
        Item(**item) for item in items_data
    ]

    db.add_all(items)
    db.flush()

    print("✅ Items seeded")