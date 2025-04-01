from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.evaluation import router

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routes
app.include_router(router)

@app.get("/")
async def root():
    return {"message": "Welcome to the Pronunciation Evaluation API"}
