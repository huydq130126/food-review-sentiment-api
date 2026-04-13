from pathlib import Path
from fastapi import FastAPI, HTTPException
from typing import Optional, Any
from pydantic import BaseModel, Field, field_validator
from fastapi.middleware.cors import CORSMiddleware
from model import SentimentClassification


BASE_DIR = Path(__file__).resolve().parent
CONFIG_PATH = BASE_DIR / "config.yaml"
classifier = SentimentClassification(str(CONFIG_PATH))
app = FastAPI(title="Food Review Sentiment API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ErrorInfo(BaseModel):
    code: str
    message: str

class ApiResponse(BaseModel):
    success: bool
    data: Optional[Any] = None
    error: Optional[ErrorInfo] = None

class ReviewRequest(BaseModel):
    text: str = Field(..., min_length=1, max_length=500)
    @field_validator("text")
    def text_must_not_be_blank(cls, v : str) -> str:
        cleaned = v.strip()
        if not cleaned:
            raise ValueError("Text đầu vào không được rỗng")
        return cleaned
    
@app.get("/")
async def root():
    return {
        "message": "API đánh giá cảm xúc review món ăn (1-5 sao)"
    }


@app.get("/health")
async def health():
    return {"status": "OK"}

@app.post("/predict")
async def predict(request: ReviewRequest):
    try:
        #validate input
        if not request.text.strip():
            raise HTTPException(status_code = 400, detail = "Text không được rỗng")
        result = classifier(request.text)
        return{
            "input": request.text,
            "output": result
        }
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code = 500, detail = str(e))
    

