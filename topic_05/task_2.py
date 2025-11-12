import requests

############ Отримання курсу валюти з API НБУ #############
def get_rate(currency):
    url = f"https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?valcode={currency}&json"
    response = requests.get(url)
    file = response.json()
    return file[0]['rate']

############ Основа конвертатора #############
def main():
    print("Конвертер валют (USD, EUR, PLN → UAH)")
    currency = input("Введіть валюту (USD, EUR або PLN): ").upper()
    amount = float(input("Введіть суму: "))

    if currency not in ["USD", "EUR", "PLN"]:
        print("Невірна валюта! Спробуйте ще раз.")
        return

    rate = get_rate(currency)
    result = amount * rate

    print(f"1 {currency} = {rate:.2f} грн")
    print(f"{amount:.2f} {currency} = {result:.2f} грн")

############### Запуск ###############
if __name__ == "__main__":
    main()