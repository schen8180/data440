# HW1 - Web Science Intro
### Sophia Chen
### DS 440, Fall 2023
### Sep 26, 2023

# Q1 

Consider the "bow-tie" structure of the web in the Broder et al. paper "Graph Structure in the Web" that was described in Module 1.

Now consider the following links:


```
A --> B
B --> C
C --> D
C --> A
C --> G
E --> F
G --> C
G --> H
I --> H
I --> K
L --> D
M --> A
M --> N
N --> D
O --> A
P --> G 
```

Draw the resulting directed graph (either sketch on paper or use another tool) showing how the nodes are connected to each other and include an image in your report. This does not need to fit into the bow-tie type diagram, but should look more similar to the graph on slide 27 from Module-01 Web-Science-Architecture.

For the graph, list the nodes (in alphabetical order) that are each of the following categories:

- SCC:
- IN:
- OUT:
- Tendrils:
    - indicate if the tendril is reachable from IN or can reach OUT
- Tubes:
    - explain how the nodes serve as tubes
- Disconnected:

## Answer

![\label{fig:bow-tie}](https://raw.githubusercontent.com/schen8180/data440/main/hw1/SCChw1.jpg?token=GHSAT0AAAAAACHJXMY4VI3JQBCGYKMNJPFOZITJQ4Q)


- SCC: A, B, C, G
- IN: P, M, O
- OUT: D, H
- Tendrils: I, L, K; 

I and L are reachable from IN, and K can reach out. 
- Tubes: N; 

This node served as a tube by only being connected with the in component and out component. 
- Disconnected: E, F

## Discussion


By looking at the PowerPoint slides, reading the Piazza discussions, and doing online research for to commplete this question, I read more about the bow-tie structure of the web. I reviewed how there are three main components that make up the structure of the web graph: the SCC, or strongly connected component, a set of IN components, and a set of OUT components. 

In this chart below, there are five different components that create this specifc bow-tie structure: the IN, SCC, OUT, Tube, the disconnected, and tentril components. The IN components are: P, M, O. This is because these nodes are connected to the SCC nodes.
The SCC components are: A, B, C, G. These nodes are be reach back to each other through directed links. 
The OUT components are D and H, where they are able to reach out to other nodes. 
The tube is node N because that is the only node that is connected from an IN node to OUT node. 
The disconnected nodes are the E and F nodes where they are only connected to themselves and not with the other nodes. 
The tentrils are I, L, and K because two satisfy the two conditions of a tentril, which are the nodes reachable from IN cannot reach the SCC nodes, and the nodes that can reach out cannot be reach from the SCC nodes. 

# Q2
Demonstrate that you know how to use curl and are familiar with the available options.

a)  First, load this URI https://httpbin.org/user-agent directly in your browser and take a screenshot. The resulting webpage should show the "User-Agent" HTTP request header that your web browser sends to the web server.

b) In a single curl command, issue a HEAD HTTP request for the URI, https://t.co/KSHFYLmmB0. Show the HTTP response headers, follow any redirects, and change the User-Agent HTTP request field to "DATA 440." Show the command you issued and the result of your execution on the command line. (Either take a screenshot of your terminal or copy/paste into a code segment.)

Briefly explain the results you get for each of these steps.
## Answer

## a)
```
{
     "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
}

```

