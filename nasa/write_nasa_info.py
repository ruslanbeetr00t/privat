import json
import requests
from nasa_api import API


mars_rover_url = f'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=1000&page=2&api_key={API}'


def request_url():
    try:
        response = requests.get(mars_rover_url)
        if response.status_code == 200:
            print(response.json())
            return response.json()
    except requests.ConnectionError:
        print('Connection Error, try again later or fix bug')


def write_json_file_with_photo_info():
    with open('nasa_photo.json', 'w', encoding='utf-8') as file_json:
        json.dump(request_url(), file_json, ensure_ascii=False, indent=4)
        return 'nasa_photo.json'


def images_nasa():
    images = request_url()['photos']
    print(f'Знайдено:-{len(images)} фото')
    print('Яку фотографію ви хочете переглянути?')
    print(images[9])

images_nasa()
