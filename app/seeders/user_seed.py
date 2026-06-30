from app.models.user import User


def seed_users(db):
    print("🌱 Seeding users...")

    users = [
        User(name="Francisco Ces", username="francisco_ces", role="director", center_id=1, password_hash="$2b$12$qZxT3P4tUQj34KOJFzqXaeieBy2ddAZwxVZnKaSJq5Qw4YyQjm6OG"),
        User(name="Gregman Rodríguez", username="gregman_rodriguez", role="director", center_id=3, password_hash="$2b$12$qZxT3P4tUQj34KOJFzqXaeieBy2ddAZwxVZnKaSJq5Qw4YyQjm6OG"),

        
        User(name="Javier Bermúdez", username="javierbermudez", role="volunteer", center_id=1, password_hash="$2b$12$qZxT3P4tUQj34KOJFzqXaeieBy2ddAZwxVZnKaSJq5Qw4YyQjm6OG"),
        User(name="Dino Pronio", username="dino_pronio", role="volunteer", center_id=2, password_hash="$2b$12$qZxT3P4tUQj34KOJFzqXaeieBy2ddAZwxVZnKaSJq5Qw4YyQjm6OG"),
        User(name="Génova Castillo", username="genova_castillo", role="volunteer", center_id=3, password_hash="$2b$12$qZxT3P4tUQj34KOJFzqXaeieBy2ddAZwxVZnKaSJq5Qw4YyQjm6OG"),
    ]

    db.add_all(users)
    db.flush()

    print("✅ Users seeded")