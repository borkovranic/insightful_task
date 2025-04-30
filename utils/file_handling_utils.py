import json
import re
from pathlib import Path

from config import CURRENCY_CONVERSION_COMPARISON_MAP
from utils.logger import logger


def get_currency_mapping():
    currency_mapping_json_path = Path(__file__).parent.parent / "configs" / "currencies.json"
    with open(currency_mapping_json_path, 'r') as f:
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


def parse_conversion_rates(conversion_rates_file):
    conversion_rates = {}
    with open(conversion_rates_file, 'r') as file:
        for line in file:
            parts = line.split(' = ')
            left = parts[0].strip().split()
            right = parts[1].strip().split()

            from_currency = left[1]
            to_currency = right[1]
            rate = float(right[0])

            key = f"{from_currency}_to_{to_currency}"
            conversion_rates[key] = rate

    return conversion_rates


def get_conversion_rate(conversion_rates, from_currency, to_currency):
    key = f"{from_currency.upper()}_to_{to_currency.upper()}"
    return conversion_rates.get(key)


def format_conversion_rates(input_file, output_file):
    with open(input_file, 'r') as file:
        lines = file.readlines()

    formatted_lines = []
    for line in lines:
        parts = line.split(' = ')
        if len(parts) == 2:
            amount_and_currency = parts[1].strip()
            match = re.match(r"([\d,]+(?:\.\d+)?)\s+([a-zA-Z\s]+)", amount_and_currency)
            if match:
                amount = match.group(1)
                currency = match.group(2).strip()
                formatted_amount = round(float(amount.replace(',', '')), 3)
                formatted_line = f"{parts[0]} = {formatted_amount} {currency}\n"
                formatted_lines.append(formatted_line)
            else:
                formatted_lines.append(line)
        else:
            formatted_lines.append(line)

    with open(output_file, 'w') as file:
        file.writelines(formatted_lines)


def format_conversion_result(amount, result, currency_code):
    full_currency_name = get_full_currency_name(currency_code)
    return f"{float(amount):,.0f} Serbian Dinars = {round(float(result), 3)} {full_currency_name}"


def get_full_currency_name(currency_code):
    full_currency_name = CURRENCY_CONVERSION_COMPARISON_MAP.get(currency_code, currency_code)
    return full_currency_name


def compare_files(file1, file2):
    with open(file1, 'r', encoding='utf-8') as f1, open(file2, 'r', encoding='utf-8') as f2:
        for line1, line2 in zip(f1, f2):
            assert line1 == line2, f"Files differ: {line1} != {line2}"

    logger.info(f"Conversion results are identical in files:\n{Path(file1).name} \nand \n{Path(file2).name}")
