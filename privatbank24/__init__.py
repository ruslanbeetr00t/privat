import json
import requests

in_cassa_url = 'https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5'
online_excange_url = 'https://api.privatbank.ua/p24api/pubinfo?exchange&json&coursid=11'


def cash_rate():
    response = requests.get(in_cassa_url)
    if response.status_code == 200:
        in_cass_info = response.json()
        print(in_cass_info)
        return in_cass_info


def cashless_rate():
    response = requests.get(online_excange_url)
    if response.status_code == 200:
        online_info = response.json()
        print(online_info)
        return online_info


def write_json_file():
    full_wallet_info = cash_rate(), cashless_rate()
    with open('wallet.json', 'w', encoding='utf-8') as file_json:
        json.dump(full_wallet_info, file_json, ensure_ascii=False, indent=4)
        return 'wallet.json'


def full_info():
    answer = int(input("""
    Виберіть дію яку бажаете виконати, натисніть:
    1 = якщо вам потрібен готівковий курс у відділеннях ПриватБанку,
    2 = якщо вам потрібен безготівковий обмінний курс у privat24,
    3 = для запису json файлу:
    Введіть команду:-"""))
    if answer == 1:
        cash_rate()
    elif answer == 2:
        cashless_rate()
    elif answer == 3:
        write_json_file()
    else:
        print('CATASTROFA')
        return full_info()


full_info()