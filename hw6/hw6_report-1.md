# HW6 - Creating (good) social bots
### Sophia Chen
### DS 440, Fall 2023
### November 21, 2023

# Assignment

Social bots have been used to inflate the popularity of political candidates, influence public opinion through the spread of disinformation and conspiracy theories, and manipulate stock prices through coordinated campaigns. The threats posed by malicious actors that utilize social bots are far-reaching, endangering democracy, public health, and the economy.

However, not all bots are bad. In this assignment you will prove this point by creating a (good) Twitter bot. You will NOT be scored on the complexity or sophistication of the Twitter bot, instead, you will be scored on the usefulness and originality/innovation of the bot.

Your Twitter bot must post tweets on a special Twitter account created by you.

# Criteria 1. Usefulness (4 points)

Consider creating a bot to solve or partly solve a problem you care about --- maybe not poverty or crime or income inequality. In other words create a tool to address a need. Provide an argument in your report for the reason your Twitter bot is useful.

## Answer + Discussion

For this assignment, I created a Twitter bot that posts tweets about the weather in Norfolk, VA, and gives mental health advice according to that criteria. For example, depending on the weather outside, whether sunny, windy, cold, hot, etc., it would recommend what the best actions to take are. This will be primarily useful for people who suffer from mental health illnesses, such as seasonal depression disorder, major depressive disorder, or ADHD. There are many more mental disorders, and this list presents a few examples of common mental disorders in our community. 
I also added another feature to it that can provide you with some example activities that you can do when you can't come up with things to do. 

This bot is helpful, especially for people who suffer from seasonal depression or other mental health disorders, as this can give advice when these individuals lack the motivation to engage in activities during bad weather conditions. In addition, these tweets are created in a way that offers thorough advice or allows the audience to reflect on positive thoughts during nice weather. The goal here is to promote happiness and good feelings. 


When implemented, this bot is supposed to tweet every 8-10 hours, reflecting on the daily change in weather conditions. It considers the times when people feel productive, offline, or resting. Since many people do not follow a traditional work shift, this bot also accommodates those who fall into this category by posting at diverse times. 

I initially made this bot tweet every 4 hours to check for its functionality.

An example is this tweet: 


sophia
@sophiac6170
·
Nov 25
It's currently 2023-11-25 14:20:16: 2.4°C, clear sky ,and also a good day! Take advantage of the weather and engage in activities that bring you joy and relaxation What is the last thing you did that bought you joy?

By asking the question at the end of the tweet, the audience can think about the good memories and these maybe can remind them of the positive things they experienced. 

In contrast, when the weather is not at its greatest condition outside, my twitter bot will tweet a message that warns the audience about the bad conditions and advise them to take the necessary pre-cautions to be safe outside. Since bad weather are rare these days, the bot has not recieved the oppounity to post messages to help the audience when there is rain, snow, fog, etc. 



 Another useful property in which the twitter bot can be useful is its ability to post example activities when the audience have hard times thinking about what to do. Example activities include writing a short story, learning on how to play a new card game, learning sports, etc. 

An example is this tweet: 


sophia
@sophiac6170 · 9m

How are you feeling about trying this activity: Go see a Broadway production?

This is the following code I wrote for this program. 

