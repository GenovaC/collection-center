from app.models.item import Item


def seed_items(db):
    print("🌱 Seeding items...")

    items_data = [

        # ==========================
        # medical_supplies
        # ==========================

        {"name": "Vendas elásticas", "category": "medical_supplies", "priority": "high"},
        {"name": "Gasas", "category": "medical_supplies", "priority": "high"},
        {"name": "Algodón", "category": "medical_supplies", "priority": "mid"},
        {"name": "Guantes desechables", "category": "medical_supplies", "priority": "critic"},
        {"name": "Jeringas con agujas", "category": "medical_supplies", "priority": "high"},
        {"name": "Tensiómetros", "category": "medical_supplies", "priority": "mid"},
        {"name": "Oxímetros", "category": "medical_supplies", "priority": "high"},
        {"name": "Kits de primeros auxilios", "category": "medical_supplies", "priority": "critic"},
        {"name": "Pañales para adultos", "category": "medical_supplies", "priority": "mid"},


        # ==========================
        # medicine
        # ==========================

        {"name": "Acetaminofén", "category": "medicine", "priority": "high"},
        {"name": "Ibuprofeno", "category": "medicine", "priority": "high"},
        {"name": "Paracetamol", "category": "medicine", "priority": "high"},
        {"name": "Amoxicilina", "category": "medicine", "priority": "high"},
        {"name": "Ciprofloxacina", "category": "medicine", "priority": "high"},
        {"name": "Solución fisiológica (suero)", "category": "medicine", "priority": "critic"},
        {"name": "Alcohol al 70%", "category": "medicine", "priority": "critic"},
        {"name": "Loratadina", "category": "medicine", "priority": "mid"},
        {"name": "Cetirizina", "category": "medicine", "priority": "mid"},
        {"name": "Antiinflamatorios", "category": "medicine", "priority": "high"},

        {"name": "Losartán", "category": "medicine", "priority": "critic"},
        {"name": "Captopril", "category": "medicine", "priority": "critic"},
        {"name": "Valsartán", "category": "medicine", "priority": "critic"},
        {"name": "Omesartan", "category": "medicine", "priority": "critic"},
        {"name": "Enalapril", "category": "medicine", "priority": "critic"},
        {"name": "Amlodipina", "category": "medicine", "priority": "critic"},
        {"name": "Nifedipina", "category": "medicine", "priority": "critic"},
        {"name": "Metformina", "category": "medicine", "priority": "critic"},
        {"name": "Levotiroxina", "category": "medicine", "priority": "critic"},

        {"name": "Artrodar", "category": "medicine", "priority": "low"},
        {"name": "Metilprednisolona", "category": "medicine", "priority": "high"},


        # ==========================
        # pediatric_medications
        # ==========================

        {"name": "Acetaminofén (jarabe o gotas)", "category": "pediatric_medications", "priority": "high"},
        {"name": "Ibuprofeno (suspensión)", "category": "pediatric_medications", "priority": "high"},
        {"name": "Salbutamol (inhalador)", "category": "pediatric_medications", "priority": "critic"},
        {"name": "Loratadina/Desloratadina (jarabe)", "category": "pediatric_medications", "priority": "mid"},
        {"name": "Amoxicilina/Cefalexina (suspensión)", "category": "pediatric_medications", "priority": "high"},
        {"name": "Suero de rehidratación oral", "category": "pediatric_medications", "priority": "critic"},


        # ==========================
        # textiles
        # ==========================

        {"name": "Centros de cama", "category": "textiles", "priority": "high"},
        {"name": "Cobijas", "category": "textiles", "priority": "high"},


        # ==========================
        # for_children
        # ==========================

        {"name": "Pañales", "category": "for_children", "priority": "critic"},
        {"name": "Toallitas húmedas", "category": "for_children", "priority": "high"},
        {"name": "Fórmula para bebés", "category": "for_children", "priority": "critic"},
        {"name": "Biberones", "category": "for_children", "priority": "high"},
        {"name": "Jabón neutro", "category": "for_children", "priority": "high"},
        {"name": "Shampoo para niños", "category": "for_children", "priority": "mid"},
        {"name": "Crema antipañalitis", "category": "for_children", "priority": "high"},


        # ==========================
        # for_rescuers
        # ==========================

        {"name": "Botas de seguridad", "category": "for_rescuers", "priority": "critic"},
        {"name": "Medias gruesas", "category": "for_rescuers", "priority": "critic"},
        {"name": "Cascos resistentes", "category": "for_rescuers", "priority": "critic"},
        {"name": "Tapabocas KN95", "category": "for_rescuers", "priority": "critic"},
        {"name": "Guantes", "category": "for_rescuers", "priority": "critic"},
        {"name": "Linternas", "category": "for_rescuers", "priority": "critic"},
        {"name": "Lentes de seguridad", "category": "for_rescuers", "priority": "critic"},
        {"name": "Bebidas hidratantes", "category": "for_rescuers", "priority": "critic"},
        {"name": "Alimentos de fácil consumo", "category": "for_rescuers", "priority": "critic"},


        # ==========================
        # veterinary_use
        # ==========================

        {"name": "Suero de hidratación", "category": "veterinary_use", "priority": "critic"},
        {"name": "Complejos vitamínicos", "category": "veterinary_use", "priority": "mid"},
        {"name": "Relajantes musculares", "category": "veterinary_use", "priority": "high"},
        {"name": "Comida húmeda y seca", "category": "veterinary_use", "priority": "critic"},
        {"name": "Alimento para perros y gatos (seco y húmedo)", "category": "veterinary_use", "priority": "critic"},
        {"name": "Cobijas para mascotas", "category": "veterinary_use", "priority": "mid"},
        {"name": "Correas o arnés para perros y gatos", "category": "veterinary_use", "priority": "high"},
        {"name": "Camitas", "category": "veterinary_use", "priority": "low"},
        {"name": "Antibióticos de uso veterinario", "category": "veterinary_use", "priority": "critic"},
        {"name": "Analgésicos de uso veterinario", "category": "veterinary_use", "priority": "critic"},

        ]

    items = [
        Item(**item) for item in items_data
    ]

    db.add_all(items)
    db.flush()

    print("✅ Items seeded")