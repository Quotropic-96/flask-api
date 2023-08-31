# @desc Get all currencies at work
def get_available_currencies(rates):
  rate_set = set()
  for rate in rates:
    rate_set.add(rate["from"])
    rate_set.add(rate["to"])
  return rate_set

# @desc Get missing conversion rates
def get_missing_rates(currencies, rates):
  known_rates = {}  # Dictionary to store known conversion rates

  # Populate known conversion rates from the provided rates
  for rate in rates:
    from_currency, to_currency, rate_value = rate["from"], rate["to"], float(rate["rate"])
    known_rates[(from_currency, to_currency)] = rate_value

  all_rates = []  # List to store all the conversion rates

  for from_currency in currencies:
    for to_currency in currencies:
      # Skip the case when converting to the same currency
      if from_currency == to_currency: continue

      else:
        # Check if the direct conversion rate is known
        direct_rate = known_rates.get((from_currency, to_currency))

        if direct_rate is not None:
          all_rates.append({"from": from_currency, "to": to_currency, "rate": str(round(direct_rate, 3))})
        
        else:
          # Compute conversion through EUR
          rate_1 = known_rates.get((from_currency, "EUR"))
          rate_2 = known_rates.get(("EUR", to_currency))

          if rate_1 is not None and rate_2 is not None:
            conversion_rate = rate_1 * rate_2
            all_rates.append({"from": from_currency, "to": to_currency, "rate": str(round(conversion_rate, 3))})
          else:
            print(f'WARNING: Missing conversion rate from {from_currency} to {to_currency}')

  return all_rates