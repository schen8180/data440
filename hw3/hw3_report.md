# HW3 - Ranking Webpages 
### Sophia 
### DS 440, Fall 2023
### 10/25/2023

# Q1. Data Collection (4 points)

For the following tasks, consider which items could be scripted with a shell script or Python. Consider creating separate scripts for different tasks. Determine the best way to collect the data.

Download the HTML content of the 1000 unique URIs you gathered in HW2 and strip out HTML tags (called "boilerplate") so that you are left with the main text content of each webpage. Plan ahead because this will take time to complete.

Save the HTML content returned from each URI in a uniquely-named file. The easiest thing is to use the URI itself as the filename, but your shell will likely not like some of the characters that may occur in URIs (e.g., "?", "&"). My suggestion is to hash the URIs to associate them with their respective filename using a cryptographic hash function, like MD5.


### Removing HTML Boilerplate

Now use a tool to remove (most) of the HTML markup from your 1000 HTML documents.

The Python boilerpy3 library will do a fair job at this task. You can use pip to install this Python package. The main boilerpy3 webpage has several examples of its usage.

Keep both files for each URI (i.e., raw HTML and processed), and upload both sets of files to your GitHub repo. Put the raw and processed files in separate folders. Remember that to upload/commit a large number of files to GitHub, use the command line.

Sometimes boilerpy3 is unable to extract the downloaded HTML (either it's all boilerplate or it's not actually HTML), so it produces no output, resulting in a 0B size file. You may also run into HTML files that trigger UnicodeDecode exceptions when using boilerpy3. You can skip files that have these types of encoding errors, result in 0B output, or contain inappropriate content (whatever you define as such). The main goal is to have enough processed files so that you can find 10 documents that contain your query term (for Q2 and later).

Q: How many of your 1000 URIs produced useful text? If that number was less than 1000, did that surprise you?

## Answer



The example figure below shows the growth in the number of websites between 1993 and 1996.

