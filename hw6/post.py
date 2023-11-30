from datetime import datetime
from playwright.sync_api import sync_playwright
from scrape_twitter1 import get_auth_twitter_pg
from scrape_twitter1 import post_tweet
from twitterbot import *



with sync_playwright() as playwright:
        
    browser_dets = get_auth_twitter_pg(playwright)
    if( len(browser_dets) != 0 ):
        #True or False, post_tweet() should return the link of the newly posted tweet. 
        get_new_tweet_link = True

        #Twitter handle of account where message is to be posted
        twitter_account = 'sophiac6170'

        #reply_to_link should contain the link (e.g., 'https://twitter.com/xnwala/status/1699844461545836833') to the tweet to be replied to. Leave blank for isolated post
        reply_to_link = ''

        city = "Norfolk"  # Replace "YourCity" with the city you want weather updates for


        temperature, description = tweet_weather(city)


        
        # Tweet mental health advice based on weather

        tweet_mental_health_advice(temperature, description)


        tweet_cold_weather_advice(temperature)


        various_weather_activities(description)





        