## b)
```
Last login: Tue Sep 26 18:11:14 on ttys000
(base) xi@Sophias-MacBook-Air-4 ~ % curl -L -I -A "DATA 440" https://t.co/KSHFYLmmB0
HTTP/1.1 301 Moved Permanently
date: Fri, 29 Sep 2023 02:32:24 GMT
perf: 7626143928
vary: Origin
server: tsa_b
expires: Fri, 29 Sep 2023 02:37:25 GMT
location: https://www.theguardian.com/books/2022/dec/04/our-mission-is-crucial-meet-the-warrior-librarians-of-ukraine
set-cookie: muc=5110befb-18c2-4239-9db9-5ee273f367d0; Max-Age=63072000; Expires=Sun, 28 Sep 2025 02:32:25 GMT; Domain=t.co; Secure; SameSite=None
set-cookie: muc_ads=5110befb-18c2-4239-9db9-5ee273f367d0; Max-Age=63072000; Expires=Sun, 28 Sep 2025 02:32:25 GMT; Path=/; Domain=t.co; Secure; SameSite=None
cache-control: private,max-age=300
x-transaction-id: 0d68def00df44039
strict-transport-security: max-age=0
x-response-time: 17
x-connection-hash: e9d2a9aa587e2d7d10034b04c10b2143835f5c66efc12ccd16ee3e8cff185c88
transfer-encoding: chunked

HTTP/1.1 200 OK
Connection: keep-alive
Content-Length: 313461
onion-location: https://www.guardian2zotagl6tmjucg3lrhxdk4dw3lhbqnkvvkywawy3oqfoprid.onion/books/2022/dec/04/our-mission-is-crucial-meet-the-warrior-librarians-of-ukraine
x-gu-frontend-git-commit-id: e93bc211dc6dd2350e9c6bb5c591531afef32426
link: <https://assets.guim.co.uk/polyfill.io/v3/polyfill.min.js?rum=0&features=es6%2Ces7%2Ces2017%2Ces2018%2Ces2019%2Cdefault-3.6%2CHTMLPictureElement%2CIntersectionObserver%2CIntersectionObserverEntry%2CURLSearchParams%2Cfetch%2CNodeList.prototype.forEach%2Cnavigator.sendBeacon%2Cperformance.now%2CPromise.allSettled&flags=gated&callback=guardianPolyfilled&unknown=polyfill&cacheClear=1&http3=true>; rel=prefetch,<https://assets.guim.co.uk/assets/frameworks.web.3c870acd254123292ad1.js?http3=true>; rel=prefetch,<https://assets.guim.co.uk/assets/index.web.31524e6437c54fd2506c.js?http3=true>; rel=prefetch,<https://assets.guim.co.uk/javascripts/commercial/88af4895df42fce21b6d/graun.standalone.commercial.js?http3=true>; rel=prefetch,,<https://assets.guim.co.uk/>; rel=preconnect,<https://i.guim.co.uk>; rel=preconnect,<https://j.ophan.co.uk>; rel=preconnect,<https://ophan.theguardian.com>; rel=preconnect,<https://api.nextgen.guardianapps.co.uk>; rel=preconnect,<https://hits-secure.theguardian.com>; rel=preconnect,<https://interactive.guim.co.uk>; rel=preconnect,<https://phar.gu-web.net>; rel=preconnect,<https://static.theguardian.com>; rel=preconnect,<https://support.theguardian.com>; rel=preconnect
etag: W/"hash-3018644980948850151"
x-gu-dotcomponents: true
content-type: text/html; charset=UTF-8
Accept-Ranges: bytes
Date: Fri, 29 Sep 2023 02:32:25 GMT
Age: 0
Set-Cookie: GU_mvt_id=190368; expires=Thu, 28 Dec 2023 02:32:25 GMT; path=/; domain=.theguardian.com; Secure
X-Timer: S1695954745.390155,VS0,VE238
Strict-Transport-Security: max-age=63072000; includeSubDomains; preload
X-Frame-Options: SAMEORIGIN
X-XSS-Protection: 1; mode=block
X-Content-Type-Options: nosniff
Content-Security-Policy: default-src https:; script-src https: 'unsafe-inline' 'unsafe-eval' blob: 'unsafe-inline'; frame-src https: data:; style-src https: 'unsafe-inline'; img-src https: data: blob:; media-src https: data: blob:; font-src https: data:; connect-src https: wss: blob:; child-src https: blob:; object-src 'none'; base-uri 'none'
Referrer-Policy: no-referrer-when-downgrade
Feature-Policy: camera 'none'; microphone 'none'; midi 'none'; geolocation 'none'
Permissions-Policy: camera=(), microphone=(), midi=(), geolocation=(), interest-cohort=()
X-GU-Edition: us
Cache-Control: max-age=60, stale-while-revalidate=6, stale-if-error=864000, private,no-transform
Vary: Accept-Encoding,User-Agent
Set-Cookie: GU_geo_country=US; path=/; Secure

```
## Discussion
In this part of the exercise, I browsed the web and experimented with the command link to search for a way to make a single line multiple curl commands. 
I discovered that to make curl commands on a single line, I simply need to issue the requests all together at once on a line beside the given URI in my terminal. The L command allows curl to follow redirects up to 500 times, the I command helps curl make a HEAD request. The -A option helps curl change the user agent name. In this case, the tasks are: issue a HEAD HTTP request, follow redirects, and change the user-agent to "DATA 440" for the link, https://t.co/KSHFYLmmB0
HTTP. Thus, the curl command in the terminal would be: curl -L -I -A "DATA 440" https://t.co/KSHFYLmmB0. 



