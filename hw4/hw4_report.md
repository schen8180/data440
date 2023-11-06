# HW4 - Exploring Social Networks
### Sophia Chen 
### DS 440, Fall 2023
### November 2, 2023 

# Topic: You will investigate the friendship paradox on Facebook and Twitter, which says "most people have fewer friends than their friends have, on average."

# Q1 Friendship Paradox on Facebook

Determine if the friendship paradox holds for a user's Facebook account. (This used to be more interesting when you could more easily download your friend's friends list from Facebook. Facebook now requires each friend to approve this operation, effectively making it impossible.)

Q: What is the mean, standard deviation, and median of the number of friends that the user's friends have?



## Answer
According to the plot I made, it shows that the user has fewer friends than the friends their friends have. Thus, the friendship paradox does hold for this user's Facebook account. 

For the number of friends that the user's friends have, they have a mean of 542.6734693877551, a standard deviation of 536.6744685696292, and a median of 396.0. 

The figure below shows an example of the friendship paradox for a user.

## Discussion

I used Python code and imported libraries such as the pandas, numpy, matplotlib, and seaborn libraries to do this assignment. 

Then, I imported and read this assignment's data file and named it as friends. From this, I created variables that separate the user, User, from their friends and the variable User by themself. Then, I used Python to calculate the mean, median, and standard deviation for their friends. 

To create the plot, I utilized the concepts I learned from my data visualization class and made a scatter plot that shows the friendship paradox. The plot I made does, indeed, show that the friendship paradox holds for this individual. 

![\label{fig:friendship}](https://github.com/schen8180/data440/blob/main/hw4/hw_4%20(2).png?raw=true)


```python

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

friends = pd.read_csv('friend_count.csv')

no_user = friends[:-1] # to get df without user

no_user_list = no_user[" FRIENDCOUNT"].to_numpy() #converting the values into a list to perform python calculations to find the mean, standard deviation, and the median of the friend counts. 

np.mean(no_user_list) #getting mean
542.6734693877551

np.std(no_user_list) #standard deviation
536.6744685696292

np.median(no_user_list)
396.0

#making a list with friend count for later use
mylist = []
counter = 0
for i in friends['USER']:
    counter += 1
    i = f"friend {counter}" 
    mylist.append(i)
mylist #this is the list of friends

friends['USERS'] = mylist

#getting info about user
user = friends[friends["USER"] == 'User ']

#sorting the values
friends.sort_values(' FRIENDCOUNT', ascending=False, inplace=True)


#making the plot,  this is where the user and the list comes in 
plt.figure(figsize = [30,16])
ax = sns.scatterplot(data = friends, x = "USERS", y = " FRIENDCOUNT", s = 60, alpha = 0.99, ec = 'k')
sns.scatterplot(data = user , x = "USERS", y = " FRIENDCOUNT", s = 250, ec = 'crimson', ax = ax,
               color = 'none')

plt.yticks(fontsize = 14)
plt.xlabel('USERS', fontsize = 26, labelpad = 20)
plt.xticks(fontsize=12,rotation=60, weight = 'bold')
plt.xlim(-5, 99)
plt.ylabel( 'FRIENDCOUNT', fontsize = 26, labelpad = 20)
plt.title("Does the Friendship Paradox hold for this user and their friends on Facebook?",fontsize = 26)
plt.savefig('hw_4.png',bbox_inches = 'tight',facecolor='white')
plt.show()

```


* How do I select a subset of a DataFrame?, <https://pandas.pydata.org/docs/getting_started/intro_tutorials/03_subset_data.html>

* How to Convert Pandas DataFrame into a List?, <https://www.geeksforgeeks.org/how-to-convert-pandas-dataframe-into-a-list/>

* How to Fix: KeyError in Pandas <https://www.geeksforgeeks.org/how-to-fix-keyerror-in-pandas/>

* matplotlib.pyplot.xlabel <https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.xlabel.html>
