import json
import time
import random
import datetime

service = "app2"
levels = ["INFO", "WARN", "ERROR"]
messages = [
    "Order created",
    "Order updated",
    "Inventory checked",
    "External API call",
    "Timeout talking to downstream service",
    "Validation failed",
    "Unknown exception occurred",
]

while True:
    level = random.choices(levels, weights=[65, 25, 10])[0]
    log = {
        "timestamp": datetime.datetime.utcnow().isoformat() + "Z",
        "service": service,
        "level": level,
        "message": random.choice(messages),
    }
    print(json.dumps(log), flush=True)
    time.sleep(random.uniform(0.2, 1.2))
