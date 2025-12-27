# api_fetcher.py - fetch data from a public API and print a summary
import requests

def fetch_iss_location():
    url = 'http://api.open-notify.org/iss-now.json'
    r = requests.get(url, timeout=10)
    if r.status_code != 200:
        print('API error', r.status_code)
        return
    data = r.json()
    pos = data.get('iss_position', {})
    lat = pos.get('latitude')
    lon = pos.get('longitude')
    print(f'ISS current position: latitude={lat}, longitude={lon}')

if __name__ == '__main__':
    fetch_iss_location()
