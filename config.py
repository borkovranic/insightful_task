from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent

RESULTS = PROJECT_ROOT / 'Results'

WEB_RESULTS = PROJECT_ROOT / RESULTS / 'web_results.txt'
CONVERSION_RATES = PROJECT_ROOT / RESULTS / 'conversion_rates.txt'

default_from_currency_id = "rsd"

target_currency_ids = ["usd", "eur"]

amounts = ["1000", "2000", "3000"]

currencies = {
    "rsd": "RSD - Serbian Dinar",
    "usd": "USD - US Dollar",
    "eur": "EUR - Euro"
}

