import json
from datetime import datetime, date, timedelta

import pandas as pd

from services.news_service import get_news
from services.sms_service import send_sms
from services.stock_service import get_stock

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

with open("config/stock_data.json", "r") as file:
    data = json.load(file)

time_series = data["Time Series (Daily)"]
df = pd.DataFrame.from_dict(time_series, orient="index")
df.columns = ["Open", "High", "Low", "Close", "Volume"]
df.index = pd.to_datetime(df.index)
df = df.astype(float)

yesterday_date = date.today() - timedelta(days=1)
bf_yesterday_date = date.today() - timedelta(days=2)
yday_value = df.loc[str(yesterday_date)]["Close"]
bfyday_value = df.loc[str(bf_yesterday_date)]["Close"]

# TODO Update function when API is available
# stock_data = get_stock(STOCK)['Time Series (Daily)']
# data_list = [value for (key, value) in data.items()]
# last_3_days = list(time_series.items())[:3]
#
# print(last_3_days[0])
# print(last_3_days[1])
# print(last_3_days[2])
# print((float(last_3_days[0][1]['4. close']) / float(last_3_days[1][1]['4. close'])) * 100)

# for date, values in last_3_days:
#     print(date, values['4. close'])

variation = round((float(yday_value) / float(bfyday_value) - 1) * 100, 2)
symbol, negated_variation = ("🔺", variation) if variation > 0 else ("🔻", variation  * -1)

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

message = f"\n\n{STOCK}: {symbol}{negated_variation}%\n\n"
if variation < 5:
    news_list = list(get_news(date.today() - timedelta(days=1))['articles'][:3])

    for i in news_list:
        message +=  f"Headline: {i['title']} \n" + f"Brief: {i['description']} \n\n"

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 
send_sms(message)

#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

