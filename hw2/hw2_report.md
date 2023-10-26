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

Given the provided program, scrape_twitter_v2.py, I made additions in the def get_tweet_ids_user_timeline_page(screen_name, page, max_tweets) to extract extended URLs from the tweets pulled. This file is uploaded to this assignment's folder. 

```

logged_in_links = ['https://twitter.com/home', 'https://t.co/']

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

```

```
            if 'urls' in tweet_obj.get('entities', []):
                for link in tweet_obj['entities']['urls']:
                    print(link['expanded_url'])
                    if 'twitter.com' not in link['expanded_url'] and 'soundcloud.com' not in link['expanded_url'] and 'twitch.com' not in link['expanded_url']:
                        with open('my2.txt', 'a') as file:
                            file.writelines(link['expanded_url'] + '\n')
```

From the command line: (In order to extract the unique tweets out of all the tweets extracted), I used this command:

```
(base) xi@Sophias-MacBook-Air-4 data440 % grep -Eo 'https?://[^ ]{50,}' my.txt | sort -u > new.txt 

```
Grep extracts the long links and sort extracts the unique links and sorts it in a txt file. I have relabled my file that contains 1000 links called my_1000links.txt

## Discussion


To create a Python program that will allow me to extract links from Twitter tweets, I used the given codes from scrape_twitter_v2.py and added some of my code to remove links from the tweet objects generated from running the whole program. First, I referenced the Python program from process_tweets.py and based my code on that file; I checked to see if URIs were contained in the tweet object, and if they were, I checked if links such as 'twitter.com,' 'twitch.com', 'soundcloud.com' are the URLs. I made a condition so that this loop could only return the links that do not contain these words. After that, I opened a file, appended all the URLs in a new .txt file, and saved them for later use. 

The Python program is called scrape_twitter_v2.py, and it is saved in the folder of this assignment. 

I then used requests and Linux commands to extract only the long, unique links from the file. After many couple tries, I found that the command: grep -Eo 'https?://[^ ]{50,}' my.txt | sort -u > new.txt works the best at completing this task. I then saved that file into my directory by using > new.txt. 

I have also tried to write a Python program that could do this task, but it was unsuccessful at extracting only the long links. Thus, I used these Linux commands. 


This is what my Python program consisted of:

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
This technique did not work in my Jupyter notebook, so I used Linux commands instead.

Since I was experimenting with various techniques, I wanted to save each trial in a different file; thus, there are several differently named variables. Additionally, there were some instances when the Twitter page could not load after scrolling to fetch many links. For example, I noticed that sometimes, when I ran the the program to find 2000 tweets for tweets containing the word "country", the program could only extract much less than the requested amount. After this, when trying again to fetch more links, Twitter was not responsive. This entire process was very time-consuming, and I could only extract around 300 links out of 1000 assigned in this task. 

This was what I saw when I wanted to get a large amount of links from Twitter in one sitting: 

