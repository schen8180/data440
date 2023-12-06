# HW7 - Recommender system
### Sophia Chen
### DATA 440, Fall 2023
### Due November 30, 2023

# Assignment

The goal of this assignment is to use the basic recommendation principles we have learned to recommend movies for yourself. Utilize code from Class notebook w/examples; you're not expected to implement the core functionalities from scratch.

Write a report that contains the answers and explains how you arrived at the answers to the following questions. Before starting, review the HW report guidelines. Name your report for this assignment hw7_report with the proper file extension.

Report (2 points)

---


## Q1 

Find 3 users who are closest to you in terms of age, gender, and occupation.

For each of those 3 users:

A: What are their top 3 (favorite) films?

B: What are their bottom 3 (least favorite) films?

Based on the movie values in those 6 tables (3 users X (favorite + least favorite)), choose a user that you feel is most like you. Feel free to note any outliers (e.g., "I mostly identify with user 123, except I did not like "Ghost" at all"). You can investigate more than just the top 3 and bottom 3 movies to find your best match.

This user is the substitute you.

## Answer
The 3 users who are closest to me in terms of age, gender, and occupation are: 324, 477, 496. 

Their top 3 (favorite) films and bottom 3 (least favorite) films are listed down below: 

```

324|21|F|student|02176

top 3 films:
324	748	5	880575108
324	471	5	880575412
324	298	5	880575493

bottom 3 films:
324	877	1	880575163
324	283	3	880575531
324	332	3	880574766

477|23|F|student|02125

top 3 films:
477	815	5	875941763

477	709	5	875941763

477	88	5	875941085

bottom 3 films:
477	280	4	875941022

477	781	4	875941191

477	15	4	875941863

496|21|F|student|55414

top 3 films:

496	727	5	876072633 - 727|Immortal Beloved (1994)|01-Jan-1994||http://us.imdb.com/M/title-exact?Immortal%20Beloved%20(1994)|0|0|0|0|0|0|0|0|1|0|0|0|0|0|1|0|0|0|0


496	921	5	876072633 - 921|Farewell My Concubine (1993)|01-Jan-1993||http://us.imdb.com/M/title-exact?Ba%20Wang%20Bie%20Ji%20(1993)|0|0|0|0|0|0|0|0|1|0|0|0|0|0|1|0|0|0|0

496	42	5	876066676 - 42|Clerks (1994)|01-Jan-1994||http://us.imdb.com/M/title-exact?Clerks%20(1994)|0|0|0|0|0|1|0|0|0|0|0|0|0|0|0|0|0|0|0

bottom 3 films:

496	97	1	876066848 - 97|Dances with Wolves (1990)|01-Jan-1990||http://us.imdb.com/M/title-exact?Dances%20with%20Wolves%20(1990)|0|0|1|0|0|0|0|0|1|0|0|0|0|0|0|0|0|0|1

496	1444	1	876066465 - 1444|That Darn Cat! (1965)|01-Jan-1965||http://us.imdb.com/Title?That+Darn+Cat%21+(1965)|0|0|0|0|1|1|0|0|0|0|0|0|0|1|0|0|0|0|0

496	136	1	876066424 - 136|Mr. Smith Goes to Washington (1939)|01-Jan-1939||http://us.imdb.com/M/title-exact?Mr.%20Smith%20Goes%20to%20Washington%20(1939)|0|0|0|0|0|0|0|0|1|0|0|0|0|0|0|0|0|0|0

```

I am chosing 496 as the user that is most like me as we both really like the film 921, which is Farewell My Concubine (1993). This is the only film that we share a common factor in. I am not too familar with the movies that the other 2 users have watched and rated. 

## Discussion

```
# this is the code I used to open and read the user.txt file from the Movie Lens dataset and find the users that are most similar to me

user1 = open("/content/drive/MyDrive/DATA440Fall2023/u.user.txt","r")
while True:
  content=user1.readline()
  if '21' in content and 'F' in content and 'student' in content:
    print(content)
  #print(type(content)) #content is a string
  if not content:
    break

user1.close()

```


```

I picked the users that share the similar occupation, gender, and age as me. 

324|21|F|student|02176

477|23|F|student|02125

496|21|F|student|55414
```

```
# To find the movies the users have watched, I created if statements that can be used to search for certain users based on their user id. 
By changing the rating from 5 to 1, I can find their most favorite and least favorite films 

Here is an example: 
data1 = open("/content/drive/MyDrive/DATA440Fall2023/u.data.txt","r")
while True:
  content2 = data1.readline()
  content2_list = content2.split('\t')
  if '496' in content2_list[0] and '5' in content2_list[2]:
    print(content2)
  if not content2:
    break

```

