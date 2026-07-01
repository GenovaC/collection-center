from app.models.user import User


def seed_users(db):
    print("🌱 Seeding users...")

    users = [

        # Gerentes
        User(name="Francisco Ces", username="francisco_ces", role="director", center_id=3, password_hash="$2b$12$lsLK.oKvIR4cLDSzUpjFreAEN2W5Vq.WowIilCsrig6/lGyH2GFr2"),
        User(name="Gregman Rodríguez", username="gregman_rodriguez", role="director", center_id=2, password_hash="$2b$12$lsLK.oKvIR4cLDSzUpjFreAEN2W5Vq.WowIilCsrig6/lGyH2GFr2"),

        # Ciudad Bolívar
        User(name="Dino Pronio", username="dino_pronio", role="volunteer", center_id=1, password_hash="$2b$12$lsLK.oKvIR4cLDSzUpjFreAEN2W5Vq.WowIilCsrig6/lGyH2GFr2"),

        # Guayana
        User(name="Génova Castillo", username="genova_castillo", role="volunteer", center_id=2, password_hash="$2b$12$lsLK.oKvIR4cLDSzUpjFreAEN2W5Vq.WowIilCsrig6/lGyH2GFr2"),
        User(name="Vanessa Salazar", username="vanessa_salazar", role="volunteer", center_id=2, password_hash="$2b$12$lsLK.oKvIR4cLDSzUpjFreAEN2W5Vq.WowIilCsrig6/lGyH2GFr2"),        

        # Upata
        User(name="Javier Bermúdez", username="javier_bermudez", role="volunteer", center_id=3, password_hash="$2b$12$lsLK.oKvIR4cLDSzUpjFreAEN2W5Vq.WowIilCsrig6/lGyH2GFr2"),
        User(name="Enmanuel Muñoz", username="enmanuel_munoz", role="volunteer", center_id=3, password_hash="$2b$12$lsLK.oKvIR4cLDSzUpjFreAEN2W5Vq.WowIilCsrig6/lGyH2GFr2"),
        User(name="Maryangel Lanz", username="maryangel_lanz", role="volunteer", center_id=3, password_hash="$2b$12$lsLK.oKvIR4cLDSzUpjFreAEN2W5Vq.WowIilCsrig6/lGyH2GFr2"),
    ]

    db.add_all(users)
    db.flush()

    print("✅ Users seeded")