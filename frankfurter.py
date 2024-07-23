import api

def get_available_currencies():
    return api.get(f"{api.BASE_URL}/currencies")

def get_latest_rate(from_currency, to_currency):
    data = api.get(f"{api.BASE_URL}/latest?from={from_currency}&to={to_currency}")
    return data["rates"][to_currency], data["date"]


def get_historical_rate(from_currency, to_currency, date):
    data = api.get(f"{api.BASE_URL}/{date}?from={from_currency}&to={to_currency}")
    return data["rates"][to_currency]
