import requests


API_KEY = 'AIzaSyDuaH-_tY9TWo6foVp3lhzZ0NdjGEZdDpc'
def get_location(address):
    response = requests.get(f'https://maps.googleapis.com/maps/api/geocode/json?address={address}&key={API_KEY}').json()
    location = response['results'][0]['geometry']['location']
    position = f'{location["lat"]}, {location["lng"]}'
    print(position)
    return position

def get_map(position):
    params = {
                'center':position, 
                'zoom':'15',
                'size':'600x300',
                'maptype':'roadmap',
                'markers':f'color:red|label:I|{position}',
                'key':API_KEY,
            }
    response = requests.get(
                            f'https://maps.googleapis.com/maps/api/staticmap',
                            params = params
                            ).url
    return response

if __name__ == '__main__':
    position = get_location('中國福建省福州市鼓楼区五一北路173号')
    print(get_map(position))
