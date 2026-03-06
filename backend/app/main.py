from fastapi import FastAPI
from .api import member_router
# Existing app creation and middleware setup are assumed above
app = FastAPI()
# Include other routers here
app.include_router(member_router)
