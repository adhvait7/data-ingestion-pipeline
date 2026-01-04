from datetime import datetime, timezone

def current_utc_timestamp():
    return datetime.now(timezone.utc).isoformat()

def current_utc_date():
    return datetime.now(timezone.utc).date().isoformat()