from fastapi import FastAPI
from .routers import bill

app = FastAPI()
app.include_router(bill.APIRouter)