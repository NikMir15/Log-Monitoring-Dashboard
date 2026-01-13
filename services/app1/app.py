import json
import os
import random
import time
from datetime import datetime, timezone

SERVICE = os.getenv("SERVICE_NAME", "app1")

LEVELS = ["INFO", "WARN", "ERROR"]
MESSAGES = [
    "User login successful",
    "Payment processed",
    "Order created",
    "Cache miss",
    "DB connection retry",
    "Timeout calling upstream service",
    "Validation failed",
    "Rate limit exceeded",
]

def log(level: str, message: str):
    event = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "service": SERVICE,
        "level": level,
        "message": message,
        "request_id": f"req-{random.randint(1000, 9999)}",
    }
    print(json.dumps(event), flush=True)

if __name__ == "__main__":
    while True:
        level = random.choices(LEVELS, weights=[70, 20, 10])[0]
        msg = random.choice(MESSAGES)
        log(level, msg)
        time.sleep(random.uniform(0.2, 1.0))
