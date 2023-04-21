import requests

def call(dropdown, days, place):
    datapoints = days*8
    dates = []
    values = []
    APIkey = "08c34f14a1dc20a379a8990c2af3942d"
    url = f'http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={APIkey}'
    requ = requests.get(url)
    contents = requ.json()
    contents = contents['list']
    for dtp in range(0,datapoints,1):
        dates.append(contents[dtp]['dt_txt'])
        if dropdown == 'Temperature':
            values.append(round(contents[dtp]['main']['temp']/10, 1))
        else:
            values.append(round(contents[dtp]['clouds']['all'], 1))
    return (dates, values)