# Q3
Write a Python program to find links to PDFs in a webpage.

Your program must do the following:

- take the URI of a webpage as a command-line argument
- extract all the links from the page
- for each link, request the URI and use the Content-Type HTTP response header to determine if the link references a PDF file
- for all links that reference a PDF file, print the original URI (found in the parent HTML page), the final URI (after any redirects), and the number of bytes in the PDF file. (Hint: Content-Length HTTP response header)

Here is a snippet of the expected operation:

```
% python3 get_pdfs.py https://alexandernwala.com/files/teaching/fall-2022/week-2/2018_wsdl_publications.html

URI: http://www.cs.odu.edu/~mln/pubs/ht-2018/hypertext-2018-nwala-bootstrapping.pdf
Final URI: https://www.cs.odu.edu/~mln/pubs/ht-2018/hypertext-2018-nwala-bootstrapping.pdf
Content Length: 994,153 bytes

URI: http://www.cs.odu.edu/~mln/pubs/ipres-2018/ipres-2018-atkins-news-similarity.pdf
Final URI: https://www.cs.odu.edu/~mln/pubs/ipres-2018/ipres-2018-atkins-news-similarity.pdf
Content Length: 18,995,885 bytes

```

Show that the program works on 3 different URIs, one of which must be https://alexandernwala.com/files/teaching/fall-2022/week-2/2018_wsdl_publications.html, which contains 8 links to PDFs.

- Many W&M DS faculty members have a list of their publications in PDF form on their webpages. You may search their webpages for URIs to use.
- Also, there are a set of pages linked on our DATA 440 Syllabus that say "pdf available". If you follow some of those links, you'll likely find a page that links to at least one PDF.

You will likely want to use the BeautifulSoup Python library for this question. Run pip3 install beautifulsoup4 to install BeautifulSoup4. I highly recommend that you install Python packages inside your Python virtual environment:

```
$ python3 -m venv p3_env     # Creates a Python 3 virtual environment in a directory called p3_env
$ source p3_env/bin/activate # Activates your Python 3 virtual environment. All new packages will be installed in py_env

$ which python               # Shows the path of your virtual env's Python
$ deactivate                 # Deactivates your Python virtual environment

```
## Answer

```

import requests
from bs4 import BeautifulSoup

def get_pdf(link, org_uri): 
    response = requests.get(link, allow_redirects = True)
    final_uri = response.url 
    content_type = response.headers.get("Content-Type", "")
    is_pdf = content_type.lower().startswith("application/pdf")
    pdf_size = len(response.content) 
    print(f"Parent URI: {org_uri}") 
    print(f"Final URI: {final_uri}") 
    print(f"Is PDF: {is_pdf}")
    print(f"PDF Size (bytes): {pdf_size}\n")
def web_scraper(user_url):  
    url = user_url 
    response = requests.get(url) 
    soup = BeautifulSoup(response.text, "html.parser") 
    links = soup.find_all('a') 
    for i in links: 
        href = i.get("href") 
        if href and not href.startswith("#") and not href.startswith("mailto:") and not href.startswith("javascript:"):
            link = href 
            if link.lower().endswith("pdf"): 
                get_pdf(link,url)

```

