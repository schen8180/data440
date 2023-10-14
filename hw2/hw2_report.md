# HW2 - Archiving the Web 
### Sophia Chen
### DATA 440, Fall 2023
### Due Tuesday October 10, 2023

# Part 1
## Q1 

Q1. Collect URIs from Tweets (2 points)
Extract 1000 unique links from tweets in Twitter.

Main steps:

- Create a special Twitter account
- Write a Python program that collects English-language tweets that contain links. See Collecting Tweets.
- Write a Python program that extracts the links shared in tweets. See Extracting Links from Tweets.
- Resolve all URIs to their final target URI (i.e., the one that responds with a 200). See Resolve URIs to Final Target URI.
- Save only unique final URIs (no repeats). See Save Only Unique URIs.

if after this step, you don't have 1000 unique URIs, go back and gather more until you are able to get at least 1000 unique URIs

- Save this collection of 1000 unique links in a file and upload it to your repo in GitHub -- we'll use it again in HW3

### Collecting Tweets

Scrape tweets from the Twitter Search Engine Result Page (SERP). You'll likely need to collect more than 1000 tweets initially to get 1000 unique links.

Feel free to use multiple keywords to extract tweet. For example, you could collect 250 tweets each about 5 different keywords. Use keywords (e.g., 'covid', 'olympics', 'vaccine') and not "stopwords" (e.g., test, the, tweet).

### Extracting Links from Tweets

Links in tweets are stored in the ['entities']['urls'] part of the tweet dictionary structure. This has several components:

