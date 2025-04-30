from Applications.Calculator.calculator_windows import Calculator
from utils.file_handling_utils import write_lines_to_txt, read_lines_from_txt, get_conversion_rate, \
    parse_conversion_rates, format_conversion_rates, format_conversion_result, compare_files
from Applications.Exchange.xe import Xe

from config import WEB_RESULTS, CONVERSION_RATES, currencies, \
    target_currency_ids, amounts, CALCULATOR_RESULTS
from utils.logger import logger
from utils.app_utils import get_calculator, close_multiple_calculator_windows

TARGET_CURRENCIES_NAMES = [currencies.get(currency_id) for currency_id in target_currency_ids]


def test_validate_conversion_from_rsd_to_target_currencies_accurate(page):
    try:
        xe = Xe(page)
        xe.open_exchange()
        xe.set_from(currencies.get('rsd'))
        xe.convert_multiple_amounts_and_currencies(amounts, TARGET_CURRENCIES_NAMES)

        write_lines_to_txt(WEB_RESULTS, xe.conversion_results)
        write_lines_to_txt(CONVERSION_RATES, xe.conversion_rates)

        format_conversion_rates(WEB_RESULTS, WEB_RESULTS)

        conversion_rates = parse_conversion_rates(CONVERSION_RATES)

        calculator = Calculator()

        calculator_results = []
        for currency in target_currency_ids:
            currency_conversion_rate = get_conversion_rate(conversion_rates, 'RSD', currency)
            for amount in amounts:
                calculator.multiply_numbers(amount, currency_conversion_rate)
                result = calculator.get_calculator_results()
                formatted_result = format_conversion_result(amount, result, currency)
                calculator_results.append(formatted_result)

        write_lines_to_txt(CALCULATOR_RESULTS, calculator_results)

        calculator.close_calculator()

        compare_files(WEB_RESULTS, CALCULATOR_RESULTS)

    except Exception as e:
        logger.error(f"Test failed with error: {e}")
        close_multiple_calculator_windows()
        raise
