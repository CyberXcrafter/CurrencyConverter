from forex_python.converter import CurrencyRates

def currency_converter(amount, from_currency, to_currency):
    c = CurrencyRates()
    converted_amount = c.convert(from_currency, to_currency, amount)
    return converted_amount

# Example usage:
amount_to_convert = 1  # Change this to the amount you want to convert
from_currency_code = 'USD'  # Change this to the source currency code
to_currency_code = 'INR'  # Change this to the target currency code

converted_amount = currency_converter(amount_to_convert, from_currency_code, to_currency_code)
print(f"{amount_to_convert} {from_currency_code} equals {converted_amount} {to_currency_code}")
