from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import os
from routes import router
from auth import instant_login
from models import LoginRequest

load_dotenv()

app = FastAPI(title="Magazine Blog Platform API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000", "https://*.netlify.app"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {
        "message": "Magazine Blog Platform API",
        "version": "1.0.0",
        "docs": "/docs"
    }

@app.post("/api/auth/login")
async def login(login_request: LoginRequest):
    user = instant_login(login_request)
    return user

app.include_router(router, prefix="/api")

if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
