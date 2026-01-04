import requests
import logging
from utils.time_utils import current_utc_timestamp, current_utc_date
from utils.file_utils import append_json_line


URL = "https://api.coingecko.com/api/v3/simple/price"
PARAMS = {
    "ids": "bitcoin",
    "vs_currencies": "usd"
}
SOURCE = "coingecko"

logging.basicConfig(level=logging.INFO)

def fetch_market_data():
    try:
        response = requests.get(URL, params=PARAMS, timeout=10)
        response.raise_for_status()
        data = response.json()
        
        timestamp = current_utc_timestamp()
        records = []
        
        for asset, price_info in data.items():
            record = ({
                "asset": asset,
                "price_usd": price_info["usd"],
                "timestamp_utc": timestamp,
                "source": SOURCE
            })
            append_json_line(
                base_path="data/raw",
                date_str=current_utc_date(),
                filename="market_prices.json",
                payload=record
            )
            records.append(record)            
        logging.info("Successfully fetched market data for %s", list(data.keys()))
        return records
    except requests.RequestException as e:
        logging.error("Failed to fetch market data: %s", e)
        return []
    