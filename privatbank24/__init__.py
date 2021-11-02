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


def archiv_wallet():
    day = int(input('add day'))
    month = int(input('add month'))
    year = int(input('add year'))
    archiv_wallet_url = f'https://api.privatbank.ua/p24api/exchange_rates?json&date={day}.{month}.{year}'
    response = requests.get(archiv_wallet_url)
    if response.status_code == 200:
        archiv = response.json()
        print(archiv)
        return archiv


def self_service_terminal():
    city = input('add you city')
    self_service_terminal_url = f'https://api.privatbank.ua/p24api/infrastructure?json&tso&address=&city={city}'
    response = requests.get(self_service_terminal_url)
    if response.status_code == 200:
        terminal = response.json()
        print(terminal)
        return terminal


def write_json_self_service_terminal():
    with open('self_service_terminal.json', 'w', encoding='utf-8') as file_json:
        json.dump(self_service_terminal(), file_json, ensure_ascii=False, indent=4)


def write_json_archiv():
    with open('archiv.json', 'w', encoding='utf-8') as file_json:
        json.dump(archiv_wallet(), file_json, ensure_ascii=False, indent=4)


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
    3 = для запису json файлу,
    4 = для перегляду архіву валют,
    5 = для створення json файлу з архівам валют,
    6 = для пошуку термінала самообслуговування,
    7 = для створення json файлу з розташуванням терміналів самообслуговування у вашому місті,
    Введіть команду:-"""))
    if answer == 1:
        cash_rate()
    elif answer == 2:
        cashless_rate()
    elif answer == 3:
        write_json_file()
    elif answer == 4:
        archiv_wallet()
    elif answer == 5:
        write_json_archiv()
    elif answer == 6:
        self_service_terminal()
    elif answer == 7:
        write_json_self_service_terminal()
    else:
        print('CATASTROFA')
        return full_info()


full_info()
#Код валюты (справочник кодов валют: https://ru.wikipedia.org/wiki/Коды_валют)