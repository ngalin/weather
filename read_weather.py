import json
from datetime import datetime
import pandas as pd


def get_forecast():
  first_row = True
  nrow = 0

  with open('data/tmp/forecast_weather.json') as f:
    for line in f:
      print(nrow)
      nrow += 1

      res = json.loads(line)
      timezone_offset = res['city']['timezone']
      first_line = True
      for forecast in res['list']:
        if first_line:
          forecast_time = forecast['dt'] + timezone_offset
          first_line = False

        dt = forecast['dt'] + timezone_offset
        if first_row:
          data = pd.DataFrame(forecast['main'],
                              index=[datetime.utcfromtimestamp(forecast_time).strftime('%Y-%m-%d %H:%M:%S')])
          data['dt'] = datetime.utcfromtimestamp(dt).strftime('%Y-%m-%d %H:%M:%S')
          df = pd.DataFrame.from_dict(data)
          first_row = False

        else:
          data = pd.DataFrame(forecast['main'],
                              index=[datetime.utcfromtimestamp(forecast_time).strftime('%Y-%m-%d %H:%M-%S')])
          data['dt'] = datetime.utcfromtimestamp(dt).strftime('%Y-%m-%d %H:%M:%S')
          df = df.append(data)

  df.to_csv('data/tmp/forecast_weather.csv', header=True, index=True)


## processing current weather
def get_current():
  first_row = True
  nrow = 0

  with open('data/tmp/current_weather.json') as f:
    for line in f:
      res = json.loads(line)
      timezone_offset = res['timezone']
      dt = res['dt'] + timezone_offset
      print(nrow)
      nrow += 1
      if first_row:
        data = pd.DataFrame(res['main'], index=[datetime.utcfromtimestamp(dt).strftime('%Y-%m-%d %H:%M:%S')])
        df = pd.DataFrame.from_dict(data)
        first_row = False

      else:
        data = pd.DataFrame(res['main'], index=[datetime.utcfromtimestamp(dt).strftime('%Y-%m-%d %H:%M:%S')])
        df = df.append(data)

      print(datetime.utcfromtimestamp(dt).strftime('%Y-%m-%d %H:%M:%S'))

    df.to_csv('data/tmp/current_weather.csv', header=True, index=True)


def main():
  get_forecast()
  get_current()


if __name__ == "__main__":
  main()
