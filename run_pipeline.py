from ingestion.fetch_market_data import fetch_market_data
from transforms.normalize_market_data import normalize_market_data

def main():
    fetch_market_data()
    normalize_market_data()

if __name__ == "__main__":
    main()
