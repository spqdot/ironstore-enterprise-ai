from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routers.chat import router

app = FastAPI(
    title="IronStore Enterprise AI Assistant",
    version="1.0"
)

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://localhost:5174",
        "http://localhost:5175",
        "http://localhost:5176",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)