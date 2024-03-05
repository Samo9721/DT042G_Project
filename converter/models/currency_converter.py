import urllib.request
import urllib.error
import json

from converter.exceptions.conversion_exceptions import InvalidCurrencyError, NetworkError

class CurrencyConverter:
    """
    A class for converting currencies using exchange rates fetched from the web.
    """

    API_URL = "https://www.floatrates.com/daily/{}.json"

    def __init__(self):
        """
        Initializes the CurrencyConverter class.
        """

    @staticmethod
    def is_connected(host='https://www.google.com/', timeout=1):
        """
        Check if the device is connected to the internet.

        :param  host: A reliable host to test internet connectivity.
        :param timeout: Timeout for the connection attempt.
        :return: True if connected, False otherwise.
        """
        try:
            urllib.request.urlopen(host, timeout=timeout)
            return True
        except urllib.error.URLError:
            return False

    @staticmethod
    def get_exchange_rate(from_currency, to_currency):
        """
        Fetches the exchange rate for the given "from" and "to" currencies.

        :param from_currency: The currency to convert from.
        :param to_currency: The currency to convert to.
        :return: The exchange rate as float.
        """
        if not CurrencyConverter.is_connected():
            raise NetworkError()

        try:
            with urllib.request.urlopen(CurrencyConverter.API_URL.format(from_currency.lower())) as response:
                from_data = json.loads(response.read().decode('utf-8'))

            if from_currency.upper() == to_currency.upper():
                return 1  # Same currency conversion
            else:
                from_to_rate = from_data.get(to_currency.lower(), {}).get('rate')
                if from_to_rate:
                    return from_to_rate
                else:
                    raise InvalidCurrencyError(f"Exchange rate not found for {from_currency} to {to_currency}.")
        except urllib.error.URLError as e:
            raise NetworkError(f"Error fetching data: {e}")

    def convert(self, from_currency, to_currency, amount):
        """
        Converts the given amount from one currency to another.

        :param from_currency: The currency to convert from.
        :param to_currency: The currency to convert to.
        :param amount: The amount to be converted.
        :return: The converted amount in the target currency.
        """
        rate = self.get_exchange_rate(from_currency, to_currency)
        return rate * amount
