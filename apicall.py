import requests

def call(days, place):
    datapoints = days*8
    APIkey = "08c34f14a1dc20a379a8990c2af3942d"
    url = f'http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={APIkey}'
    requ = requests.get(url)
    contents = requ.json()
    contents = contents['list']
    return (datapoints, contents)

