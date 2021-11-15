import json


def read_nasa_json_info():
    with open('nasa_photo.json', 'r') as file_json:
        photo = json.load(file_json)
        # print(photo)
        # photo = response.json()["photos"]
        # print(f"Finde{len(photo)} photos")
        # print(photo[99]['img_src'])
        for photos in photo['photos']:
            all_photos = [photos['img_src']]
            print(all_photos)


read_nasa_json_info()