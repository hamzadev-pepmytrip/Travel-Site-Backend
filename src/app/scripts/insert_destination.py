from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models import (
    Region,
    Destination,
    DestinationImage,
    VisaType,
    PackageCategory,
    Package,
    PackageImage,
)

# Sample data
DESTINATIONS = [
    {
        "region_name": "Asia",
        "country_name": "Japan",
        "city": "Tokyo",
        "slug": "tokyo-japan",
        "description": "A bustling city with culture and technology.",
        "airport": "Narita International Airport",
        "airport_code": "NRT",
        "image_url": "https://example.com/images/tokyo.jpg",
        "destination_images": [
            "https://example.com/images/tokyo1.jpg",
            "https://example.com/images/tokyo2.jpg",
        ],
        "visa_types": [
            {
                "visa_format": "Tourist Visa",
                "description": "Allows entry for tourism purposes up to 30 days.",
                "requirements": "Passport, flight ticket, hotel booking",
                "processing_time": "5 business days",
                "service_fee": "$50",
            },
            {
                "visa_format": "Business Visa",
                "description": "For business meetings or conferences.",
                "requirements": "Invitation letter, proof of employment",
                "processing_time": "7 business days",
                "service_fee": "$75",
            },
        ],
        "package_category": {"name": "City Tours", "slug": "city-tours"},
        "package": {
            "title": "Explore Tokyo in 5 Days",
            "slug": "explore-tokyo",
            "description": "Discover the heart of Japan with this immersive 5-day package.",
            "price": 999.99,
            "duration_days": 5,
            "featured": True,
            "rating": 4.8,
            "is_active": True,
            "on_deal": False,
            "image_url": "https://example.com/images/tokyo-package.jpg",
            "package_images": [
                "https://example.com/images/tokyo-pkg1.jpg",
                "https://example.com/images/tokyo-pkg2.jpg",
            ],
        },
    }
]


def insert_data():
    db: Session = SessionLocal()
    try:
        for data in DESTINATIONS:
            region = db.query(Region).filter_by(name=data["region_name"]).first()
            if not region:
                print(f"Region {data['region_name']} not found. Skipping.")
                continue

            # Create Destination
            destination = Destination(
                region_id=region.id,
                country_name=data["country_name"],
                city=data["city"],
                slug=data["slug"],
                description=data["description"],
                airport=data["airport"],
                airport_code=data["airport_code"],
                image_url=data["image_url"],
            )
            db.add(destination)
            db.flush()

            # Destination Images
            for img_url in data["destination_images"]:
                dest_img = DestinationImage(
                    destination_id=destination.id, image_url=img_url
                )
                db.add(dest_img)

            # Visa Types
            for visa in data["visa_types"]:
                visa_type = VisaType(
                    destination_id=destination.id,
                    visa_format=visa["visa_format"],
                    description=visa["description"],
                    requirements=visa["requirements"],
                    processing_time=visa["processing_time"],
                    service_fee=visa["service_fee"]
                )
                db.add(visa_type)

            # Package Category (create or get existing)
            category_data = data["package_category"]
            category = (
                db.query(PackageCategory).filter_by(slug=category_data["slug"]).first()
            )
            if not category:
                category = PackageCategory(
                    name=category_data["name"], slug=category_data["slug"]
                )
                db.add(category)
                db.flush()

            # Package
            pkg_data = data["package"]
            package = Package(
                title=pkg_data["title"],
                slug=pkg_data["slug"],
                description=pkg_data["description"],
                price=pkg_data["price"],
                duration_days=pkg_data["duration_days"],
                destination_id=destination.id,
                category_id=category.id,
                featured=pkg_data["featured"],
                rating=pkg_data["rating"],
                is_active=pkg_data["is_active"],
                on_deal=pkg_data["on_deal"],
                image_url=pkg_data["image_url"],
            )
            db.add(package)
            db.flush()

            # Package Images
            for img_url in pkg_data["package_images"]:
                pkg_img = PackageImage(package_id=package.id, image_url=img_url)
                db.add(pkg_img)

        db.commit()
        print("✅ Data inserted successfully!")

    except Exception as e:
        db.rollback()
        print("❌ Error inserting data:", e)

    finally:
        db.close()


if __name__ == "__main__":
    insert_data()
