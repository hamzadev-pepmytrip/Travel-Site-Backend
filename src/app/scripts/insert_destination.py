from app.database import SessionLocal
from app.models.destination import Destination

def run():
    db = SessionLocal()
    try:
        new_dest = Destination(
            country_name="Maldives",
            region="South Asia",
            slug="maldives"
        )
        db.add(new_dest)
        db.commit()
        db.refresh(new_dest)
        print(f"✅ Inserted destination with ID: {new_dest.id}")
    except Exception as e:
        print(f"❌ Error: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    run()
