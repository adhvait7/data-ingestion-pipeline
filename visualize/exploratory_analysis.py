import json
from datetime import datetime
from zoneinfo import ZoneInfo
import matplotlib.pyplot as plt

FILEPATH = "data/raw_prices.json"

timestamps = []
prices = []

with open(FILEPATH, "r") as f:
    for line in f:
        record = json.loads(line)

        # convert UTC -> IST for display
        utc_time = datetime.fromisoformat(record["timestamp_utc"])
        ist_time = utc_time.astimezone(ZoneInfo("Asia/Kolkata"))

        timestamps.append(ist_time)
        prices.append(record["prices"]["bitcoin"]["usd"])

# sort by time (important)
data = sorted(zip(timestamps, prices))
timestamps, prices = zip(*data)

plt.figure(figsize=(10, 5))
plt.plot(timestamps, prices, marker="o")

plt.title("Bitcoin Price Over Time (USD)")
plt.xlabel("Time (IST)")
plt.ylabel("Price (USD)")

plt.grid(True)
plt.tight_layout()
plt.show()
