from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Configure CORS to avoid CORS issue
app.add_middleware(
    CORSMiddleware, 
    allow_origins = ["http://localhost:3000"], 
    allow_methods = ["*"], 
    allow_headers = ["*"]
)

@app.get("/")
def homePage(): 
    return {"message": "Welcome to the home page for testing of testing"}