import requests

# status
resp = requests.get('http://127.0.0.1:5051/health').json()
print(resp)

# get
resp = requests.get('http://127.0.0.1:5051/ads/1').json()
print(resp)

# post
resp = requests.post('http://127.0.0.1:5051/ads/',
                     json={
                         'title': 'Объявление 4',
                         'description': 'Описание объявлени 4',
                         'data_create': '2022-03-11',
                         'user_id': 1
                     }).json()
print(resp)

# delete
resp = requests.delete('http://127.0.0.1:5051/ads/23').json()
print(resp)

# put
resp = requests.put('http://127.0.0.1:5051/ads/24',
                     json={
                         'title': 'Объявление 55556',
                         'description': 'Описание объявлени 44446',
                         'data_create': '2022-03-11',
                         'user_id': 1
                     }).json()
print(resp)