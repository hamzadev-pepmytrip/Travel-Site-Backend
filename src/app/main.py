from fastapi import FastAPI
from app.database import Base, engine
from app.routers import all_routers
from app.sceduler import start_scheduler
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Or ["*"] for testing only
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)


for router, prefix, tags in all_routers:
    app.include_router(router, prefix=prefix, tags=tags)

start_scheduler()