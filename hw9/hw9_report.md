# Final exam - Email Classification
### Sophia Chen
### DATA 440, Fall 2023
### Due Tuesday December 19, 2023

## Assignment

The goal of this assignment is to classify emails into two groups based on topic -- either `relevant` (on topic) or `non-relevant` (off topic). You may choose the topic based on what types of emails you typically receive (or what you have access to).
 
**Important:** Much of the code for this assignment is provided for you, therefore, your report must include a high-level description of how the code works and answers to all of the sub-questions asked.

**Tips for Completing this Assignment:**
* First, read the entire assignment before starting.
* *Don't start with a Google search.*  Your first references should be
    * [Module 13 lecture slides](https://docs.google.com/presentation/d/1j7qEgPjPtf7_5iwMDvdbKXdRHSdYzVUW/edit#slide=id.p1)
    * [Class Colab notebook](https://github.com/anwala/teaching-web-science/blob/main/fall-2022/week-13/data_440_03_f22_mod_13_pci_ch_06.ipynb)
    * [*Programming Collective Intelligence* book](https://go.oreilly.com/old-dominion-university/library/view/programming-collective-intelligence/9780596529321/) and [Chapter 6 code](https://github.com/arthur-e/Programming-Collective-Intelligence/tree/master/chapter6)



# Part 1
## Q1 - Create two datasets, Testing and Training (2 points)

Create two datasets, Training and Testing. You may choose a topic to classify your emails on (but choose only 1 topic). This can be spam, shopping emails, school emails, etc. 

The **Training** dataset should consist of
* 20 text documents for email messages you consider `relevant` to your chosen topic
* 20 text documents for email messages you consider `non-relevant` to your chosen topic

The **Testing** dataset should consist of:
* 5 text documents for email messages you consider `relevant` to your chosen topic
* 5 text documents for email messages you consider `non-relevant` to your chosen topic

*A: What topic did you decide to classify on?*


## Answer

I decided to do my topic on distinguishing my college's emails from non-college ones, such as categorizing the groups to be the ones related to William and Mary and non-related to the school. 

## Discussion

To obtain the text files from my emails, I copied and pasted the content into an empty text file. I continued to do this for each testing and training category, based on whether or not they are affiliated with the college.

## Q2 - Naive Bayes classifier (3 points) 

Use the example code in the class Colab notebook to train and test the Naive Bayes classifier.  
* Use your *Training* dataset to *train* the Naive Bayes classifier.  
* Use your *Testing* dataset to *test* the Naive Bayes classifier.

Create a table to report the classification results for each email message in the *Testing* dataset.  The table should include what the classifier reported (`relevant` or `non-relevant`) and the actual classification.

*A: For those emails that the classifier got wrong, what factors might have caused the classifier to be incorrect?  You will need to look at the text of the email to determine this.*

## Answer

For this part of the problem, I used the functions and classes presented in Module 13 - Document Filtering to use the Naive Bayes classifier in Python. I wrote code that iterates over the email text files that need to be imported for testing and training. 

Since the email classifier classified both relevant and irrelevant emails as 'bad,' I suspect common words that the classifier cannot distinguish may frequently appear in both email categories, causing the classifier to be unable to detect what is good versus bad. 



## Discussion

```

class basic_classifier:

  def __init__(self,getfeatures,filename=None):
    # Counts of feature/category combinations
    self.fc={}
    # Counts of documents in each category
    self.cc={}
    self.getfeatures=getfeatures

  # Increase the count of a feature/category pair
  def incf(self,f,cat):
    self.fc.setdefault(f, {})
    self.fc[f].setdefault(cat, 0)
    self.fc[f][cat]+=1

  # Increase the count of a category
  def incc(self,cat):
    self.cc.setdefault(cat, 0)
    self.cc[cat]+=1

  # The number of times a feature has appeared in a category
  def fcount(self,f,cat):
    if f in self.fc and cat in self.fc[f]:
      return float(self.fc[f][cat])
    return 0.0

  # The number of items in a category
  def catcount(self,cat):
    if cat in self.cc:
        return float(self.cc[cat])
    return 0

  # The total number of items
  def totalcount(self):
    return sum(self.cc.values())

  # The list of all categories
  def categories(self):
    return self.cc.keys()

  def train(self,item,cat):
    features=self.getfeatures(item)
    # Increment the count for every feature with this category
    for f in features:
      self.incf(f,cat)

    # Increment the count for this category
    self.incc(cat)

  def fprob(self,f,cat):
    if self.catcount(cat)==0: return 0

    # The total number of times this feature appeared in this
    # category divided by the total number of items in this category
    return self.fcount(f,cat)/self.catcount(cat)

  def weightedprob(self,f,cat,prf,weight=1.0,ap=0.5):
    # Calculate current probability
    basicprob=prf(f,cat)

    # Count the number of times this feature has appeared in
    # all categories
    totals=sum([self.fcount(f,c) for c in self.categories()])

    # Calculate the weighted average
    bp=((weight*ap)+(totals*basicprob))/(weight+totals)
    return bp

# For non relevant emails
import os
# assign directory
directory = '/content/drive/MyDrive/DATA440Fall2023/FinalExam/training_non_relevant_emails'

my_non_relevant_emails = []
# iterate over files in
# that directory
for filename in os.listdir(directory):
    # checking if it is a file
    if filename.endswith('.txt'):
        with open(os.path.join(directory, filename)) as f:
            #print(f.read())
            my_non_relevant_emails.append(f.read())

# For relevant emails
# assign directory
directory = '/content/drive/MyDrive/DATA440Fall2023/FinalExam/training_relevant_emails'

my_relevant_emails = []
# iterate over files in
# that directory
for filename in os.listdir(directory):
    # checking if it is a file
    if filename.endswith('.txt'):
        with open(os.path.join(directory, filename)) as f:
            #print(f.read())
            my_relevant_emails.append(f.read())

# Training the sample
def sampletrain(cl):
  cl.train(my_non_relevant_emails[0],'bad')
  cl.train(my_non_relevant_emails[1],'bad')
  cl.train(my_non_relevant_emails[2],'bad')
  cl.train(my_non_relevant_emails[3],'bad')
  cl.train(my_non_relevant_emails[4],'bad')
  cl.train(my_non_relevant_emails[5],'bad')
  cl.train(my_non_relevant_emails[6],'bad')
  cl.train(my_non_relevant_emails[7],'bad')
  cl.train(my_non_relevant_emails[8],'bad')
  cl.train(my_non_relevant_emails[9],'bad')
  cl.train(my_non_relevant_emails[10],'bad')
  cl.train(my_non_relevant_emails[11],'bad')
  cl.train(my_non_relevant_emails[12],'bad')
  cl.train(my_non_relevant_emails[13],'bad')
  cl.train(my_non_relevant_emails[14],'bad')
  cl.train(my_non_relevant_emails[15],'bad')
  cl.train(my_non_relevant_emails[16],'bad')
  cl.train(my_non_relevant_emails[17],'bad')
  cl.train(my_non_relevant_emails[18],'bad')
  cl.train(my_non_relevant_emails[19],'bad')
  cl.train(my_relevant_emails[0],'good')
  cl.train(my_relevant_emails[1],'good')
  cl.train(my_relevant_emails[2],'good')
  cl.train(my_relevant_emails[3],'good')
  cl.train(my_relevant_emails[4],'good')
  cl.train(my_relevant_emails[5],'good')
  cl.train(my_relevant_emails[6],'good')
  cl.train(my_relevant_emails[7],'good')
  cl.train(my_relevant_emails[8],'good')
  cl.train(my_relevant_emails[9],'good')
  cl.train(my_relevant_emails[10],'good')
  cl.train(my_relevant_emails[11],'good')
  cl.train(my_relevant_emails[12],'good')
  cl.train(my_relevant_emails[13],'good')
  cl.train(my_relevant_emails[14],'good')
  cl.train(my_relevant_emails[15],'good')
  cl.train(my_relevant_emails[16],'good')
  cl.train(my_relevant_emails[17],'good')
  cl.train(my_relevant_emails[18],'good')
  cl.train(my_relevant_emails[19],'good')

text = my_relevant_emails[18]

cl.classify(text, default='unkown')

Output: 
'good'

sampletrain(cl)
#print("")
print("Total items:", cl.totalcount())
print("Categories:", cl.categories())
for cat in cl.categories():
  print(cat, cl.catcount(cat))

Output: 
Total items: 80
Categories: dict_keys(['bad', 'good'])
bad 40.0
good 40.0

# Using Naive Bayes Classifier
class naivebayes(basic_classifier):   # change for basic_classifier

  def __init__(self,getfeatures):
    basic_classifier.__init__(self,getfeatures)  # change for basic_classifier
    self.thresholds={}

  def docprob(self,item,cat):
    features=self.getfeatures(item)

    # Multiply the probabilities of all the features together
    p=1
    for f in features: p*=self.weightedprob(f,cat,self.fprob)
    return p

  def prob(self,item,cat):
    catprob=self.catcount(cat)/self.totalcount()
    docprob=self.docprob(item,cat)
    return docprob*catprob

  def setthreshold(self,cat,t):
    self.thresholds[cat]=t

  def getthreshold(self,cat):
    if cat not in self.thresholds: return 1.0
    return self.thresholds[cat]

  def classify(self,item,default=None):
    probs={}
    # Find the category with the highest probability
    max=0.0
    for cat in self.categories():
      probs[cat]=self.prob(item,cat)
      if probs[cat]>max:
        max=probs[cat]
        best=cat

    # Make sure the probability exceeds threshold*next best
    for cat in probs:
      if cat==best: continue
      if probs[cat]*self.getthreshold(best)>probs[best]: return default
    return best

# Running the test

import os
# assign directory
directory = '/content/drive/MyDrive/DATA440Fall2023/FinalExam/testing_non_relevant_emails'

testing_non_relevant_emails = []
# iterate over files in
# that directory
for filename in os.listdir(directory):
    # checking if it is a file
    if filename.endswith('.txt'):
        with open(os.path.join(directory, filename)) as f:
            #print(f.read())
            testing_non_relevant_emails.append(f.read())


# For non-relevant emails
cl = naivebayes(getwords)
sampletrain(cl)
cl.classify(testing_non_relevant_emails[0], default='unknown')

Output: 
'bad'

cl = naivebayes(getwords)
sampletrain(cl)
cl.classify(testing_non_relevant_emails[1], default='unknown')

Output: 
'bad'

cl = naivebayes(getwords)
sampletrain(cl)
cl.classify(testing_non_relevant_emails[2], default='unknown')

Output: 
'bad'

cl = naivebayes(getwords)
sampletrain(cl)
cl.classify(testing_non_relevant_emails[3], default='unknown')

Output: 
'bad'

cl = naivebayes(getwords)
sampletrain(cl)
cl.classify(testing_non_relevant_emails[4], default='unknown')

Output: 
'bad'

# For relevant emails
cl = naivebayes(getwords)
sampletrain(cl)
cl.classify(testing_relevant_emails[0], default='unknown')

Output: 
'bad'

cl = naivebayes(getwords)
sampletrain(cl)
cl.classify(testing_relevant_emails[1], default='unknown')

Output: 
'bad'

cl = naivebayes(getwords)
sampletrain(cl)
cl.classify(testing_relevant_emails[2], default='unknown')

Output: 
'bad'

cl = naivebayes(getwords)
sampletrain(cl)
cl.classify(testing_relevant_emails[3], default='unknown')

Output: 
'bad'

cl = naivebayes(getwords)
sampletrain(cl)
cl.classify(testing_relevant_emails[4], default='unknown')

Output: 
'bad'

```

The table below report the classification results for each email message in the *Testing* dataset.

|Email|Reported Classification |Actual Classification|
|:---|:---|:---|
|Testing Relevant 1|'bad'|'good'|
|Testing Relevant 2|'bad'|'good'|
|Testing Relevant 3|'bad'|'good'|
|Testing Relevant 4|'bad'|'good'|
|Testing Relevant 5|'bad'|'good'|
|Testing Non-Relevant 1|'bad'|'bad'|
|Testing Non-Relevant 2|'bad'|'bad'|
|Testing Non-Relevant 3|'bad'|'bad'|
|Testing Non-Relevant 4|'bad'|'bad'|
|Testing Non-Relevant 5|'bad'|'bad'|




### Q3 - Confusion Matrix (3 points)

Draw a confusion matrix for your classification results (see Module 13, [slides 42](https://docs.google.com/presentation/d/1j7qEgPjPtf7_5iwMDvdbKXdRHSdYzVUW/edit#slide=id.p42)).  
* This should be a table in Markdown or LaTeX, NOT a screenshot of output or image generated by another program.  There's an example of a LaTeX confusion matrix in the [Overleaf report template](https://www.overleaf.com/read/tzvqcjvjtgdx).


*A: Based on the results in the confusion matrix, how well did the classifier perform?*  

*B: Would you prefer an email classifier to have more false positives or more false negatives?  Why?*


## Answer 

A)
 Based on the results in the confusion matrix, the classifier did not perform very well. 



B) 

 I prefer an email classifier to have more false positives because it is safer to consider irrelevant emails important than disregard a vital email that contains crucial information. An email classifier with more false positives will report spam emails as important, but that will not bring me any severe consequences. At most, it can allow me to spend a few extra minutes discovering that it is unnecessary and ignore the issue. However, classifying essential emails as spam can bring me further consequences of missing out on important information and events. Thus, I would rather have my email classifier have more false positives than false negatives. 


### Q4 *(1 point)* 

Report the [precision and recall](https://developers.google.com/machine-learning/crash-course/classification/precision-and-recall) scores of your classification results.  Include the formulas you used to compute these values.

## Answer  

| | |Actual||
|---|---|---|---|
|**Predicted**| |Reported|Actual|
| |Reported|0 (TP)|0 (FP)|
| |Actual|5 (FN)|5 (TN)|


Precision = TP/(TP + FP)
= 0/0
= 0

Recall = TP/(TP + FN)
= 0/(0+5)
= 0

## Discussion 
From the confusion matrix, there are zero true positives, zero false positives, five false negatives, and five true negatives. There are five false negatives because the classifier identified five emails in the testing set to be 'bad' when they are actually not spam and five emails to be 'bad' when they are spam. 

The Precision score shows the correct identifications and the Recall score shows the correct positives identified correctly. These scores are zero because the classifier did not make any positive identifications nor correctly identify positives in the emails. 

<!--
### Q5 *(2 points)* 

Tune your classifier by updating weights to obtain better classification results. You may want to change the default weights (`weight`, `ap`) given to `weightedprob()` or the threshold used for the Bayesian classifier or change how the words are extracted from the document (for this you will need to re-train the model).  Report the changes you made, re-run your Testing dataset, and show that the performance improved (either by using the confusion matrix or by computing precision and recall).

If your classifier got all of the items correct in Q2, change the weights to make the classifier perform worse and discuss the results.

### Q6 *(3 points)* 

Implement the classifier with the Multinomial model instead of the multiple Bernoulli model and re-run Q2 and Q3.  Did the classification improve? *Ensure to remove the unique word filter from the extractor.*

*For credit on this part, you must describe what you have done and discuss the differences between the Multinomial model and the multiple Bernoulli model.*
-->


# References

* Classification: Precision and Recall, <https://developers.google.com/machine-learning/crash-course/classification/precision-and-recall>
* Confusion Matrix, <https://www.sciencedirect.com/topics/engineering/confusion-matrix#:~:text=A%20confusion%20matrix%20is%20a,performance%20of%20a%20classification%20algorithm.>
* Python Classes: The Power of Object-Oriented Programming, <https://realpython.com/python-classes/>
* Naive Bayes Classifier Explained: Applications and Practice Problems of Naive Bayes Classifier, <https://www.analyticsvidhya.com/blog/2017/09/naive-bayes-explained/>

