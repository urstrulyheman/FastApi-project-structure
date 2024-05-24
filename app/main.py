from fastapi import FastAPI
from app.api.endpoints import user, item
from app.db import init_db


app = FastAPI()

# Initialize the database
init_db()

# Include the user and item routes
app.include_router(user.router, prefix="/users", tags=["users"])
app.include_router(item.router, prefix="/items", tags=["items"])