![\label{fig:twitter}](https://github.com/schen8180/data440/blob/main/hw2/hw2_pic1.png?raw=true)

Additionally, after twitter provides me with this message I ussually cannot immediately run the program right after or the message will still be there. Thus, to resolve this, I had to wait for a an small amount of time before I could use the program again. As a result of this, it took me longer than expected to make progress on this task. 

Moreover, the twitter webpage is more likely to stop running after minimize the window, so I have to keep the webpage open when I am running it. 

### Update (10/19):
After professor Nwala advised me to use two seperate twitter accounts to collect tweets, I was able to extract the links from tweets at a much faster rate. I finally collected 1000 links. 

I also manually removed the links that refernce a video as my function that I wrote does not seem to be able to exclude these links. I used the command f property in my mac to do this. 


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


## Answer and Discussion
I had to download the memgator and edit the access using Linux commands to complete this task. At first, I could not perform test commands due to my lack of access to execute memgator. After consulting with the web and Professor Nwala, I changed the type of access I was initially allowed. The commands I used to change the file permissions to gain access to execute the file were ls -l. I typed this command onto my terminal, followed by the file I was working on. After returning those commands and changing the permissions to read, write, and execute the file, I could further proceed along the task.

This is an example of what the output is after using the memgator command for one of my URIs:
```
(base) xi@Sophias-MacBook-Air-4 Downloads % ./memgator-darwin-amd64 -F 2 -f JSON "https://wydaily.com/news/local/2023/10/11/tour-de-midnight-bike-ride-rolls-to-williamsburg-for-epilepsy-awareness/"
{
  "original_uri": "https://wydaily.com/news/local/2023/10/11/tour-de-midnight-bike-ride-rolls-to-williamsburg-for-epilepsy-awareness/",
  "self": "http://localhost:1208/timemap/json/https://wydaily.com/news/local/2023/10/11/tour-de-midnight-bike-ride-rolls-to-williamsburg-for-epilepsy-awareness/",
  "mementos": {
    "list": [
      {
        "datetime": "2023-10-11T15:03:48Z",
        "uri": "https://web.archive.org/web/20231011150348/https://wydaily.com/news/local/2023/10/11/tour-de-midnight-bike-ride-rolls-to-williamsburg-for-epilepsy-awareness/"
      },
      {
        "datetime": "2023-10-13T20:38:42Z",
        "uri": "https://web.archive.org/web/20231013203842/https://wydaily.com/news/local/2023/10/11/tour-de-midnight-bike-ride-rolls-to-williamsburg-for-epilepsy-awareness/"
      }
    ],
    "first": {
      "datetime": "2023-10-11T15:03:48Z",
      "uri": "https://web.archive.org/web/20231011150348/https://wydaily.com/news/local/2023/10/11/tour-de-midnight-bike-ride-rolls-to-williamsburg-for-epilepsy-awareness/"
    },
    "last": {
      "datetime": "2023-10-13T20:38:42Z",
      "uri": "https://web.archive.org/web/20231013203842/https://wydaily.com/news/local/2023/10/11/tour-de-midnight-bike-ride-rolls-to-williamsburg-for-epilepsy-awareness/"
    }
  },
  "timemap_uri": {
    "link_format": "http://localhost:1208/timemap/link/https://wydaily.com/news/local/2023/10/11/tour-de-midnight-bike-ride-rolls-to-williamsburg-for-epilepsy-awareness/",
    "json_format": "http://localhost:1208/timemap/json/https://wydaily.com/news/local/2023/10/11/tour-de-midnight-bike-ride-rolls-to-williamsburg-for-epilepsy-awareness/",
    "cdxj_format": "http://localhost:1208/timemap/cdxj/https://wydaily.com/news/local/2023/10/11/tour-de-midnight-bike-ride-rolls-to-williamsburg-for-epilepsy-awareness/"
  },
  "timegate_uri": "http://localhost:1208/timegate/https://wydaily.com/news/local/2023/10/11/tour-de-midnight-bike-ride-rolls-to-williamsburg-for-epilepsy-awareness/"
}

```

It is best and more convenient to create a program that can automate collecting each link from the file of 1000 links, running the memgator-darwin-amd64 command for each link, and storing them in a separate file in my folder. Doing this all by myself was difficult, so I went to TA hours and asked questions, worked with friends, and consulted with the web. They were beneficial to me.

I first created a function that takes in the parameters URI and counter.
Following that, I created a try block and except block. 
Inside the try block, I used Python's built-in subprocess.check_out() function to check if the format that appears after running the memgator command is "./memgator-darwin-amd64","-F","2","-f","JSON" followed by the requested URI.

After that, I saved each URI into a file and stored it in a variable called output_file

The except blocks catch the errors that appear so that Python would not stop and crash when an error occurs. 

Next, I created a loop that iterates through the URIs and made a new file for each URI. 

I also noticed that only a few of my links have a time map showing that there more recently created web pages compared to older sites.

The program is stored in part2.py, and the .json files that contain the time maps are stored in a file named hw2file. This file is zipped in a file called my_archive.tar.gz. 

This process took approxiamately eight hours. 



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

If you will end up with a very large table of memento counts, you can bin the number of mementos. Just make sure that the bin sizes are reasonable and that you specify how many had 0 mementos individually. The target is to have no more than 15-20 rows so that your table can fit on a single page.

Q: What URI-Rs had the most mementos? Did that surprise you?

A: 

News sources have the most momentos, this did not surprise me.

|Mementos|URI-Rs
|:---|:---|
|0|513|
|1-10|58|
|11-20|13|
|21-30|7|
|31-40|5|
|41-50|2|
|51-60|1|
|61-70|1|
|71-80|2|
|81-90|0|
|91-100|3|
|101-200|1|
|201-300|1|
|301-400|2|
|401-500|0|
|501-600|1|


## Discussion

To complete this task, I created a function that measures each memgator count for each json file. 

This is the code snippet: 

def memgator_count(file):
    try:
        directory  = file
        for filename in os.listdir(directory):
            with open(filename) as file:
                data = json.load(file)
                count = 0
                for i in data['mementos']['list']:
                    count +=1
                print(count) 
    except FileNotFoundError:
        print("file is not found")
    print(len(os.listdir(directory))) # gets the count 

memgator_count("hw2files") # will print out the counts for each .json file that contain mementos. 

Using this function memgator_count("hw2files"), it prints out the total number of memgators for each file. These numbers are stored in the table above.  

## Q4. Analyze Datetimes of Mementos. (2 points)

For each of the URI-Rs from Q3 that had > 0 mementos, create a scatterplot with the age of each URI-R (today - earliest memento datetime) on the x-axis and number of mementos for that URI-R on the y-axis. Some Info Vis terminology: for this graph, the item is the URI-R and the attributes are the estimated age of the URI-R (channel is horizontal position) and the number of mementos for that URI-R (channel is vertical position).


![Alt text](image.png)

This scatterplot should be created using either R or Python, not Excel.

This is the code I wrote to collect data for the scatterplot:

```


directory  = "hw2files"
for filename in os.listdir(directory):
    with open(filename) as file:

        data = json.load(file)
        count = 0
        my = []
        for i in data['mementos']['list']:
            #my = []
            test_dict = i
            #print(test_dict)
            #print(test_dict.get('datetime')) # gets the times for each timemap file
            times = test_dict.get('datetime')
            new_format = times[:-10]
            #print(new_format)
            time_s = datetime.fromisoformat(new_format)
            my.append(time_s)
            count +=1
            early = min(my)
        #print(datetime.now())
        #print(early)
        now = datetime.now() - early
        print(now)
        print(count)

```

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

* Manipulating text at the command line with grep <https://www.redhat.com/sysadmin/manipulating-text-grep>

* Permission denied in Mac Terminal? Try this fix <https://macpaw.com/how-to/permission-denied-terminal#:~:text=You%20can%20usually%20fix%20it,you%20have%20formatted%20commands%20correctly.>

* How to Append Contents of Multiple Files Into One File on Linux? <https://www.tutorialspoint.com/how-to-append-contents-of-multiple-files-into-one-file-on-linux#:~:text=Method%201%3A%20Use%20the%20cat%20command&text=The%20%22%3E%3E%22%20operator%20adds,additional%20files%20to%20the%20command.>

* Python String format() Method <https://www.w3schools.com/python/ref_string_format.asp>

* What does %s mean in a Python format string? <https://www.geeksforgeeks.org/what-does-s-mean-in-a-python-format-string/#>

* An Introduction to Subprocess in Python With Examples <https://www.simplilearn.com/tutorials/python-tutorial/subprocess-in-python>

* Python Try Except <https://www.w3schools.com/python/python_try_except.asp>

* Python datetime module <https://www.geeksforgeeks.org/python-datetime-module/>

* datetime — Basic date and time types <https://docs.python.org/3/library/datetime.html>