## Discussion
To answer this question, I created two functions: get_pdf() and web_scraper() functions. The first function takes in two parameters, the link parameter and the org_uri, or the original uri parameter. The purpose of this was to take in the original uri, and the final uri in order to determine whether or not a pdf exists. First, I used the requests.get() python function to return the response object and check the status code of the link. I assigned this to a variable called response. After that, I used .url() to response in order to fetch the URL. Towards the end of the code for this get_pdf() function, I checked whether or not a pdf exists by using built in python functions to confirm that the word "application/pdf" is in the uri. 
After creating this function, I created another function called web_scraper() that takes in a parameter called user_url. This parameter later gets parsed into the library Beautiful Soup to assist with pulling data out of HTML files. I then assigned this to a variable called soup. Then I used the built in function, find_all(), to find links with a-tags, extracting the hyperlink, which is used to link from one page to another. Following this, I created a for loop that iterates through all these links and extracting the links with the 'href' attribute, which specifies the URL of the page the link is connected to. I created a condition to check if the links' names start with "#", "mailto:", "javascript". If they do not contain these words I called them to a variable named link.  Then I checked if the word "pdf" is in the link and used the get_pdf() function to return the link and orignal url. By testing it with the link, "https://alexandernwala.com/files/teaching/fall-2022/week-2/2018_wsdl_publications.html,", and seeing that it prints out 8 pdf links, I could see that it works for this exercise. 
```
web_scraper(link)


URI: https://www.cs.odu.edu/~mln/pubs/ht-2018/hypertext-2018-nwala-bootstrapping.pdf
Final URI: https://www.cs.odu.edu/~mln/pubs/ht-2018/hypertext-2018-nwala-bootstrapping.pdf
Content Length: 994153 bytes 

URI: https://www.cs.odu.edu/~mln/pubs/ipres-2018/ipres-2018-atkins-news-similarity.pdf
Final URI: https://www.cs.odu.edu/~mln/pubs/ipres-2018/ipres-2018-atkins-news-similarity.pdf
Content Length: 18995885 bytes 

URI: https://www.cs.odu.edu/~mln/pubs/ipres-2018/ipres-2018-jones-off-topic.pdf
Final URI: https://www.cs.odu.edu/~mln/pubs/ipres-2018/ipres-2018-jones-off-topic.pdf
Content Length: 3119205 bytes 

URI: https://www.cs.odu.edu/~mln/pubs/ipres-2018/ipres-2018-jones-archiveit.pdf
Final URI: https://www.cs.odu.edu/~mln/pubs/ipres-2018/ipres-2018-jones-archiveit.pdf
Content Length: 2639215 bytes 

URI: https://www.cs.odu.edu/~mln/pubs/jcdl-2018/jcdl-2018-nwala-scraping-serps-seeds.pdf
Final URI: https://www.cs.odu.edu/~mln/pubs/jcdl-2018/jcdl-2018-nwala-scraping-serps-seeds.pdf
Content Length: 2172494 bytes 

URI: https://www.cs.odu.edu/~mln/pubs/jcdl-2018/jcdl-2018-kelly-private-public-web-archives.pdf
Final URI: https://www.cs.odu.edu/~mln/pubs/jcdl-2018/jcdl-2018-kelly-private-public-web-archives.pdf
Content Length: 2553579 bytes 

URI: https://www.cs.odu.edu/~mln/pubs/jcdl-2018/jcdl-2018-aturban-archivenow.pdf
Final URI: https://www.cs.odu.edu/~mln/pubs/jcdl-2018/jcdl-2018-aturban-archivenow.pdf
Content Length: 3998654 bytes 

URI: https://www.cs.odu.edu/~mln/pubs/jcdl-2018/jcdl-2018-alam-archive-banner.pdf
Final URI: https://www.cs.odu.edu/~mln/pubs/jcdl-2018/jcdl-2018-alam-archive-banner.pdf
Content Length: 596000 bytes 
```

# References

* <https://www.zenrows.com/blog/curl-user-agent#:~:text=To%20change%20the%20User%2DAgent,the%20desired%20User%2DAgent%20string.>
* <https://medium.com/neo4j/the-world-wide-web-is-like-a-bow-tie-discovering-graph-structure-with-neo4j-5d1b684cd4ee#:~:text=Broder%20and%20his%20colleagues%20classified,giant%20component%20were%20called%20tubes.>
* <https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods>
* <https://blog.finxter.com/3-pythonic-ways-to-download-a-pdf-from-a-url/>
* <https://developer.mozilla.org/en-US/docs/Web/HTTP/Status>
* <https://blog.finxter.com/a-step-by-step-guide-to-fetching-the-url-from-the-href-attribute-using-beautifulsoup/>
* <https://www.w3schools.com/tags/att_a_href.asp>
* <https://www.cs.cornell.edu/home/kleinber/networks-book/networks-book-ch13.pdf>
* <https://www.booleanworld.com/curl-command-tutorial-examples/#google_vignette>