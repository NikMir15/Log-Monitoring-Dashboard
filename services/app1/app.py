import json
import time
import random
import datetime

service = "app1"
levels = ["INFO", "WARN", "ERROR"]
messages = [
    "User login success",
    "User logout",
    "DB query executed",
    "Cache miss",
    "Payment gateway timeout",
    "Invalid token",
    "Rate limit triggered",
]

while True:
    level = random.choices(levels, weights=[70, 20, 10])[0]
    log = {
        "timestamp": datetime.datetime.utcnow().isoformat() + "Z",
        "service": service,
        "level": level,
        "message": random.choice(messages),
    }
    print(json.dumps(log), flush=True)
    time.sleep(random.uniform(0.2, 1.2))
