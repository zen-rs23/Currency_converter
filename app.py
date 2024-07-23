import streamlit as st
import frankfurter
import currency

# Title
st.title("FX Converter")

# Amount input
amount = st.number_input("Amount to be converted", min_value=1.0, step=0.01)

# Fetch the available currencies
currencies = frankfurter.get_available_currencies()
currency_list = list(currencies.keys())

# Select boxes for currencies
from_currency = st.selectbox("From Currency", currency_list, index=currency_list.index('USD'))
to_currency = st.selectbox("To Currency", currency_list, index=currency_list.index('EUR'))

# Fetch button
fetch_latest = st.button("Get Latest Rate")

# Text box for display (for latest conversion rate)
if fetch_latest:
    rate, date_from_api = frankfurter.get_latest_rate(from_currency, to_currency)
    st.header("Latest Conversion Rate")
    result_text = currency.format_conversion(date_from_api, from_currency, to_currency, rate, amount)
    st.text(result_text)

# Date input for historical rates
selected_date = st.date_input("Select date")

# Fetch button for historical rate
fetch_historical = st.button("Get Historical Rate")

# Text box for display (for historical conversion rate)
if fetch_historical:
    historical_rate = frankfurter.get_historical_rate(from_currency, to_currency, selected_date)
    st.header("Conversion Rate")
    result_text = currency.format_conversion(selected_date, from_currency, to_currency, historical_rate, amount)
    st.text(result_text)
