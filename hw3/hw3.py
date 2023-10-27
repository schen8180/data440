import requests
from bs4 import BeautifulSoup
from boilerpy3 import extractors

import sys
sys.setrecursionlimit(1500)

extractor = extractors.ArticleExtractor()

file_path = "my1000_links.txt"

with open(file_path, "r") as file:
    uris = [line.strip() for line in file]
#works 
counter = 0
counter_p = 0
for i in uris:
    response = requests.get(i)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text)
        counter += 1
        print(counter)
        print(i)  
        output_file = f"uri{counter}.html"
        with open(output_file, "w") as html_file:
            html_file.writelines(str(soup))
        output_file
    
        
        
        processed_content = extractor.get_content_from_file(output_file)
        counter_p +=1
        print(processed_content)
        content_file = f"uri{counter_p}.txt"
        with open(content_file, "w") as file:
            file.writelines(str(processed_content))
        content_file