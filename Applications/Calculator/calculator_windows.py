import time
from functools import wraps

from pywinauto import findwindows
from pywinauto.application import Application

from utils.app_utils import get_calculator
from utils.logger import logger


def handle_errors(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"Error in function '{func.__name__}': {e}")
            raise

    return wrapper


class Calculator:

    def __init__(self):
        self.calculator_window = get_calculator()
        self.number_pad = None
        self.multiply_by_button = None
        self.equal_button = None
        self.clear_button = None
        self.calculator_results = None
        self._get_elements()

    def _get_elements(self, retries=5, delay=0.3):
        for attempt in range(retries):
            try:
                self.number_pad = next(
                    el for el in self.calculator_window.descendants() if el.automation_id() == 'NumberPad').children()
                self.multiply_by_button = self.calculator_window.child_window(auto_id="multiplyButton")
                self.equal_button = self.calculator_window.child_window(auto_id='equalButton')
                self.clear_button = self.calculator_window.child_window(auto_id='clearButton')
                self.calculator_results = self.calculator_window.child_window(auto_id='CalculatorResults')

            except Exception as e:
                if attempt == retries - 1:
                    raise RuntimeError(f"Failed to initialize calculator elements: {str(e)}")
                time.sleep(delay)

    @handle_errors
    def click_digit(self, digit: int):
        digit = next(num for num in self.number_pad if num.automation_id() == f"num{digit}Button")
        digit.click()

    @handle_errors
    def click_decimal_point(self):
        decimal_button = self.calculator_window.child_window(auto_id="decimalSeparatorButton")
        decimal_button.click()

    @handle_errors
    def click_multiply_button(self):
        self.multiply_by_button.click()

    @handle_errors
    def click_clear_button(self):
        self.clear_button.click()

    @handle_errors
    def click_equal_button(self):
        self.equal_button.click()

    @handle_errors
    def get_calculator_results(self):
        result = self.calculator_window.child_window(auto_id='CalculatorResults').window_text()
        float_result = float(result.replace("Display is ", ""))
        formatted_result = round(float_result, 3)
        return formatted_result

    def enter_number(self, number):
        logger.info(f"Entering number {number}...")
        if isinstance(number, (int, float)):
            number_str = str(number)
        else:
            number_str = number
        for digit in number_str:
            if digit == '.':
                self.click_decimal_point()
            else:
                self.click_digit(int(digit))

    def close_calculator(self):
        self.calculator_window.close()

    def multiply_numbers(self, first_number, second_number):
        logger.info(f"Multiplying numbers {first_number} x {second_number}...")
        self.click_clear_button()
        self.enter_number(first_number)
        self.click_multiply_button()
        self.enter_number(second_number)
        self.click_equal_button()

    def calculate_multiple_amounts(self, amounts: list, conversion_rate):
        results = []
        for amount in amounts:
            self.multiply_numbers(amount, conversion_rate)
            results.append(self.get_calculator_results())
        return results
