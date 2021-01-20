import json
import urllib.request

class api1:
    def __init__(self, api2):
        self.api2 = api2

    def get(self, city):
        data = self.api2.get(city)
        temp = {"temp" : (str(data['temp']))+' c'}
        return temp

class api2:
    def __init__(self, api3):
        self.api3 = api3

    def get(self, city):
        data = self.api3.get(city)
        tempinc = ((data['main']['temp']) - 273.15)
        temp = ("%.2f" % tempinc)
        data = {"temp" : str(temp)} 
        return data

class api3:
    def __init__(self):
        self.apikey = 'e8e4ff8f8290aee90e6800ec0eeb245f'

    def get(self, city):
        source = urllib.request.urlopen('https://api.openweathermap.org/data/2.5/weather?q=' + city + '&appid=' + self.apikey).read()
        data = json.loads(source)
        return data

def main():
     
     a3 = api3()
     a2 = api2(a3)
     a1 = api1(a2)

     print(a1.get('stockholm'))

if __name__ == "__main__":
    main()