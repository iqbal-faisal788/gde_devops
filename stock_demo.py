import requests

url = "https://twelve-data1.p.rapidapi.com/quote"

querystring = {"symbol":"AMZN"}

headers = {
	"X-RapidAPI-Key": "51fc172253mshb6b58650d625e9ep14b00ejsna48ec6c423e9",
	"X-RapidAPI-Host": "twelve-data1.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring).json()

symbol = response['symbol']
name = response["name"]
currency = response.get('currency')
date = response["datetime"]
open = float(response.get('open'))
high = float(response.get('high'))
low = float(response.get('low'))
close = float(response.get('close'))
volume = int(response.get('volume'))

#print(response)

print(f'{symbol}\n{name}\n{currency}\n{date}\n{open}\n{high}\n{low}\n{close}\n{volume}')


"""

{
  "average_volume": "4801633",
  "change": "55.56006",
  "close": "3173.00000",
  "currency": "USD",
  "datetime": "2020-09-14",
  "exchange": "NASDAQ",
  "fifty_two_week": {
    "high": "3552.25000",
    "high_change": "-379.25000",
    "high_change_percent": "-10.67633",
    "low": "1626.03003",
    "low_change": "1546.96997",
    "low_change_percent": "95.13785",
    "range": "1626.030029 - 3552.250000"
  },
  "high": "3186.98999",
  "low": "3144.25195",
  "name": "Amazon.com Inc",
  "open": "3172.93726",
  "percent_change": "1.78223",
  "previous_close": "3117.43994",
  "symbol": "AMZN",
  "volume": "1178898"
}

"""