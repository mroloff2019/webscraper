# webscraper
You will need BeautifulSoup4 on your machine to run this python program.
This script is a basic web scraper that will take the the title and the price of products on a website. 

1. Please add website to this variable: url_to_scrap = ""
2. ('div', class_="") add the class of the contents you want to scrape. 
3. Fill out the class in these variables: 
title = job.find('div', class_="").text
price = job.find('div', class_="").text
