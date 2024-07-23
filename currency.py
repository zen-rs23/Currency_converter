def format_conversion(date, from_currency, to_currency, rate, amount):
    converted_amount = amount * rate
    inverse_rate = 1 / rate
    return (f"The conversion rate on {date} from {from_currency} to {to_currency} was {rate:.4f}. So {amount:.2f} in {from_currency} correspond "
            f"\nto {converted_amount:.2f} in {to_currency}. The inverse rate was {inverse_rate:.4f}.")
