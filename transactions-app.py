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

#  @desc    Gets a currency rate by currency codes
#  @route   GET /currency-rate/<from_currency>/<to_currency>
#  @access  Public
@app.get('/currency-rate/<from_currency>/<to_currency>')
def get_currency_rate_by_currency_codes(from_currency, to_currency):
  available_currencies = get_available_currencies(currency_rates)
  all_rates = get_missing_rates(available_currencies, currency_rates)
  filtered_rates = list(filter(lambda rate: rate["from"] == from_currency and rate["to"] == to_currency, all_rates))
  if len(filtered_rates) != 0:
    return filtered_rates[0]
  else:
    return [{"message": f'No rate found from {from_currency} to {to_currency}'}]


#  @desc    Gets a transaction by sku & currency
#  @route   GET /transactions/<currency>/<sku>
#  @access  Public
@app.get('/transactions/<currency>/<sku>')
def get_transaction_by_currency_and_sku(currency, sku):
  filtered_transactions = list(filter(lambda transaction: transaction["currency"] == currency and transaction["sku"] == sku, transactions))
  if len(filtered_transactions) != 0:
    return filtered_transactions
  else:
    return [{"message": f'No transactions found with currency {currency} and sku {sku}'}]

#  @desc    Gets all the transactions with a given currency
#  @route   GET /transactions/<currency>
#  @access  Public
@app.get('/transactions/<currency>')
def get_all_transactions_by_currency(currency):
  filtered_transactions = list(filter(lambda transaction: transaction["currency"] == currency, transactions))
  if len(filtered_transactions) != 0:
    return filtered_transactions
  else:
    return [{"message": f'No transactions found with currency {currency}'}]

app.run()