```python

%pip install 

from tweepy import *
from datetime import datetime

import requests
import json
import time


client = tweepy.Client(consumer_key='K8K8lrRJin9ya4cAFCheiuDi9',
consumer_secret='OtaWRUtd0dD59dJTQnHw97BBNIINOd896hYykgbM3Mu3aR3kVR',
access_token='1726342082598486016-2DHyzNWZtvX4HCcbUaFeubJC85mYih',
access_token_secret='wLBrVJuCIFZchftZYqy3ZETEsy1wVE7SddxUbYEiBwzRn')


# from twitter:
consumer_key='K8K8lrRJin9ya4cAFCheiuDi9'
consumer_secret='OtaWRUtd0dD59dJTQnHw97BBNIINOd896hYykgbM3Mu3aR3kVR'
access_token='1726342082598486016-2DHyzNWZtvX4HCcbUaFeubJC85mYih'
access_token_secret='wLBrVJuCIFZchftZYqy3ZETEsy1wVE7SddxUbYEiBwzRn'


city = 'Norfolk'

weather_api_key = 'ddaa5125c9d89295555ec93230e2e96b'
consumer_key = 'ddaa5125c9d89295555ec93230e2e96b'

# checking the dictionary 
base_url = "http://api.openweathermap.org/data/2.5/weather"
params = {'q': city, 'appid': consumer_key, 'units': 'metric'}
response = requests.get(base_url, params=params)
weather_data = response.json()
weather_data

def get_weather(weather_api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {'q': city, 'appid': consumer_key, 'units': 'metric'}
    response = requests.get(base_url, params=params)
    weather_data = response.json()
    return weather_data


def celsius_to_fahrenheit(celsius):
    celsius = weather_data['main']['temp']
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def tweet_weather(city):
    weather_data = get_weather(weather_api_key, city)
    print("Weather Data:", weather_data)
    celsius = weather_data['main']['temp']

    # Extract relevant information from the API response
    temperature = weather_data['main']['temp']
    description = weather_data['weather'][0]['description']

    #message = f"Current weather in {city} @ {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}: {temperature}°C, {description}"



    #response = client.create_tweet(text=message)
    #api.update_status(message) needs upgraded subscription to v1 endpoint

    return temperature, description

def tweet_cold_weather_advice(temperature):
  temp = float(temperature)
  if temp < 60:
    advice = f"It's currently {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}: {temperature}°C, {description} , and brrrrrrrr, it is kind of chilly right now, make sure to stay warm! "
  else:
    advice = f"It's currently {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}: {temperature}°C, {description} , and looks like it is a great day!"
  response = client.create_tweet(text=advice)


def tweet_mental_health_advice(temperature, description):
    if "rain" in description.lower() or "storm" in description.lower() or "snow" in description.lower():
        advice = f"Uh-oh, looks like the weather is not going to be so great right now. Take it easy today! Consider staying indoors and practicing self-care. Make sure to not stay in dark spaces too long, maybe try having an artificial sunlight lamp to keep you warm and bright :), as a kind reminder, the current time is now {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}: {temperature}°C, {description}. Reach out to friends or family if you need more support. If you ever need to go outside, make sure to dress warmly, bring an umbrella, and promise me to take precautionary measures on the road, ok?"
    elif 'mist' in description.lower():
        advice = f"It's currently {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}: {temperature}°C, {description} and the weather is also looking pretty foggy! Make sure to take some precautions when going outside. The lack of sunlight may have an negative impact your mood. If it does, even by the slightest bit, try practicing Radical Acceptance, which is saying yes to reality instead of no, no, no! For example, instead of fighting the negativity of the weather, try to think of ways that can help you work with it. In this case, maybe try asking yourself if you would like to travel to another place warmer or go along with the mood of the weather and stay inside to cozy up with relaxing in-door activities."
    else:
        advice = f"It's currently {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}: {temperature}°C, {description} ,and also a good day! Take advantage of the weather and engage in activities that bring you joy and relaxation What is the last thing you did that bought you joy?"

    response = client.create_tweet(text=advice)


while True:
    city = "Norfolk"  # Replace "YourCity" with the city you want weather updates for
    temperature, description = tweet_weather(city)

    # Tweet mental health advice based on weather
    tweet_mental_health_advice(temperature, description)

    tweet_cold_weather_advice(temperature)

    time.sleep(60)  # Tweet every 4 hours


```
In addition, I copied all of this to a py file called twitterbot.py and imported its functions to use in another file called post.py. This file contains parts of the provided code used to scrape Twitter, such as the scrape_twitter1 file provided by Professor Nwala. The post.py file is where all of the functions are gathered and used for execution. 




# Criteria 2. Originality/Innovation (4 points)

Express yourself, be creative. Alternatively, consider improving a pre-existing solution or tool. Provide an argument in your report for the reason your Twitter bot is original or innovative.

## Answer + Discussion


My Twitter bot is helpful because it incorporates creative ideas of combining topics of mental health and data science to impact our community positively. 

In this case, programming a type of data science software that helps people with mental disabilities will be extremely useful in the mental health community. 

The reason why I say this is because, at first, while looking for inspiration to create my bot, I could not find many bots that post mental health advice, especially for members of the community who suffer from ADHD and depression in Norfolk, Va. Thus, I created a bot that addresses this issue. 

I can improve this further by designing more features that can enhance the impact the bot can bring. For example, I was thinking about creating a part that posts about the temperature of the weather. If the temperature of the weather is low, then I will make this bot post and inform the audience about the weather and how to take the necessary actions to protect themselves from this. I have written an essential function to carry out this task, but I plan to expand it further. 

Additionally, I want to post aesthetically pleasing graphics, pictures, or memes for users who have difficulty reading posts. Another helpful feature of this bot is the ability to reuse or retweet other people's posts about positive mental health media. These will maximize the helpfulness of this bot, and in the future, I plan to revise this project to improve it. 



# References

* Social Bots explained: how do Social Bots work?, <https://www.example.com>
* *args and **kwargs in Python, <https://www.geeksforgeeks.org/args-kwargs-python/>
* How to make a Twitter Bot in Python?, <https://www.geeksforgeeks.org/how-to-make-a-twitter-bot-in-python/>
* Check multiple conditions in if statement – Python, <https://www.geeksforgeeks.org/check-multiple-conditions-in-if-statement-python/>
* if elif else, <https://www.pythonclassroom.com/decisions-if-elif-else/if-elif-else>
* Playwright, <https://playwright.dev/python/docs/api/class-playwright>
* 403 Forbidden 453 - You currently have access to a subset of Twitter API v2 endpoints and limited v1.1 endpoints only, <https://stackoverflow.com/questions/76528610/403-forbidden-453-you-currently-have-access-to-a-subset-of-twitter-api-v2-endp>
* Why is my Twitter bot not posting it's ".update_status"?, <https://stackoverflow.com/questions/70255707/why-is-my-twitter-bot-not-posting-its-update-status>
* Usage of Twitter API v2 with tweepy and pandas in Python, <https://www.kirenz.com/post/2021-12-10-twitter-api-v2-tweepy-and-pandas-in-python/twitter-api-v2-tweepy-and-pandas-in-python/>
* Twitter API v2, <https://developer.twitter.com/en/docs/twitter-api>
* OpenWeather, <https://openweathermap.org/>
* Weather API, <https://openweathermap.org/api>
* Bored API Documentation, <https://www.boredapi.com/documentation#endpoints-type>
* Mental Health Goes Digital: How APIs are Helping to Improve Access and Support, <https://dev.to/techdecoderjonny/mental-health-goes-digital-how-apis-are-helping-to-improve-access-and-support-567i>