```
# I practiced the same logic as I did for the previous files here to find the names of the films. This code helps identity the movie names to the movie ids from the users. 

Here is an example: 
item1 = open("/content/drive/MyDrive/DATA440Fall2023/u.item.txt","r",encoding = "ISO-8859-1")
while True:
  content=item1.readline()
  if '921' in content:
    print(content)
  if not content:
    break
    
```



## Q2

Based on the ratings that users have given to the movies, answer the following questions:

* *A: Which 5 users are most correlated to the* substitute you *(i.e., which 5 users rate movies most similarly to the* substitute you?)

* *B: Which 5 users are least correlated (i.e., negative correlation)?*


## Answer

A: The 5 users that are most correlated to my subsitute are users: 644, 564, 791, 939, 842. 

We both share a Pearson Correlation Coefficient of 1, meaning we share a positive relationship in the movies we like and dislike. 

B: The 5 users that are least correlated from to my subsitute are users: 206, 205, 126, 39, and 19. 

Our Pearson Correlation Coefficient is -1.0, which says we do not share the same taste in movie ratings.

## Discussion
To answer this question, I used functions such as topMatches(), sim_pearson(), and sim_distance() from the collab notebook. First, I created a dictionary to store the users' movies from the movie lens dataset. 

After getting the dictionary, I stored it to a variable called critics to use in the topMatches() function. Doing this allowed me to find the five users that are most correlated and least correlated to my substitute user. 

```
nested_dict = {}

with open("/content/drive/MyDrive/DATA440Fall2023/u.data.txt","r") as file:
    for line in file:
        user_id, movie_id, rating, _ = map(int, line.strip().split('\t'))
        nested_dict.setdefault(user_id, {})[movie_id] = rating
    nested_dict


critics = nested_dict


from math import sqrt


def sim_pearson(prefs, p1, p2):
    '''
    Returns the Pearson correlation coefficient for p1 and p2.
    '''

    # Get the list of mutually rated items
    si = {}
    for item in prefs[p1]:
        if item in prefs[p2]:
            si[item] = 1

    # If they are no ratings in common, return 0
    if len(si) == 0:
        return 0

    # Sum calculations
    n = len(si)

    # Sums of all the preferences
    sum1 = sum([prefs[p1][it] for it in si])
    sum2 = sum([prefs[p2][it] for it in si])

    # Sums of the squares
    sum1Sq = sum([pow(prefs[p1][it], 2) for it in si])
    sum2Sq = sum([pow(prefs[p2][it], 2) for it in si])

    # Sum of the products
    pSum = sum([prefs[p1][it] * prefs[p2][it] for it in si])

    # Calculate r (Pearson score)
    num = pSum - sum1 * sum2 / n
    den = sqrt((sum1Sq - pow(sum1, 2) / n) * (sum2Sq - pow(sum2, 2) / n))
    if den == 0:
        return 0
    r = num / den
    return r

def topMatches(
    prefs,
    person,
    n=5,
    similarity=sim_pearson,
):
    '''
    Returns the best matches for person from the prefs dictionary.
    Number of results and similarity function are optional params.
    '''

    scores = [(similarity(prefs, person, other), other) for other in prefs
              if other != person]
    scores.sort()
    scores.reverse()
    return scores[0:n]


```
To find top matches
topMatches(critics, 496, n=5)

To find lowest matches
topMatches(critics, 496, n = 943) 

#I took the length of the users, and found values in the last five indexes to see the users' lowest matches.

## Q3


Compute ratings for all the films that the *substitute you* has not seen.  

Provide a list of the top 5 recommendations for films that the *substitute you* should see.  

Provide a list of the bottom 5 recommendations (i.e., films the *substitute you* is almost certain to hate).


## Answer

List of the top 5 movie recommendations that I know my user will love:

function:
getRecommendations(critics, 496)[0:5]

output: 
[(5.000000000000001, 1500),(5.000000000000001, 850),(5.0, 1656),(5.0,1617),(5.0, 1612)]


List of the bottom 5 movie recommendations that I know my user will hate:

function:
getRecommendations(critics, 496)[-5:]

output: 
[(1.0, 599), (1.0, 439), (1.0, 437), (1.0, 314), (1.0, 247)]


