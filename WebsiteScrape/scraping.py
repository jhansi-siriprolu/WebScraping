import requests
from bs4 import BeautifulSoup
import codecs

class Scrape:
    def __init__(self, url):
        self.url = url
        self.response = requests.get(self.url)

    def __str__(self):
        return f"Scraping Website {self.url}"

    def get_headers(self):
        print("HEADERS:", self.response.headers)

    def response(self):        
        print("Response: ", self.response)
        print("GET URL:", self.response.url)

    def status_code(self):
        print("Status Code:", self.response.status_code)

    def make_soup(self):
        self.soup = BeautifulSoup(self.response.text)

    def get_details(self, tag_name = "div", class_name = "quote"):
        self.make_soup()
        featured_items = self.soup.find_all(tag_name, class_=class_name)
        for each_item in featured_items:
            print(each_item.text)
            
    def links(self):
        links = self.soup.find_all('a')
        for link in links:
            print(link.text, link.get('href'))

    def get_text(self):
        with codecs.open("windom_pets.txt","w",encoding = 'utf-8') as f:
            f.write(self.soup.prettify())
if __name__ == "__main__":
    website1 = Scrape(url = "http://thisisasite.net/")
    print(website1)
    # website1.response()
    website1.status_code()
    website1.get_headers()
    website1.get_details(class_name = "info col-xs-8 col-xs-offset-2 col-sm-7 col-sm-offset-0 col-md-6 col-lg-8")
    website1.links()
    website1.get_text()