import requests

############ Підключення API НБУ #############
response = requests.get("https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json")

def rates():
    for elem in response.json():
        if (elem["cc"] == "USD" or elem["cc"] == "EUR" or elem["cc"] == "PLN"):
            print(f"{elem['cc']} : {elem['rate']}")

############ Введення валюти #############
def input_currency():
    currency = input("Введіть код валюти (USD, EUR, PLN): ").upper()
    return currency

############ Введення суми #############
def input_amount():
    amount = float(input("Введіть суму валюти: "))
    return amount

############ Основна функція #############
def main():
    print("Конвертер валют (USD, EUR, PLN to UAH)")
    
    # Отримуємо дані від користувача
    currency = input_currency()
    amount = input_amount()
    
    ############## Конвертація ##############
    for elem in response.json():
        if elem["cc"] == currency:
            converted_amount = amount * elem["rate"]
            print(f"\n{amount} {currency} = {converted_amount:.2f} UAH")

############### Запуск ###############
main()