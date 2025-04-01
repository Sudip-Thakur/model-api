from fastapi import APIRouter, File, UploadFile, Form
from services.english_evaluation import evaluate_english_pronunciation
from services.nepali_evaluation import evaluate_nepali_pronunciation

router = APIRouter()

@router.post("/evaluate/english/")
async def evaluate_english(audio: UploadFile = File(...), text: str = Form(...)):
    return await evaluate_english_pronunciation(audio, text)

@router.post("/evaluate/nepali/")
async def evaluate_nepali(audio: UploadFile = File(...), text: str = Form(...)):
    return await evaluate_nepali_pronunciation(audio, text)