## Discussion
To answer this question, I used the function provided by this homework module, the getRecommendations(). This allowed me to find movies I knew my substitute would love and hate. To see the film I will dislike, I used list indexation to find the last few items in the list of recommendations. 
```
#Function provided: 

def getRecommendations(prefs, person, similarity=sim_pearson):
    '''
    Gets recommendations for a person by using a weighted average
    of every other user's rankings
    '''

    totals = {}
    simSums = {}
    for other in prefs:
    # Don't compare me to myself
        if other == person:
            continue
        sim = similarity(prefs, person, other)
        # Ignore scores of zero or lower
        if sim <= 0:
            continue
        for item in prefs[other]:
            # Only score movies I haven't seen yet
            if item not in prefs[person] or prefs[person][item] == 0:
                # Similarity * Score
                totals.setdefault(item, 0)
                # The final score is calculated by multiplying each item by the
                #   similarity and adding these products together
                totals[item] += prefs[other][item] * sim
                # Sum of similarities
                simSums.setdefault(item, 0)
                simSums[item] += sim
    # Create the normalized list
    rankings = [(total / simSums[item], item) for (item, total) in
                totals.items()]
    # Return the sorted list
    rankings.sort()
    rankings.reverse()
    return rankings


```
```

# list of the top 5 movie recommendations that I know my user will love:
getRecommendations(critics, 496)[0:5]

[(5.000000000000001, 1500),(5.000000000000001, 850),(5.0, 1656),(5.0,1617),(5.0, 1612)]

```

```
# list of the bottom 5 movie recommendations that I know my user will hate:

getRecommendations(critics, 496)[-5:]


[(1.0, 599), (1.0, 439), (1.0, 437), (1.0, 314), (1.0, 247)]

```

## Q4

Choose your (the real you, not the *substitute you*) favorite and least favorite film from the list of 1,682 movies in `u.item`.  
For each film, generate a list of the top 5 most correlated and bottom 5 least correlated films.

## Answer

Favorite film: Farewell My Concubine (1992) 


Least favorite film: 99|Snow White and the Seven Dwarfs (1937) 

## Discussion

For this problem, I used the transformPrefs() and topMatches() functions to find movies that are the most similar and least similar to the films I like and dislike. I repeated the logic I used for the previous question to find the movies. 

```
item1 = open("/content/drive/MyDrive/DATA440Fall2023/u.item.txt","r",encoding = "ISO-8859-1")
while True:
  content=item1.readline()
  if 'Farewell My Concubine' in content: # by replacing with the titles of my favorite and least favorite film I can find their movie names 
    print(content)
  if not content:
    break
```

```

def transformPrefs(prefs):
    '''
    Transform the recommendations into a mapping where persons are described
    with interest scores for a given title e.g. {title: person} instead of
    {person: title}.
    '''

    result = {}
    for person in prefs:
        for item in prefs[person]:
            result.setdefault(item, {})
            # Flip item and person
            result[item][person] = prefs[person][item]
    return result

#this is for Farewell My Concubine
movies = transformPrefs(critics) 
topMatches(movies, 921)
[(1.000000000000004, 1223),
 (1.0000000000000027, 1418),
 (1.0000000000000027, 873),
 (1.0000000000000027, 832),
 (1.0000000000000018, 539)]

topMatches(movies, 921, n = 1682)[-5:] # setting this index to find last five values in the list for lowest matches

output
[(-1.0, 453), 
(-1.0, 452), 
(-1.0, 388), 
(-1.0, 376), 
(-1.000000000000004, 844)]

#this is for Snow White

topMatches(movies, 99) 
[(1.0000000000000027, 1299),
 (1.000000000000001, 981),
 (1.0000000000000002, 247),
 (1.0, 1523),
 (1.0, 1514)]


topMatches(movies, 99, n = 1682)[-5:]
output
[(-1.0000000000000007, 1423),
 (-1.0000000000000007, 1346),
 (-1.0000000000000007, 1270),
 (-1.0000000000000018, 1261),
 (-1.000000000000004, 882)]
```

# References

* data_440_03_f22_mod_11_pci_ch_02.ipynb

* MovieLens 100K Dataset <https://grouplens.org/datasets/movielens/100k/>

* Read a tab separated file with first column as key and the rest as values <https://stackoverflow.com/questions/29920440/read-a-tab-separated-file-with-first-column-as-key-and-the-rest-as-values>

* How to get last items of a list in Python? https://stackoverflow.com/questions/646644/how-to-get-last-items-of-a-list-in-python

* Python Nested Dictionary, <https://www.programiz.com/python-programming/nested-dictionary>

* Pearson Correlation Coefficient (r) | Guide & Examples, <https://www.scribbr.com/statistics/pearson-correlation-coefficient/#:~:text=The%20Pearson%20correlation%20coefficient%20(r,the%20relationship%20between%20two%20variables.&text=When%20one%20variable%20changes%2C%20the,changes%20in%20the%20same%20direction.>

* "for line in..." results in UnicodeDecodeError: 'utf-8' codec can't decode byte, <https://stackoverflow.com/questions/19699367/for-line-in-results-in-unicodedecodeerror-utf-8-codec-cant-decode-byte>