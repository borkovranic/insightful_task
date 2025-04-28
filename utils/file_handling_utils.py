import json
from pathlib import Path


def get_currency_mapping():
    currency_mapping_json_path = Path(__file__).parent.parent / "configs" / "currencies.json"
    with open(currency_mapping_json_path,'r') as f:
        currency_mapping = json.load(f)

    return currency_mapping


def write_lines_to_txt(file_path, file_name):
    file_path.parent.mkdir(parents=True, exist_ok=True)
    with open(file_path, 'w', encoding="utf-8") as f:
        for line in file_name:
            f.write(line + "\n")


def read_lines_from_txt(file_path):
    with open(file_path, encoding="utf-8") as f:
        lines = [line.strip() for line in f]
    return lines



def parse_conversion_rates(lines: list) -> dict:
    rates = {}
    for line in lines:
        # Primer linije: "1 RSD = 0.0085 EUR"
        parts = line.split()
        if len(parts) == 5:
            from_currency = parts[1]
            to_currency = parts[4]
            rate = float(parts[3])
            rates[(from_currency, to_currency)] = rate
    return rates

def parse_web_results(lines: list) -> list:
    results = []
    for line in lines:
        # Primer linije: "3,000 Serbian Dinars = 25.58 Euros"
        amount_str, value_str = line.split(' = ')
        amount = float(amount_str.replace(",", "").split()[0])
        value = float(value_str.split()[0].replace(",", ""))
        to_currency = value_str.split()[1]
        results.append((amount, to_currency, value))
    return results