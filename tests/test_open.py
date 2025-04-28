import time
import pytest

from utils.file_handling_utils import write_lines_to_txt, read_lines_from_txt
from Applications.Exchange.xe import Xe

from config import WEB_RESULTS, PROJECT_ROOT, CONVERSION_RATES, currencies, default_from_currency_id, \
    target_currency_ids, amounts

TARGET_CURRENCIES_NAMES = [currencies.get(currency_id) for currency_id in target_currency_ids]


def test_open2(page):
    xe = Xe(page)
    xe.open_exchange()
    xe.set_from(currencies.get('rsd'))
    xe.convert_multiple_amounts_and_currencies(amounts, TARGET_CURRENCIES_NAMES)
    write_lines_to_txt(WEB_RESULTS, xe.conversion_results)
    write_lines_to_txt(CONVERSION_RATES, xe.conversion_rates)
