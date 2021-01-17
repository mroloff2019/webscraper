from urllib.request import urlopen
from bs4 import BeautifulSoup


url_to_scrap = ""

request_page = urlopen(url_to_scrap)
page_html = request_page.read()
request_page.close()

html_soup = BeautifulSoup(page_html, '')

job_items = html_soup.find_all('div', class_="").text

filename = 'jobs.csv'
f= open(filename, 'w')

headers = 'Title \n'

f.write(headers)


for job in job_items:
	title = job.find('div', class_="").text
	title = job.find('div', class_="").text

f.write(title)
f.close()