- 'url' - The shortened URI (usually starting with https://t.co/)
- 'expanded_url' - The actual URI that was input by the user (i.e., not shortened)
- 'display_url' - The text of the URI that is displayed in the tweet (counted as part of the 280-character limit in the tweet)

Since we want the actual URIs, you want to extract the 'expanded_url' version of the link. There's an example in process_tweets.py.

We will be analyzing the content in these links in a later assignment, so you want links that will likely contain some text.

- Exclude links from the Twitter domain (twitter.com) -- these will likely be references to other tweets or images

- Exclude links that will likely point to a video/audio-only page (youtube.com, twitch.com, soundcloud.com, etc.)


If you find a link you consider to be inappropriate for any reason, just discard it and get some more links.

### Resolve URIs to Final Target URI
Many of the links that you collect will be shortened links (dlvr.it, bit.ly, buff.ly, etc.). We want the final URI that resolves to an HTTP 200 (not a redirection). For example:
```
$ curl -IL --silent http://bit.ly/wc-wail | egrep -i "(HTTP/1.1|HTTP/2|^location:)"
HTTP/1.1 301 Moved Permanently
Location: http://ws-dl.blogspot.com/2013/07/2013-07-10-warcreate-and-wail-warc.html
HTTP/1.1 301 Moved Permanently
Location: https://ws-dl.blogspot.com/2013/07/2013-07-10-warcreate-and-wail-warc.html
HTTP/2 200
```
We want https://ws-dl.blogspot.com/2013/07/2013-07-10-warcreate-and-wail-warc.html, not http://bit.ly/wc-wail.


You can either write a Unix shell script that uses curl to do this, or write a Python program using the requests library. If you use the Python requests library, make sure to include the timeout parameter to your call to get().

Example: requests.get(url, timeout=5)   # 5 second timeout
### Save Only Unique URIs
You can write Python code for this part, but I'd recommend using the Unix tools sort and uniq. Back to Basics: Sort and Uniq is a nice introduction to this.



## Answer

```
import sys
import time

from bs4 import BeautifulSoup
from datetime import datetime
from NwalaTextUtils.textutils import genericErrorInfo
from NwalaTextUtils.textutils import getLinks

from playwright.sync_api import sync_playwright
from urllib.parse import quote_plus

from util import paral_rehydrate_tweets
from util import rehydrate_tweet
from util import write_tweets_to_jsonl_file

from scrape_twitter import get_auth_twitter_pg
from scrape_twitter import get_search_tweets
#from scrape_twitter import get_timeline_tweets
from util import write_tweets_to_jsonl_file

import gzip
import json


def is_twitter_user_auth(links, cur_page_uri):

    if( cur_page_uri.strip().startswith('https://twitter.com/home') ):
        return True

    logged_in_links = ['https://twitter.com/home', 'https://t.co/']

    for l in links:
        for log_l in logged_in_links:
            if( l['link'].startswith(log_l) ):
                return True
    return False

def scroll_up(page):
    page.evaluate("window.scrollTo( {'top': 0, 'left': 0, 'behavior': 'smooth'} );")

def scroll_down(page):
    page.evaluate("window.scrollTo( {'top': document.body.scrollHeight, 'left': 0, 'behavior': 'smooth'} );")

def post_tweet(page, msg, button_name='Post', after_post_sleep=2.5):
    #Post, Reply
    # [id$='someId'] will match all ids ending with someId: https://stackoverflow.com/a/8714421
    eval_str = f''' document.querySelectorAll('[aria-label$="{button_name}"]')[0].click(); '''
    page.evaluate(eval_str)
    time.sleep(1)
    page.keyboard.type(msg, delay=20)
    page.evaluate(''' document.querySelectorAll('[data-testid="tweetButton"]')[0].click(); ''')

    #added because I observed that tweets were not posted without it
    time.sleep(after_post_sleep)

    
def color_tweet(page, tweet_link):

    query_slc = f'''article = document.querySelectorAll('[href="{tweet_link}"]');'''
    page.evaluate(query_slc + '''
        if( article.length != 0 )
        {
            article = article[0];
            article.style.backgroundColor = 'red';
            i = 0;
            while(i < 1000)
            {
                if( article.nodeName == 'ARTICLE' )
                {
                    article.style.outline = "thick solid red";
                    article.className = "cust-tweet";
                    break;
                }
                article = article.parentElement;
                i++;
            }
        }
    ''')


def get_tweet_ids_user_timeline_page(screen_name, page, max_tweets):

    prev_len = 0
    empty_result_count = 0
    
    tweet_links = set()
    break_flag = False

    while( True ):

        page_html = page.content()
        soup = BeautifulSoup(page_html, 'html.parser')
        articles = soup.find_all('article')        

        for i in range(len(articles)):
            
            t = articles[i]
            is_retweet = t.find('span', {'data-testid': 'socialContext'})
            is_retweet = False if is_retweet is None else is_retweet.text.strip().lower().endswith(' retweeted')
            
            tweet_datetime = ''
            tweet_link = t.find('time')
            
            if( tweet_link is None ):
                tweet_link = ''  
            else:
                tweet_datetime = tweet_link.get('datetime', '')
                tweet_link = tweet_link.parent.get('href', '')

            if( tweet_link == '' ):
                continue


            if( screen_name != '' and is_retweet is False and tweet_link.startswith(f'/{screen_name}/') is False ):
                #This tweet was authored by someone else, NOT the owner of the timeline, and since it was not retweeted
                continue

            #color_tweet(page, tweet_link)
            tweet_links.add( tweet_link )
            twt_id = tweet_link.split('/status/')[-1]
            tweet_obj = rehydrate_tweet(twt_id)
            if( len(tweet_obj) == 0 ):
                print('\tOOPS! rehydration failed! patch rehydrate_tweet()')
                continue

            print( '\ttweets {}, datetime: {}, is_retweet: {}'.format(len(tweet_links), tweet_datetime, is_retweet) )
            #print( f'\tdo stuff here with tweet_obj: {tweet_obj.keys()}\n' )
            
            
            #call your functions here to do stuff with tweet_obj like writing links to text file
            #this function call
            
            #file_path = 'mynewlinks.txt'
            if 'urls' in tweet_obj.get('entities', []):
                for link in tweet_obj['entities']['urls']:
                    print(link['expanded_url'])
                    if 'twitter.com' not in link['expanded_url'] and 'soundcloud.com' not in link['expanded_url'] and 'twitch.com' not in link['expanded_url']:
                        with open('my2.txt', 'a') as file:
                            file.writelines(link['expanded_url'] + '\n')
          
            if( len(tweet_links) == max_tweets ):
                print(f'exiting reached ({len(tweet_links)}) maximum: {max_tweets}')
                sys.exit(0)

        empty_result_count = empty_result_count + 1 if prev_len == len(tweet_links) else 0
        if( empty_result_count > 5 ):
            print(f'No new tweets found, so exiting')
            sys.exit(0)

        prev_len = len(tweet_links)
        print('\tthrottling/scrolling, then sleeping for 2 second\n')
        scroll_down(page)
        time.sleep(2)
    

def get_timeline_tweets(browser_dets, screen_name, max_tweets=20):

    screen_name = screen_name.strip()
    if( max_tweets < 0  or len(browser_dets) == 0 or screen_name == '' ):
        return {}

    print( f'\nget_timeline_tweets(): {screen_name}' )
    uri = f'https://twitter.com/{screen_name}/with_replies'
    
    payload = {'self': uri, 'tweets': []}
    browser_dets['page'].goto(uri)

    tweet_ids = get_tweet_ids_user_timeline_page( screen_name, browser_dets['page'], max_tweets )
    payload['tweets'] = paral_rehydrate_tweets(tweet_ids)

    return payload

def stream_tweets(browser_dets, query, max_tweets=20):

    query = query.strip()
    if( max_tweets < 0  or len(browser_dets) == 0 or query == '' ):
        return {}

    print('\nstream_tweets():')
    uri = 'https://twitter.com/search?q=' + quote_plus(query) + '&f=live&src=typd'
    
    payload = {'self': uri, 'tweets': []}
    browser_dets['page'].goto(uri)
    
    get_tweet_ids_user_timeline_page( '', browser_dets['page'], max_tweets )
    
def get_auth_twitter_pg(playwright, callback_uri=''):
    
    print('\nget_auth_twitter_pg()')

    chromium = playwright.firefox #"chromium" or "firefox" or "webkit".
    browser = chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    
    sleep_seconds = 3
    page.goto('https://twitter.com/login')
    
    while( True ):

        print(f'\twaiting for login, sleeping for {sleep_seconds} seconds')
        
        time.sleep(sleep_seconds)
        page_html = page.content()
        page_links = getLinks(uri='', html=page_html, fromMainTextFlag=False)
        scroll_down(page)

        if( is_twitter_user_auth(page_links, page.url) ):
            
            print('\tauthenticated')
            if( callback_uri != '' ):
                page.goto(callback_uri)
                print(f'\tauthenticated, loaded {callback_uri}')
                
            print('\tsleeping for 3 seconds')
            time.sleep(3)
            return {
                'page': page,
                'context': context,
                'browser': browser
            }
    
    return {}

def main():
    
    if( len(sys.argv) != 3 ):
        print(f'Usage example:\n\tpython {sys.argv[0]} "williamsburg" 20')
        return
   
    with sync_playwright() as playwright:
        
        browser_dets = get_auth_twitter_pg(playwright)
        if( len(browser_dets) == 0 ):
            return
        
        stream_tweets(browser_dets, sys.argv[1], max_tweets=int(sys.argv[2]))

if __name__ == "__main__":

    main()

```

```
            if 'urls' in tweet_obj.get('entities', []):
                for link in tweet_obj['entities']['urls']:
                    print(link['expanded_url'])
                    if 'twitter.com' not in link['expanded_url'] and 'soundcloud.com' not in link['expanded_url'] and 'twitch.com' not in link['expanded_url']:
                        with open('my2.txt', 'a') as file:
                            file.writelines(link['expanded_url'] + '\n')
```
From the command line:


```
(base) xi@Sophias-MacBook-Air-4 data440 % grep -Eo 'https?://[^ ]{50,}' my.txt | sort -u > new.txt 

```
## Discussion



In order to create a Python program that will allow me to extract links from Twitter tweets, I used the given codes from scrape_twitter_v2.py and added some of my code to extract links from the tweet objects generated from running the whole program. First, I referenced the python program from process_tweets.py and based my codes from that file; I checked to see if URLs were contained in the tweet obj, and if they were, checked if links such as 'twitter.com', 'twitch.com', 'soundcloud.com' are the URLs. I made a condition so that this loop could only return the links that do not contain these words. After that, I opened a file appended all of the URLs in a new Txt file, and saved them for later use. 

I then used requests and Linux commands to extract only the long unique links from the file. After many couple tries, I found that the command: grep -Eo 'https?://[^ ]{50,}' my.txt | sort -u > new.txt works the best at completing this task. I then saved that file into my directory by using > new.txt. 

I have also tried to write a Python program that could do this task, but it was not successful at extracting only the long links. Thus, I used these Linux commands. 


This is what my python codes consisted of:

```

import re
import requests
with open("recent2.txt", "r") as file:
    contents3 = file.read()
x = contents3
def Convert(string):
    li = list(string.split(","))
    return li
re_ex = r'(https?://)'
result = re.sub(re_ex , r',\1', x)
result = result.replace(',', '', 1)
x2 = Convert(result)
x_list = [i[:-2] for i in x2 if i.endswith('\n')]
i_list = []
for i in x_list:
    print(i)
    i_r = requests.get(i, timeout=20)
    if i_r.status_code == requests.codes.ok:
        i_list.append(i) # to get the list of resolved URIs 
        # i then coped the list of URIs in a txt file for future uses

```

Since I was experimenting with all sorts of techniques, I wanted to save each trial in a different file, thus there are several differently named variables. Additionally, there were some instances when the Twitter page could not load after scrolling to fetch a large amount of links. For example, I noticed that sometimes when I ran the the program to find 2000 tweets for tweets containing the word "country", the program could only extract much less than the requested amount. After this, when trying again to fetch more links, Twitter was not responsive. This entire process was very time-consuming and I could only extract around 300 links out of 1000 assigned in this task. 

This was what I saw when I wanted to get a large amount of links from twitter in one sitting: 
![Alt text](image-1.png)

As a result of this, it took me longer than expected to make progress on this task.

## Q2 

Obtain the TimeMaps for each of the unique URIs from Q1 using the ODU Memento Aggregator, MemGator.


You may use https://memgator.cs.odu.edu for limited testing, but do not request all of your 1000 TimeMaps from memgator.cs.odu.edu.


There are two options for running MemGator locally:

   - Install a stand-alone version of MemGator on your own machine, see https://github.com/oduwsdl/MemGator/releases

      - This was described in How to Install MemGator

   - Install Docker Desktop and run MemGator as a Docker Container, see notes at https://github.com/oduwsdl/MemGator/blob/master/README.md



Important: Obtaining TimeMaps requires contacting several different web archives for each URI-R. This process will take time. Look at the MemGator options and figure out how to process the output before running the entire process. You might want to get JSON output, or you might want to limit to the top k archives (especially if there's one that's currently taking a long time to return).

Note that if there are no mementos for a URI-R, MemGator will return nothing. Don't be surprised if many of your URI-Rs return 0 mementos. Remember the "How Much of the Web is Archived" slides -- there are lots of things on the web that are not archived. If you want to do a sanity check on a few, you can manually use the Wayback Machine and see what you get from the Internet Archive. (Remember though that MemGator is going to query several web archives, not just Internet Archive.)

If you uncover TimeMaps that are very large (e.g., for popular sites like https://www.cnn.com/) and swamp your filesystem, you have two options:

   - Manually remove those URI-Rs from your dataset (but note this in your report), or

   - Compress each TimeMap file individually (using pipe to gzip in the same command when downloading or after the download is completed). These compressed files can be used for further analysis by decompressing on the fly using commands like zcat or zless (or using gzip libraries in Python).

Finally, upload the TimeMaps to your GitHub repo -- you'll also use these for Q3. Put them in a separate folder, not the same folder as your report.

   - To upload/commit a large number of files to GitHub, use the command line.

## Discussion

*You must provide some discussion of every answer. Discuss how you arrived at the answer and the tools you used. Discuss the implications of your answer.*


## Q3. Analyze Mementos Per URI-R. (2 points)

Use the TimeMaps you saved in Q2 to analyze how well the URIs you collected in Q1 are archived. Create a table showing how many URI-Rs have certain number of mementos. For example:

|Mementos|URI-Rs
|:---|:---|
|0|750|
|1|100|
|7|50|
|12|25|
|19|25|
|24|20|
|30|27|
|57|3|

If you are using LaTeX, you should create a LaTeX table -- don't submit a spreadsheet or image of a table created in something else. If you are using Markdown, you can view the source of this file for an example of how to generate a table.

If you will end up with a very large table of memento counts, you can bin the number of mementos. Just make sure that the bin sizes are reasonable and that you specify how many had 0 mementos individually. The target is to have no more than 15-20 rows so that your table can fit on a single page. For example


|Mementos|URI-Rs
|:---|:---|
|0|750|
|1-10|150|
|11-20|50|
|21-30|47|
|57|3|


Q: What URI-Rs had the most mementos? Did that surprise you?


## Discussion

*You must provide some discussion of every answer. Discuss how you arrived at the answer and the tools you used. Discuss the implications of your answer.*

## Q4. Analyze Datetimes of Mementos. (2 points)

For each of the URI-Rs from Q3 that had > 0 mementos, create a scatterplot with the age of each URI-R (today - earliest memento datetime) on the x-axis and number of mementos for that URI-R on the y-axis. Some Info Vis terminology: for this graph, the item is the URI-R and the attributes are the estimated age of the URI-R (channel is horizontal position) and the number of mementos for that URI-R (channel is vertical position).


![Alt text](image.png)

This scatterplot should be created using either R or Python, not Excel.

Q: What can you say about the relationship between the age of a URI-R and the number of its mementos?

Q: What URI-R had the oldest memento? Did that surprise you?

Q: How many URI-Rs had an age of < 1 week, meaning that their first memento was captured the same week you collected the data?



# References

* How to Sort Text Files in Linux Using the sort Command, <https://www.makeuseof.com/how-to-use-sort-in-linux/#:~:text=Sort%20a%20File%20Numerically,the%20data%20in%20ascending%20order.&text=If%20you%20want%20to%20sort%20in%20descending%20order%2C%20reverse%20the,n%20flag%20in%20the%20command.>

* Pipe, Grep and Sort Command in Linux/Unix with Examples, <https://medium.com/@ayogun/pipe-grep-and-sort-command-in-linux-unix-with-examples-b53e6dd27ac0>

* Python append to a file <https://www.geeksforgeeks.org/python-append-to-a-file/>

* 15 Practical Grep Command Examples In Linux / UNIX <https://www.thegeekstuff.com/2009/03/15-practical-unix-grep-command-examples/>

* Regular Expression in grep <https://www.geeksforgeeks.org/regular-expression-grep/>

* Quickstart <https://docs.python-requests.org/en/latest/user/quickstart/#timeouts>

* Get Final URL After a Redirect <https://www.baeldung.com/linux/url-after-redirect>

* What Is an RTF File, and How Do I Open One? <https://www.howtogeek.com/358854/what-is-an-rtf-file-and-how-do-i-open-one/>




