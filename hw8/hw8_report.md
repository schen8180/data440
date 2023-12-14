# Homework 8 - Clustering
### Sophia Chen
### DATA 440, Fall 2023
**Due:** December 7, 2023 by 11:59pm


## Assignment

The goal of this assignment is to cluster Twitter accounts based on the content of their last 200 tweets.
 
**Important:** Much of the code for this assignment is provided for you, therefore, your report must include a high-level description of how the code works and answers to all of the sub-questions asked.

**Report (2 points**)

## Questions

### Q1 - Find Popular Twitter Accounts (2 point)
Generate a list of at least 50 popular accounts on Twitter. The accounts must be verified, have 10,000+ followers, and have 5000+ tweets.  For example:
* [`@acnwala`](https://twitter.com/acnwala) - is not verified, ~440 followers, ~3200 tweets - *don't include*
* [`@williamandmary`](https://twitter.com/williamandmary) - verified (blue checkmark), 35,000+ followers, 9,000+ tweets - *could include*  

Generate this information manually by visiting individual account pages. You only need at least 50 popular accounts.

Because we're trying to cluster the accounts based on the text in their tweets, you should choose several sets of accounts that are similar (political, tech, sports, etc.) to see if they'll get clustered together later.

Save the list of accounts (screen_names), one per line, in a text file named `accounts.txt` and upload to your GitHub repo.

*B: What topics/categories do the accounts belong to?  You don't need to specify a grouping for each account, but what general topics/categories will you expect to be revealed by the clustering? Provide a this list before generating your clusters*

## Answer

The accounts I have found mostly belong to celebrities, politics, tech, education, sports, entertainment, news, and music. 

### Q2 - Create Account-Term Matrix (3 points)

Before we can run the clustering code from the PCI book, we have to build an account-term matrix (like the [blog-term matrix](https://github.com/arthur-e/Programming-Collective-Intelligence/blob/master/chapter3/blogdata.txt) in the Module 12 slides). Consider the Twitter accounts equivalent to blogs, and all account tweets, the words of the blog.

The PCI book provided code for creating the blog-term matrix given a list of blog feeds. I've provided similar code originally written by Dr. Michele Weigle in 2021 and modified my me in 2023:
* [tweet_parser.py](tweet_parser.py) - This is similar to the feedparser library mentioned on pg. 31.  It contains the `parse()` function:
    * `parse(browser_dets, screen_name, num_tweets=50)` - use playwright to scrape Twitter and download about 50 tweets from the timeline of the `screen_name` account and return a dictionary with the following structure:   
    `{'screen_name': screen_name, 'tweets': [tweet 1 text, tweet 2 text, ...]}`

* [generate_tweet_vector.py](generate_tweet_vector.py) - This is similar to [`generatefeedvector.py`](https://github.com/arthur-e/Programming-Collective-Intelligence/blob/master/chapter3/generatefeedvector.py) described on pgs. 31-33 in PCI.  It contains main code and two functions:
    * `getwordcounts(api, screen_name)` - calls `parse()` from `tweet_parser.py` and returns the screen_name and a dictionary of word counts appearing in that account's tweets, almost exactly like `getwordcounts()` in our examples
    * `getwords(tweet)` - takes a tweet and returns a filtered list of words, similar to `getwords()` in our examples, but with some added filtering:
        * removes URLs
        * removes screen names (starting with @)
        * splits words by non-alphabetic characters (and thus removes any numbers and symbols)
        * removes any words < 3 characters or > 15 characters
        * lowercases all words

`generate_tweet_vector.py` requires that you have `accounts.txt` (from Q1) and `tweet_parser.py` located in the same folder.  

`generate_tweet_vector.py` will ***not work out-of-the-box***.  
* Instead of creating an account-term matrix for every term in the tweets, I only want the 500 most popular terms that are not stopwords.  ***You will need to write this code.***  To help with this, I've added a `sumcounts` dict that holds the words and frequency of those words over all accounts and a blank list `popularlist` where you should store the 500 most frequent non-stopword terms. On line 88, you'll see a section labeled `# BEGIN YOUR CODE BLOCK`. This is where you'll add your code.

Once complete, `generate_tweet_vector.py` will produce two files that you need to upload to your GitHub repo:
* `popular_terms.txt` - the list (one per line) of the 500 most frequent terms in the tweets
* `tweet_term_matrix.txt` - the generated account-term matrix

Once `tweet_term_matrix.txt` has been generated, you can use it in place of `blogdata.txt` in the example code to complete the remaining parts of this assignment.

*A: Explain the general operation of generate_tweet_vector.py and how the tweets are converted to the account-term matrix.*

*B: Explain in detail the code that you added to filter for the 500 most frequent non-stopword terms.*

*C: Do the 500 most frequent terms make sense based on the accounts that you chose?*

## Answer

*A
The general operation of generate_tweet_vector.py logs onto Twitter from information given by the user and parses through it to complete tasks that are defined by functions such as write_popular_terms_and_tweet_term_matrix(), write counts (), networks (), etc. These functions also help create new files that store their outputs. 

Tweets are converted to the account-term matrix by iterating through words in the popular list, a list of the 500 most frequent tweet terms, and reporting the number of items each time they are present in the top 50 popular accounts. The open() line creates a file called 'tweet_term_matrix.txt.' The first for-loop iterates over the words in the list of 500 most frequently used terms called popular list and records in the created file.
After that, another iteration is done over an empty dictionary to store the
frequency of each word appearing in the 50 most popular Twitter accounts. After that, an account term matrix is created in a file called 'tweet_term_matrix.txt' that shows the relationship between words in documents. 

*B

The code block that I have created to filter for the 500 most frequent non-stopword terms is shown below: 

```
    # sumcounts is a dictionary
    popularlist = []
    stop_words = set(stopwords.words('english')) # trying to find the stopwords in the english language

    for key, value in sumcounts.items(): #iterate over a key, value pair in dictionary 
        words = str(value).split() 
        filtered_words = [word for word in words if word.lower() not in stop_words] # filtering out the words if they are non-stop words
        sumcounts[key] = ''.join(filtered_words) #add these words into the dictionary 
    sorted_items = sorted(sumcounts.items(), key=lambda x: x[1], reverse=True) #sorting the dictionary in descending order based on word counts
    first_500_largest = sorted_items[:500] #getting the first 500 words 
    keys_only = [item[0] for item in first_500_largest] 
    for i in keys_only:
        popularlist.append(i)
    popularlist

```
In this code, I first created an empty popular list to store the 500 most frequent non-stopword terms later. In addition, after importing a Python module that I can use to find English stopwords, I kept them in a variable called stop_words. 

I created a loop that iterates over key-value pairs inside the sumcounts dictionary. I split the values from their keys and converted them into strings using str().split() to filter them from the stopwords. The ```sumcounts[key] = ''.join(filtered_words)``` line concatenates these new words back into the dictionary. Then, I sorted the words in terms of their frequency by using the sorted() Python function and lambda. The 500 most frequent terms are in the first 500 index positions. Finally, I appended my findings to the popular list I created from the beginning. 

*C

The 500 words make sense from the Twitter accounts that the Python program parsed through. Since my accounts.txt list consists of most celebrities in the entertainment industry, the words my function created made sense. For example, the words Vegas, tickets, special, concert, and artistry align with the nature of the Twitter account I chose for this assignment. 

### Q3 - Create Dendrogram (1 point)
Create an ASCII dendrogram *and* a JPEG dendrogram that uses hierarchical clustering to cluster the most similar accounts (see Module 12, slides 21, 23).  Include the JPEG in your report and upload the ASCII file to GitHub (it will be too unwieldy for inclusion in the report).

*A: How well did the hierarchical clustering do in grouping similar accounts together?  Were there any particularly odd groupings?*

## Answer

The hierarchical clustering did an okay job of grouping similar accounts. 

```
                -
                  -
                    AvrilLavigne
                    -
                      shakira
                      selenagomez
                  -
                    -
                      davidguetta
                      -
                        Oprah
                        Pink
                    -
                      -
                        Eminem
                        -
                          Cristiano
                          KimKardashian
                      -
                        -
                          pitbull
                          -
                            katyperry
                            justinbieber
                        -
                          -
                            aliciakeys
                            Real_Liam_Payne
                          -
                            -
                              KevinHart4real
                              EmWatson
                            -
                              -
                                SrBachchan
                                -
                                  onedirection
                                  BillGates
                              -
                                iamsrk
                                -
                                  zaynmalik
                                  -
                                    aplusk
                                    -
                                      KingJames
                                      LilTunechi
    -
      -
        khloekardashian
        -
          BrunoMars
          KAKA
      -
        kourtneykardash
        -
          Adele
          NiallOfficial


```

### Q4 - Cluster using k-Means (2 points)
Cluster the accounts using k-Means, using `k`=5,10,20 (see Module 12, slide 34).  For each value of `k`, create a file that lists the accounts in each cluster and upload to your GitHub repo.  
```
kclust = kcluster(data, k=10)
Iteration 0
Iteration 1
Iteration 2
Iteration 3
Iteration 4
Iteration 5
Iteration 6
Iteration 7
Iteration 8
Iteration 9
Iteration 10
Iteration 11
Iteration 12
Iteration 13
Iteration 14
Iteration 15
Iteration 16
Iteration 17
Iteration 18
Iteration 19
Iteration 20
Iteration 21
Iteration 22
Iteration 23
Iteration 24
Iteration 25
Iteration 26
Iteration 27
Iteration 28
Iteration 29
Iteration 30
Iteration 31
Iteration 32
Iteration 33
Iteration 34
Iteration 35
Iteration 36
Iteration 37
Iteration 38
Iteration 39
Iteration 40
Iteration 41
Iteration 42
Iteration 43
Iteration 44
Iteration 45
Iteration 46
Iteration 47
Iteration 48
Iteration 49
Iteration 50
Iteration 51
Iteration 52
Iteration 53
Iteration 54
Iteration 55
Iteration 56
Iteration 57
Iteration 58
Iteration 59
Iteration 60
Iteration 61
Iteration 62
Iteration 63
Iteration 64
Iteration 65
Iteration 66
Iteration 67
Iteration 68
Iteration 69
Iteration 70
Iteration 71
Iteration 72
Iteration 73
Iteration 74
Iteration 75
Iteration 76
Iteration 77
Iteration 78
Iteration 79
Iteration 80
Iteration 81
Iteration 82
Iteration 83
Iteration 84
Iteration 85
Iteration 86
Iteration 87
Iteration 88
Iteration 89
Iteration 90
Iteration 91
Iteration 92
Iteration 93
Iteration 94
Iteration 95
Iteration 96
Iteration 97
Iteration 98
Iteration 99




```
## Answer

*A: Give a brief explanation of how the k-Means algorithm operates on this data.  What features is the algorithm considering?*

The k-means algorithm from the Python program takes in the data and the number of clusters the user specifies and creates data sets based on the number of clusters the user assigns. It works by finding the distinct groups or clusters of data that are closest together. Then, it partitions the data into clusters based on the distances of the data mean to that data point. 

*B: How many iterations were required for each value of `k`?*

The number of iterations vary by each value of k. 

*C: Which `k` value created the most reasonable clusters?  For that grouping, characterize the accounts that were clustered into each group.*

At k=10, the k-Means clustering algorithm created the most reasonable clusters. 


## Extra Credit
<!--
### Q5 - Create MDS Image (1 point)

Use MDS to create a JPEG of the accounts (see Module 12, slide 42).  Include the JPEG in your report. 

*A: How many iterations were required?*

*B: How well did the MDS do in grouping similar accounts together?  Were there any particularly odd groupings?*

### Q6 - Generate Nicer Dendrogram (not ASCII art) (1 point)

Generate the dendrogram figure from Q3 using [scipy's dendrogram](https://docs.scipy.org/doc/scipy/reference/generated/scipy.cluster.hierarchy.dendrogram.html) or [plotly's create_dendrogram](https://plotly.com/python/dendrogram/). The clusters should be the same those in Q3.
-->
### Q5 - Generate Nicer MDS Image (1 points)

Generate an MDS figure of the accounts (see Module 12, slide 42) as a scatterplot using regular Python graphing libraries or Vega-Lite/D3.  Plot the labels (could be in addition to the points or in place of the points) or allow the user to mouse-over the points and display the labels (i.e., tooltips).

Place a file with the full list in your repo. List the top 10 and bottom 10 movies in your report.
<!--
### Q6 - Generate Account-Term Matrix with TF-IDF (2 points)

Re-generate the account-term matrix but this time process the terms using proper TF-IDF calculations instead of the hack discussed on slide 12 (p. 12).  Use the same 500 terms, but this time replace their frequency count with TF-IDF scores (similar to as computed in HW3). Document the code, techniques, methods, etc. used to generate these TF-IDF values.  Upload the new account-term matrix file to GitHub.
*  For this IDF computation, you can use the tweets you gathered in Q1 as your corpus (instead of searching Google for each term). Treat the set of tweets from each account as a single document.

Then re-do Q3 with the new matrix.  Compare and contrast the resulting dendrogram with the dendrogram from Q3.

Note: Ideally you would not reuse the same 500 terms and instead would come up with TF-IDF scores for all the terms and then choose the top 500 from that list, but I'm trying to limit the amount of work necessary.
-->
## Submission

Make sure that you have committed and pushed your local repo to your private GitHub repo (inside the `hw8` folder).  Your repo should include your report, images, code, and data you developed to answer the questions. Include "Ready to grade @anwala" in your final commit message. 
