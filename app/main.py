from fastapi import FastAPI
from app.routes import router

app = FastAPI()

# Подключаем маршруты
app.include_router(router)

@app.get("/")
async def root():
    return {"message": "Welcome to the Search Service!"}
