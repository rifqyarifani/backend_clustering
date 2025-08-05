from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd

app = FastAPI()

# CORS settings to allow frontend access (e.g., Next.js on localhost:3000)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, use specific origin(s)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/data")
def read_excel():
    df = pd.read_excel("data.xlsx")
    return {"data": df.to_dict(orient="records")}
