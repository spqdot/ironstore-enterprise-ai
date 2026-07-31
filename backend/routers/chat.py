from fastapi import APIRouter

from models.chat import ChatRequest
from rag import ask_question

router = APIRouter()


@router.post("/chat")
def chat(request: ChatRequest):
    return ask_question(request.question)