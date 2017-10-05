import requests, json

#543e5c60a714042074c305d5c7068aae
cityname = input("Enter City: ")
APIKEY = "543e5c60a714042074c305d5c7068aae"
url = "http://api.openweathermap.org/data/2.5/weather?q="+cityname+"&APPID="+APIKEY

response = requests.get(url)
cityweather = response.json()
print(cityweather)
print("Conditions today are", cityweather["weather"][0]["description"])