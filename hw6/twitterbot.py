from datetime import datetime

import tweepy
import requests
import json
import time

# from twitter: 
consumer_key='K8K8lrRJin9ya4cAFCheiuDi9',
consumer_secret='OtaWRUtd0dD59dJTQnHw97BBNIINOd896hYykgbM3Mu3aR3kVR',
access_token='1726342082598486016-2DHyzNWZtvX4HCcbUaFeubJC85mYih',
access_token_secret='wLBrVJuCIFZchftZYqy3ZETEsy1wVE7SddxUbYEiBwzRn'



client = tweepy.Client(consumer_key='K8K8lrRJin9ya4cAFCheiuDi9',
consumer_secret='OtaWRUtd0dD59dJTQnHw97BBNIINOd896hYykgbM3Mu3aR3kVR',
access_token='1726342082598486016-2DHyzNWZtvX4HCcbUaFeubJC85mYih',
access_token_secret='wLBrVJuCIFZchftZYqy3ZETEsy1wVE7SddxUbYEiBwzRn')




city = 'Norfolk'
consumer_key = 'ddaa5125c9d89295555ec93230e2e96b'



weather_api_key = 'ddaa5125c9d89295555ec93230e2e96b'
consumer_key = 'ddaa5125c9d89295555ec93230e2e96b'


def relaxing_nice_weather_activities():
    try:
        # Make a GET request to the Bored API
        response = requests.get('http://www.boredapi.com/api/activity?type=relaxation')

    # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the JSON response
            data = response.json()
        
            # Display the suggested activity
            print(data.get("activity"))
            #print("Type:", data.get("type"))
            #print("Participants:", data.get("participants"))
            #print("Price:", data.get("price"))
            #print("Link:", data.get("link"))
            #print("Key:", data.get("key"))
    except Exception as e:
        print("An error has occured: ", e)


def social_nice_weather_activities():
    try:
        # Make a GET request to the Bored API
        response = requests.get('http://www.boredapi.com/api/activity?type=social')

    # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the JSON response
            data = response.json()
        
            # Display the suggested activity
            print(data.get("activity"))
            #print("Type:", data.get("type"))
            #print("Participants:", data.get("participants"))
            #print("Price:", data.get("price"))
            #print("Link:", data.get("link"))
            #print("Key:", data.get("key"))
    except Exception as e:
        print("An error has occured: ", e)




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
    
    # Extract relevant information from the API response
    temperature = weather_data['main']['temp']
    description = weather_data['weather'][0]['description']
    
    #message = f"Current weather in {city} @ {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}: {temperature}°C, {description}"


    #response = client.create_tweet(text=message) #the two var in this, temp and description (the outputs) in this will be used in tweet_mental_health_advice 
    #api.update_status(message) needs upgraded subscription to v1 endpoint 
    
    return temperature, description

def tweet_cold_weather_advice(temperature):
  temp = float(temperature)
  if temp < 60:
    advice = f"Brrrrrrrr, it is kind of chilly right now, make sure to stay warm! Layers, coats, thick socks are all quite essential to wear before going out! Update @ {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}: {temperature}°C, {description}"
  else:
    advice = f"Looks like it is going to feel great today based on the temperature outside! Temperature Update {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}: {temperature}°C, {description} "
  response = client.create_tweet(text=advice)



def tweet_mental_health_advice(temperature, description):
    if "rain" in description.lower() or "storm" in description.lower() or "snow" in description.lower():
        advice = f"Uh-oh, looks like the weather is not going to be so great right now. Take it easy today! Consider staying indoors and practicing self-care. Make sure to not stay in dark spaces too long, maybe try having an artificial sunlight lamp to keep you warm and bright :), as a kind reminder, the current time is now {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}: {temperature}°C, {description}. Reach out to friends or family if you need more support. If you ever need to go outside, make sure to dress warmly, bring an umbrella, and promise me to take precautionary measures on the road, ok?"
    elif 'mist' in description.lower():
        advice = f"It's currently {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}: {temperature}°C, {description} and the weather is also looking pretty foggy! Make sure to take some precautions when going outside. The lack of sunlight may have an negative impact your mood. If it does, even by the slightest bit, try practicing Radical Acceptance, which is saying yes to reality instead of no, no, no! For example, instead of fighting the negativity of the weather, try to think of ways that can help you work with it. In this case, maybe try asking yourself if you would like to travel to another place warmer or go along with the mood of the weather and stay inside to cozy up with relaxing in-door activities."
    else:
        advice = f"It's currently {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}: {temperature}°C, {description} ,and also a good day! Take advantage of the weather and engage in activities that bring you joy and relaxation. What is the last thing you did that bought you joy?"
    response = client.create_tweet(text=advice)




def various_weather_activities(description):
    if "rain" not in description.lower() or "storm" not in description.lower() or "snow" not in description.lower() or 'mist' not in description.lower():
        try:
            # Make a GET request to the Bored API
            response = requests.get('http://www.boredapi.com/api/activity?type=recreational')
    #     response3 = requests.get('http://www.boredapi.com/api/activity?type=social')

            # Check if the request was successful (status code 200)
            if (response.status_code == 200):
                # Parse the JSON response
                data = response.json()


                act = data.get("activity")
                advice2 = f"How are you feeling about trying this activity: {act}?"

            response = client.create_tweet(text=advice2)


        except Exception as e:
            print("An error has occured: ", e)
    else:
        try:
            # Make a GET request to the Bored API
            response = requests.get('http://www.boredapi.com/api/activity?type=relaxation')

            # Check if the request was successful (status code 200)
            if (response.status_code == 200):
                # Parse the JSON response
                data = response.json()


                act = data.get("activity")
                advice = f"How are you feeling about trying this activity: {act}?"

            response = client.create_tweet(text=advice)


        except Exception as e:
            print("An error has occured: ", e)





def relaxing_activities(description):

    try:
        # Make a GET request to the Bored API
        response2 = requests.get('http://www.boredapi.com/api/activity?type=relaxation')
        #response3 = requests.get('http://www.boredapi.com/api/activity?type=social')

    # Check if the request was successful (status code 200)
        if (response2.status_code == 200) and ("rain" in description.lower() or "storm" in description.lower() or "snow" in description.lower()):
            # Parse the JSON response
            data = response.json()


            act = data.get("activity")
            advice2 = f"How are you feeling about trying this activity: {act}?"

        response = client.create_tweet(text=advice2)


    except Exception as e:
        print("An error has occured: ", e)


while True:
    city = "Norfolk"  # Replace "YourCity" with the city you want weather updates for

    temperature, description = tweet_weather(city)
    
    # Tweet mental health advice based on weather
    tweet_mental_health_advice(temperature, description)

    time.sleep(8 * 60 * 60) # Tweet every Tweet every 8 hr


    various_weather_activities(description)


    time.sleep(3 * 60 * 60)  # Tweet every 3 hr


    various_weather_activities(description)

    time.sleep(4 * 60 * 60)  # Tweet every 4 hr


    tweet_cold_weather_advice(temperature)
    time.sleep(7 * 60 * 60) # Tweet every Tweet every 7 hr




    

