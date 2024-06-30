import uvicorn
from fastapi import FastAPI, APIRouter

from public.handlers import memes_router

app = FastAPI()
main_api_router = APIRouter()

main_api_router.include_router(memes_router)
app.include_router(main_api_router)

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True, host="0.0.0.0", port=8000)