from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.responses import FileResponse
import redis

app = FastAPI()

r = redis.Redis(host='localhost', port=6379, db=0)


@app.get("/")
def read_root():
    return {"message": "Приложение работает!"}

@app.get("/click/{user_id}")
async def click(user_id: int):
    clicks = r.incr(f"user:{user_id}:clicks")
    print(f"User {user_id} clicked. Total clicks: {clicks}")  # Логируем результат
    return JSONResponse({"clicks": clicks})


@app.get("/get_clicks/{user_id}")
async def get_clicks(user_id: int):
    clicks = int(r.get(f"user:{user_id}:clicks") or 0)
    return JSONResponse({"clicks": clicks})

