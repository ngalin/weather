# make some api calls - and log weather hourly values in Sydney, AU
# on the hour make call to get current temperature in Sydney, and
# make call and record the 5 day 3hr forecast for Sydney.
# after get 24 x 5 x (24/3) values,

import requests
import schedule
import json
import datetime
import api_secret

CITY = 'Sydney'
COUNTRY = 'au'
QUERY = {"q": "Sydney,au", "APPID": api_secret.APPID}
HEADERS = {
  'Accept': "*/*",
  'Host': "api.openweathermap.org",
  'Connection': "keep-alive",
  'cache-control': "no-cache"
}
URL_NOW_WEATHER = "http://api.openweathermap.org/data/2.5/weather"
URL_FORECAST = "http://api.openweathermap.org/data/2.5/forecast"
CURRENT = open('data/current_weather.json', 'w')
FORECAST = open('data/forecast_weather.json', 'w')


def get_weather():
  json.dump(obj=get_current_weather().json(), fp=CURRENT, sort_keys=True)
  CURRENT.write('\n')
  json.dump(obj=get_forecast_weather().json(), fp=FORECAST, sort_keys=True)
  FORECAST.write('\n')

  print('ran', datetime.datetime.now())
  return


def get_current_weather():
  return requests.request("GET", url=URL_NOW_WEATHER, headers=HEADERS, params=QUERY)


def get_forecast_weather():
  return requests.request("GET", url=URL_FORECAST, headers=HEADERS, params=QUERY)


def main():
  print("Hello World!")
  schedule.every().hour.do(get_weather)

  while True:
    schedule.run_pending()

  CURRENT.close()
  FORECAST.close()


if __name__ == "__main__":
  main()
