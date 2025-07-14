from fastapi import FastAPI
from app.database import Base, engine
from app.routers import all_routers

app = FastAPI()


Base.metadata.create_all(bind=engine)


for router, prefix, tags in all_routers:
    app.include_router(router, prefix=prefix, tags=tags)