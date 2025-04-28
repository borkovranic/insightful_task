from utils.logger import logger

from playwright.sync_api import Page, expect


class Xe:
    URL = "https://www.xe.com/"

    FROM__TO_CURRENCIES_TYPE_NAME = "Type to search..."

    LOCATOR_FROM_CURRENCY = "#midmarketFromCurrency"
    LOCATOR_FROM_CURRENCY_DROPDOWN = "#midmarketFromCurrency-listbox"

    TARGET_CURRENCY_LOCATOR = "#midmarketToCurrency"
    LOCATOR_TO_CURRENCY_DROPDOWN = "#midmarketToCurrency-listbox"

    CONVERSION = "div[data-testid='conversion'][class*='grid-area:conversion']"

    def __init__(self, page: Page):
        self.page = page
        self.currency_element = None
        self.first_conversion = True
        self.conversion_rates = []
        self.conversion_results = []

    def open_exchange(self):
        logger.info(f"Navigating to {self.URL}...")
        self.page.goto(self.URL)
        self.first_conversion = True
        self.page.wait_for_load_state('domcontentloaded')

    def input_amount(self, amount):
        amount_textbox = self.page.get_by_role("textbox", name="Amount")
        amount_textbox.clear()
        amount_textbox.fill(amount)

        parent_element = amount_textbox.locator("..").locator("..")  # Koristimo ".." da uzmemo parent element

        if self.first_conversion is False:
            loading_indicator = parent_element.locator("svg[xmlns='http://www.w3.org/2000/svg']")
            try:
                loading_indicator.wait_for(state='visible')
                loading_indicator.wait_for(state='detached')
            except TimeoutError:
                logger.warning("Loading indicator nije nestao u očekivanom vremenskom okviru.")

    def click_currency_element_and_input_name(self, side, currency_name):
        currency_element = self.page.locator(f"#midmarket{side}Currency")
        currency_element.click()
        currency_input = currency_element.get_by_role("combobox", name="Type to search...")
        currency_input.fill(currency_name[:3])

    def select_currency_in_dropdown(self, side, currency_name):
        dropdown = self.page.locator(f"#midmarket{side}Currency-listbox")
        dropdown.get_by_role("option", name=currency_name[:3]).first.click()

    def verify_currency_element_value(self, side, currency_name):
        currency_element = self.page.locator(f"#midmarket{side}Currency")
        expect(currency_element).to_have_text(currency_name)

    def set_currency_element_value(self, currency_name, side):
        logger.info(f"Setting currency field '{side}' to {currency_name}...")
        self.click_currency_element_and_input_name(side, currency_name)
        self.select_currency_in_dropdown(side, currency_name)
        self.verify_currency_element_value(side, currency_name)

    def set_from(self, currency_name="RSD - Serbian Dinar"):
        self.set_currency_element_value(currency_name, side="From")

    def set_to(self, currency_name):
        self.set_currency_element_value(currency_name, side="To")

    def click_convert_button(self):
        self.page.get_by_role("button", name="Convert").click()

    def get_conversion_value(self):
        con = self.page.locator(self.CONVERSION)
        from_amount_and_currency = con.locator("p").first.text_content().lstrip().rstrip()
        to_amount_and_currency = con.locator("p").nth(1).text_content().lstrip().rstrip()
        result_of_conversion = f"{from_amount_and_currency}{to_amount_and_currency}"
        logger.info(f"Result of conversion:\n{from_amount_and_currency} {to_amount_and_currency}")
        return result_of_conversion

    def get_conversion_rate(self):
        conversion_rate = self.page.locator(self.CONVERSION).locator("div").locator("div").locator(
            "p").first.text_content().strip()
        if conversion_rate not in self.conversion_rates:
            self.conversion_rates.append(conversion_rate)

    def convert_currency(self, amount):
        self.input_amount(amount)
        if self.first_conversion is True:
            self.click_convert_button()
            self.first_conversion = False
        # time.sleep(2)

    def convert_multiple_amounts(self, amounts_list: list):
        for amount in amounts_list:
            self.convert_currency(amount)
            self.conversion_results.append(self.get_conversion_value())
        self.get_conversion_rate()

    def convert_multiple_amounts_and_currencies(self, amounts_list: list, currency_list: list):
        for currency in currency_list:
            self.set_to(currency)
            self.convert_multiple_amounts(amounts_list)
