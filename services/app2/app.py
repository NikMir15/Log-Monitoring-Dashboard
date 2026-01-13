import json
import os
import random
import time
from datetime import datetime, timezone

SERVICE = os.getenv("SERVICE_NAME", "app2")

LEVELS = ["INFO", "WARN", "ERROR"]
MESSAGES = [
    "Inventory updated",
    "Message consumed from queue",
    "Job completed",
    "Low disk warning",
    "API returned 500",
    "Service degraded",
    "Circuit breaker open",
    "Upstream dependency unavailable",
]

def log(level: str, message: str):
    event = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "service": SERVICE,
        "level": level,
        "message": message,
        "request_id": f"req-{random.randint(10000, 99999)}",
    }
    print(json.dumps(event), flush=True)

if __name__ == "__main__":
    while True:
        level = random.choices(LEVELS, weights=[65, 25, 10])[0]
        msg = random.choice(MESSAGES)
        log(level, msg)
        time.sleep(random.uniform(0.2, 1.2))
