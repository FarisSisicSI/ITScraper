import requests
from bs4 import BeautifulSoup


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
