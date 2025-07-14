from . import (
    destination_router,
    package_category_router,
    packages_router,
    destination_image_router,
    
)

all_routers = [
    (destination_router.router, "/destinations", ["Destinations"]),
    (package_category_router.router, "/package-categories", ["Package Categories"]),
    (packages_router.router, "/packages", ["Packages"]),
    (destination_image_router.router, "/destination-images", ["Destination Images"]),
]