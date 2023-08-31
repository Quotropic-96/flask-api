from flask import Flask
from utils.rates import *

app = Flask(__name__)

# Data
transactions = [
  { "sku": "T2006", "amount": "10.00", "currency": "USD" },
  { "sku": "M2007", "amount": "34.57", "currency": "CAD" },
  { "sku": "R2008", "amount": "17.95", "currency": "USD" },
  { "sku": "T2006", "amount": "7.63", "currency": "EUR" },
  { "sku": "B2009", "amount": "21.23", "currency": "USD" }
]

currency_rates = [
  { "from": "EUR", "to": "USD", "rate": "1.359" },
  { "from": "CAD", "to": "EUR", "rate": "0.732" },
  { "from": "USD", "to": "EUR", "rate": "0.736" },
  { "from": "EUR", "to": "CAD", "rate": "1.366" }
]

#  @desc    Gets all the currency rates
#  @route   GET /all-currency-rates
#  @access  Public
@app.get('/all-currency-rates')
def get_all_currency_rates():
  available_currencies = get_available_currencies(currency_rates)
  return {"Currency rates":get_missing_rates(available_currencies, currency_rates)}
