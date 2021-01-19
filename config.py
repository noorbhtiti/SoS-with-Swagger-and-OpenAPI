import json

class api1:
    def __init__(self, api2):
        self.api2 = api2

    def get(self):
        data = self.api2.get()
        return data

class api2:
    def __init__(self, api3):
        self.api3 = api3

    def get(self):
        
        return self.api3.get()

class api3:
    def __init__(self, source):
        self.source = source

    def get(self):
        data = self.source
        return data


def main():
     data = {"name" : "Luleå", "country" : "Sweden", "temp" : -13}
     a3 = api3(data)
     a2 = api2(a3)
     a1 = api1(a2)

     print(a1.get())

if __name__ == "__main__":
    main()