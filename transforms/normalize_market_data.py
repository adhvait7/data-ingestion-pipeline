import json
import csv
import os

RAW_BASE_PATH = "data/raw"
PROCESSED_PATH = "data/processed/market_prices.csv"

SCHEMA = ["asset", "price_usd", "timestamp_utc", "source"]

def normalize_market_data():
    rows = []
    
    for date_folder in os.listdir(RAW_BASE_PATH):
        date_path = os.path.join(RAW_BASE_PATH, date_folder)
        
        if not os.path.isdir(date_path):
            continue
        raw_file = os.path.join(date_path, "market_prices.json")
        if not os.path.exists(raw_file):
            continue
        
        with open(raw_file, "r") as f:
            for line in f:
                raw_record = json.loads(line)
                
                record = raw_record
                
                if not all(field in record for field in SCHEMA):
                    continue
                
                rows.append([
                    record["asset"],
                    record["price_usd"],
                    record["timestamp_utc"],
                    record["source"]
                ])
                
    os.makedirs(os.path.dirname(PROCESSED_PATH), exist_ok=True)
    
    with open(PROCESSED_PATH, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(SCHEMA)
        writer.writerows(rows)
        
    print(f"Processed {len(rows)} rows into {PROCESSED_PATH}")
    
if __name__=="__main__":
    normalize_market_data()