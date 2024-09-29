import requests
from bs4 import BeautifulSoup

#Scraper dio koda koji izvlaci podatke sa ITVesti.info
class NewsScraper:
    def __init__(self, url):
        self.url = url

    def scrape(self):
        response = requests.get(self.url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')

            post_link_element = soup.select_one('.blog-posts .post-title a')
            post_url = post_link_element['href']

            post_response = requests.get(post_url)
            post_soup = BeautifulSoup(post_response.content, 'html.parser')
            post_content_element = post_soup.select_one('.post .post-body p')
            content = post_content_element.get_text(strip=True)

            return content

#Scraper dio koda koji izvlaci podatke sa Zenicablog.com
class ChScraper:
    def __init__(self, url):
        self.url = url

    def scrape(self):
        response = requests.get(self.url)
        if response.status_code == 200:

            soup = BeautifulSoup(response.content, 'html.parser')
            post_link_element = soup.select_one('.entry-title a')
            post_url = post_link_element['href']

            post_response = requests.get(post_url)
            post_soup = BeautifulSoup(post_response.content, 'html.parser')
            post_content_element = post_soup.select('.col-lg-10 p')
            content1 = '\n'.join([p.get_text(strip=True) for p in post_content_element])


            return content1
