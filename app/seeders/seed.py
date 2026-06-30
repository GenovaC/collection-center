from app.db.database import SessionLocal

from app.seeders.center_seed import seed_centers
from app.seeders.user_seed import seed_users
from app.seeders.item_seed import seed_items


def run_seeds():
    db = SessionLocal()

    try:
        print("🚀 Starting seeding process...")

       # seed_centers(db)
        seed_users(db)
       # seed_items(db)

        db.commit()

        print("✅ Seeding completed successfully")

    except Exception as e:
        db.rollback()
        print("❌ Error during seeding:", str(e))

    finally:
        db.close()


if __name__ == "__main__":
    run_seeds()