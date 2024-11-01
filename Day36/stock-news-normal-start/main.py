import requests
from dotenv import load_dotenv
import os
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

load_dotenv()
STOCK_API_KEY = os.getenv('STOCK_API_KEY')
NEWS_API_KEY = os.getenv('NEWS_API_KEY')
SID_KEY = os.getenv('SID_KEY')
AUTH_TOKEN = os.getenv('AUTH_TOKEN')

    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

#TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]
stock_paprams = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY
}
response = requests.get(STOCK_ENDPOINT, params = stock_paprams)
data = response.json()['Time Series (Daily)']
data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data['4. close']
print(yesterday_closing_price)
 
#TODO 2. - Get the day before yesterday's closing stock price
day_before_yesterday_data = data_list[1]
day_before_yesterday_data = day_before_yesterday_data['4. close']
print(day_before_yesterday_data)

#TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp
difference = float(yesterday_closing_price) - float(day_before_yesterday_data)
up_down = None
if difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

#TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
percentage_difference = round((difference / float(yesterday_closing_price)) * 100)

#TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").
if abs(percentage_difference) > 3:
    news_params = {
        "apiKey": NEWS_API_KEY,
        "qInTitle": COMPANY_NAME
    }
    ## STEP 2: https://newsapi.org/
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 
    
#TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.
    news_response = requests.get(NEWS_ENDPOINT, params = news_params)
    articles = news_response.json()['articles']
    
#TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation
    three_articles = articles[:3]

    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number. 

#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.
    formatted_articles = [f"{STOCK_NAME}: {up_down}{percentage_difference}%\nHeadline: {article['title']}. \nBrief: {article['description']}" for article in three_articles]

#TODO 9. - Send each article as a separate message via Twilio. 
    client = Client(SID_KEY, AUTH_TOKEN)

    for article in formatted_articles:
        message = client.messages.create(
            from_='+17083040184',
            body=article,
            to='+--------' # Your phone number
        )
        
        print(message.sid)
    