from fastapi import FastAPI
from fastapi.security import HTTPBearer
from fastapi.middleware.cors import CORSMiddleware

from app.database import engine
from app.models import skill
from app.routers.skill import router as skill_router

# サーバー起動時にテーブルを作成
skill.Base.metadata.create_all(bind=engine)

app = FastAPI()
security = HTTPBearer(auto_error=False)
app.include_router(skill_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/hello")
def get_hello():
    return "hello"