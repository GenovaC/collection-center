from app.models.center import Center


def seed_centers(db):
    print("🌱 Seeding centers...")

    centers = [
        Center(name="Eje Norte: Núcleo Ciudad Bolívar"),
        Center(name="Eje Central: Núcleo Ciudad Guayana"),
        Center(name="Eje Sur: Centro Académico Regional Upata"),
    ]

    db.add_all(centers)
    db.flush()

    print("✅ Centers seeded")