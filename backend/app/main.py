from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from datetime import datetime
import random

app = FastAPI(title="LTB+ Trading Bot", version="1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Signal(BaseModel):
    timestamp: str
    pair: str
    signal: str
    confidence: int
    expiration: int
    price: float

@app.get("/")
def home():
    return {
        "message": "🚀 LTB+ Trading Bot Backend is Running!",
        "status": "active"
    }

@app.get("/signal/{pair}")
async def get_signal(pair: str):
    # ডামি সিগনাল (পরে রিয়েল ইন্ডিকেটর লাগবে)
    direction = random.choice(["BUY", "SELL"])
    confidence = random.randint(82, 97)
    
    price = round(random.uniform(19.80, 19.95), 5) if "MXN" in pair else round(random.uniform(1.085, 1.095), 5)
    
    return Signal(
        timestamp=datetime.now().isoformat(),
        pair=pair.replace("-", "/"),
        signal=direction,
        confidence=confidence,
        expiration=15,
        price=price
    )

@app.get("/signals")
async def get_all_signals():
    return [get_signal(pair) for pair in ["USD-MXN", "EUR-USD", "GBP-USD"]]
