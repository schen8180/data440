# HW0 - Writing Reports
### Sophia Chen
### DATA 440, Fall 2023
### Due Tuesday September 12, 2023

# Part 1
## Q1 

*You may copy the question into your report, but make sure that you make it clear where the question ends and your answer begins.*

## Answer

The example figure below shows the graphic of what is web science. 

![web_science.png](https://raw.githubusercontent.com/schen8180/data440/main/hw0/Web%20Image_ECS_Xlarge.jpg_SIA_JPG_fit_to_width_INLINE.jpg?token=GHSAT0AAAAAACHJXMY4VTUXP4ZYGNHPMOLGZH7QGHQ)



*If you want to include code in your report, you can insert a screenshot (if it's legible), or you can copy/paste the code into a fenced code block.*

```python
#!/usr/local/bin/python3
# testargs.py

import random
import string

password = (random.choices(string.ascii_letters, k=6) + random.choices(string.digits, k=3))
random.shuffle(password)
password = ''.join(password)
print('Your randomly generated password is', password)
```

The table below shows a table of the first four weeks of the course syllabus.  

|Week|Date|Topic|
|:---|:---|:---|
|1|Aug 31 & Sep 5|Introduction to Web Science and Web Architecture|
|2|Sep 7 & 12|Introduction to Python|
|3|Sep 14 & 19|Introduction to Info Vis with R, Python|
|4|Sep 21 & 26|Measuring the Web|

The table below shows an example confusion matrix (you'll see this term later) from <https://en.wikipedia.org/wiki/Confusion_matrix>.

| | |Actual||
|---|---|---|---|
|**Predicted**| |Cat|Dog|
| |Cat|5 (TP)|3 (FP)|
| |Dog|2 (FN)|3 (TN)|

## Discussion

*You must provide some discussion of every answer. Discuss how you arrived at the answer and the tools you used. Discuss the implications of your answer.*

# Part 2

## Q1

Create a directory (name it whatever you wish, e.g., data440. Change the permissions on this directory so that you are the only user who can read, write, or execute (view the contents) the directory (see "Protection and Permission"). Take a screenshot of (or copy/paste) the command and its output into your report. 

```
(base) xi@Sophias-MacBook-Air-4 ~ % cd Downloads
(base) xi@Sophias-MacBook-Air-4 Downloads % chmod 740 data440
(base) xi@Sophias-MacBook-Air-4 Downloads % ls -l data440
total 0
drwxr-xr-x  4 xi  staff  128 Sep 11 16:26 folder1
(base) xi@Sophias-MacBook-Air-4 Downloads % 

```

```
(base) xi@Sophias-MacBook-Air-4 folder1 % chmod +rwx test1.txt
(base) xi@Sophias-MacBook-Air-4 folder1 % chmod +rwx testing.txt
(base) xi@Sophias-MacBook-Air-4 folder1 % ls -l
total 8
-rwxr-xr-x@ 1 xi  staff  38 Sep 10 21:16 test1.txt
-rwxr-xr-x  1 xi  staff   0 Sep 11 16:04 testing.txt
(base) xi@Sophias-MacBook-Air-4 folder1 % 

```



## Q2 
For each of the commands below, do the following: 
- Execute the command
- Take a screenshot of (or copy/paste) the command and its output into your report
- Write a sentence that describes what the command did

Commands:

1.) wc -l test.txt

2.) echo "CS 800" >> test.txt; cat test.txt

3.) grep CS test.txt

4.) grep -c CS test.txt

5.) sort test.txt

6.) sort -k2 test.txt

7,) sort -k2 -n test.txt

8.) sort test.txt | uniq -c

# 
## Answer
1.) wc -l test.txt -
This statement prints the number of lines in the test file, 
```
(base) xi@Sophias-MacBook-Air-4 data440 % wc -l test1.txt
       5 test1.txt
```

2.) echo "CS 800" >> test.txt; cat test.txt

This statement displays the lines of text that are passed as arguements on the command line, like replicating the lines of text that are passed as arguements on the command line

```
(base) xi@Sophias-MacBook-Air-4 data440 % echo "CS 800" >> test.txt; cat test1.txt
CS 800
CS 432
CS 725
MATH 212
MATH 32
```

3.) grep CS test.txt

This statement searches the file for a pattern of characters, in this case, lines of text that have cs in them and displays them
```
(base) xi@Sophias-MacBook-Air-4 data440 % grep CS test1.txt
CS 800
CS 432
CS 725
```

4.) grep -c CS test.txt

This statement outputs the number of lines in file .txt that contain the word pattern as a string or a sub-string. It counts how many lines of text that contain the letter c in it. In this case, there are three lines that match the pattern c in them. 
```
(base) xi@Sophias-MacBook-Air-4 data440 % grep -c CS test1.txt
3
```

5.) sort test.txt

This statement sorts the lines of text in the text file alphabetically. 

```
(base) xi@Sophias-MacBook-Air-4 data440 % sort test1.txt
CS 432
CS 725
CS 800
MATH 212
MATH 32
```


6.) sort -k2 test.txt

This statement 

```
(base) xi@Sophias-MacBook-Air-4 data440 % sort -k2 test1.txt
MATH 212
MATH 32
CS 432
CS 725
CS 800
```
7,) sort -k2 -n test.txt

This statement arranges the text file by sorting the lines of text in a certain number of columns. k2 means to sort the second column, but there is no other columns presented.  -n means to sort the file in numeric ascending order. 

```
(base) xi@Sophias-MacBook-Air-4 data440 % sort -k2 -n test1.txt
MATH 32
MATH 212
CS 432
CS 725
CS 800
```


8.) sort test.txt | uniq -c

This statement first sorts the list, and the second command uniq -c strips duplicate lines from the text file. the uniq command also automatically assumes the file has been sorted.  

```
(base) xi@Sophias-MacBook-Air-4 data440 % sort test1.txt | uniq -c
   1 CS 432
   1 CS 725
   1 CS 800
   1 MATH 212
   1 MATH 32
```

# References

*Every report must list the references that you consulted while completing the assignment. If you consulted a webpage, you must include the URL.*

* How to Sort Text Files in Linux Using the sort Command, <https://www.makeuseof.com/how-to-use-sort-in-linux/#:~:text=Sort%20a%20File%20Numerically,the%20data%20in%20ascending%20order.&text=If%20you%20want%20to%20sort%20in%20descending%20order%2C%20reverse%20the,n%20flag%20in%20the%20command.>
* Linux Journey, <https://linuxjourney.com/lesson/file-permissions>
* How to manage Linux permissions for users, groups, and others <https://www.redhat.com/sysadmin/manage-permissions>

