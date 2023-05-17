import requests
import json
import info_operations


def send_responce():
    url = 'http://127.0.0.1:5000/api'
    data = info_operations.read_info()
    response = requests.post(url, json=data)
    if response.status_code == 200:
        json_data = response.json()
        with open('data/response.json', 'w', encoding='utf-8') as f:
            json.dump(json_data, f, ensure_ascii=False, indent=4)
    else:
        print(f'Error: {response.status_code}')
