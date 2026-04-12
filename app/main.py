from fastapi import FastAPI
from app.database import Base, engine
from app.routers import auth

#Import model so SQLAlchemy knows it
from app.models.user import User

app = FastAPI()

# This will create tables later
Base.metadata.create_all(bind=engine)
app.include_router(auth.router) 


@app.get("/")
def root():
    return {"message": "API is working"}