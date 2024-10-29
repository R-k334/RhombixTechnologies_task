import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

class infow():
    def __init__(self):
        service = Service(r'C:\Users\Shaqa\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe')
        self.driver = webdriver.Chrome(service=service)

    def get_info(self, query):
        self.query = query
        self.driver.get(url="https://www.wikipedia.org")
        search = self.driver.find_element("xpath", '//*[@id="searchInput"]')
        search.click()
        search.send_keys(query)
        enter = self.driver.find_element("xpath", '//*[@id="search-form"]/fieldset/button')
        enter.click()
        time.sleep(200000)  