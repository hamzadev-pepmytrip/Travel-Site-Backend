from fastapi import FastAPI
from app.database import Base, engine
from app.routers import destination_router
from app.routers import package_category_router
from app.routers import packages_router

app = FastAPI()


Base.metadata.create_all(bind=engine)


app.include_router(destination_router.router, prefix="/destinations", tags=["Destinations"])
app.include_router(package_category_router.router, prefix="/package-categories", tags=["Package Categories"])
app.include_router(packages_router.router, prefix="/packages", tags=["Packages"])
