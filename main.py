import plotext as plt
import requests
from icecream import ic
from datetime import datetime
import os


api_url = 'https://pro-api.coinmarketcap.com/v2/cryptocurrency/quotes/latest'



plt.title("Streaming Data")
plt.clc()
current_price_arr = []
current_time_arr = []
start = 1

while True:

    response = requests.get(api_url, headers={'X-CMC_PRO_API_KEY': ''},
                            params={'slug': 'bitcoin'})
    if response.status_code == requests.codes.ok:
        current_price = (response.json()['data']['1']['quote']['USD']['price'])
    else:
        print("Error:", response.status_code, response.text)
    current_price_arr.append(current_price)
    current_time_arr.append(start)
    start += 1


    plt.clt() # to clear the terminal
    plt.cld() # to clear the data only

    plt.plot(current_time_arr, current_price_arr)
    plt.theme('dark')

    plt.show()
    plt.sleep(60) # to add