![\label{fig:web-growth}](https://raw.githubusercontent.com/anwala/teaching-web-science/main/fall-2022/homework/hw0/growth_early_web.png)



```python
#works 
counter = 0
counter_p = 0
for i in uris:
    response = requests.get(i, verify=False)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text)
        counter += 1
        print(counter)
        print(i)  
        output_file = f"uri{counter}.html"
        with open(output_file, "w") as html_file:
            html_file.writelines(str(soup))
        output_file
        
        extractor = extractors.ArticleExtractor()
        processed_content = extractor.get_content_from_file(output_file)
        counter_p +=1
        print(processed_content)
        content_file = f"uri{counter_p}.txt"
        with open(content_file, "w") as file:
            file.writelines(str(processed_content))
        content_file
```

It seems like most of my html files contain readable text with the exception of some of them being in different languages. 

How many of your 1000 URIs produced useful text? If that number was less than 1000, did that surprise you?

Most of my URIs produced useful text, and that did not surprise me because most of my URIs collected were news articles or scholarly sites. 

In addition, I ran across a couple of problems in my function such as html errors, and after I searched these errors up, I was told I needed to install a couple of modules, such as import urllib3 in Python. 

## Discussion

To complete this task, I downloaded Python's built in functions and extentions, as well as resuing some of the prior code from hw2 to extract raw text and html files from the 1000 URIs collected from hw2. 
I wrote loops and functions to iterate through each and every text line that starts with "https://" or "http://" to get the links. After that, I examined each one and checked to see if I can store them individually into their unique .html file. After getting all the html files, I used the command, , to compress and save it in a zip file, which later I used to download onto my computer and upload it in my mac. 


# Q2 Rank with TF-IDF (4 points)

Choose a query term (e.g., "coronavirus") that is not a stop word (e.g., "the"), or super-general (e.g., "web"), or in HTML markup (e.g., "http") that is found in at least 10 of your documents. If the term is present in more than 10 documents, choose any 10 English-language documents from different domains from the result set.

Hint: You may want to use the Unix command grep -c on the processed files to help identify a good query -- it indicates the number of lines where the query appears:

## Answer

To do this task, I utilized linux commands provided such as grep -c "word" file and  wc -w file. The grep -c command finds the count of the desired words in the file you are using and the wc -w uses the total number of words presented in the file. 

I used uri96.html uri93.html uri61.html uri24.html uri17.html uri11.html uri13.html uri22.html uri25.html uri32.html. These are the results of my findings: 

```

(base) xi@Sophias-MacBook-Air-4 hw3uri % grep -c "war" uri96.html uri93.html uri61.html uri24.html uri17.html
uri96.html:30  
uri93.html:2  
uri61.html:6 
uri24.html:3
uri17.html:1  
uri11.html:1 
uri13.html:1 
uri22.html:1 
uri25.html:4 
uri32.html:1 

```

```

(base) xi@Sophias-MacBook-Air-4 hw3uri % wc -w uri96.html uri93.html uri61.html uri24.html uri17.html uri11.html uri13.html uri22.html uri25.html uri32.html

   37031 uri96.html
    6305 uri93.html
    6553 uri61.html
   11147 uri24.html
    7398 uri17.html
    647 uri11.html
    3792 uri13.html
    3615 uri22.html
    6276 uri25.html
   10073 uri32.html
   95837 total


```

To compute my TF and IDF for a certain term, 
TF is the term frequency for the number of times the word has appeared in the document. So I found the amount of times the term "war" has appeared in each of the html documents and divided each of them by the total number of words appeared. This is to avoid penalizing shorter documents. 

IDF is the inverse document frequency, and is computed by total docs in corpus/docs with term. 

IDF (term) = log2(total docs in corpus/docs with term)

Total docs in corpus = 35 Billion on google 

From google, I searched the word "war" appeared in google for 10,470,000,000 times. 

TF-IDF = TF × IDF 

IDF  = log2(total docs in corpus / docs with term)
= log2(35000000000/10470000000)
= 1.7411


Table 1. 10 Hits for the term "war".

|TF-IDF |TF |IDF  |URI
|------:|--:|---:|---
|2.35394|0.0001352  |1.7411|uri17.html https://www.live5news.com/2023/10/10/suspect-deadly-williamsburg-co-shooting-now-charged-with-murder/
|0.01975|0.0113416  |1.7411|uri22.html https://123moviesaz.top/
|0.002583|0.0014837  |1.7411|uri11.html http://www.diariopopularmg.com.br/
|0.001592|0.0009156  |1.7411|uri61.html https://cgireland.org/planned-events-for-national-allotments-community-gardens-week/
|0.0014105|0.0008101  |1.7411|uri96.html https://www.cnn.com/2023/07/14/middleeast/palestinians-mock-abbas-mime-intl/index.html 
|0.00111|0.0006373  |1.7411|uri25.html https://www.newsbreak.com/williamsburg-county-sc/3187003770457-suspect-in-williamsburg-county-homicide-facing-an-upgraded-charge-wcso
|5.5210e-4|0.0003171  |1.7411|uri93.html https://econcryptohub.com/owner-pick/hsk-2-master-mandarin-chinese-characters-workbook-volume-1-learning-chinese-new-words-pinyin-writing-stroke-order-popular-phrases-example-for-beginners-master-chinese-characters/ 
|4.686e-4|0.0002691  |1.7411|uri24.html https://abcnews.go.com/Business/wireStory/taylor-swifts-eras-tour-dances-1-box-office-103995175
|4.5913e-4|0.0002637  |1.7411|uri13.html http://www.diariopopularmg.com.br/
|1.1728e-4|0.0000993  |1.7411|uri32.html https://agenciaajn.com/noticia/israel-el-jefe-del-consejo-de-seguridad-nacional-dice-que-la-cuestion-de-los-rehenes-israelies-en-gaza-es-parte-central-de-cada-discusion-223527


# References

* grep command in Unix/Linux, <https://www.geeksforgeeks.org/grep-command-in-unixlinux/>

* Cat command in Linux with examples, <https://www.geeksforgeeks.org/cat-command-in-linux-with-examples/>

* Optimizing Jupyter Notebook: Tips, Tricks, and nbextensions <https://towardsdatascience.com/optimizing-jupyter-notebook-tips-tricks-and-nbextensions-26d75d502663>

* Download all files in a path on Jupyter notebook server <https://stackoverflow.com/questions/43042793/download-all-files-in-a-path-on-jupyter-notebook-server>

* urllib3 1.26.18 documentation <https://urllib3.readthedocs.io/en/1.26.x/user-guide.html#ssl>