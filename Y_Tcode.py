
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

class Music:
    def __init__(self):
        service = Service(r'C:\Users\Shaqa\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe')
        self.driver = webdriver.Chrome(service=service)

    def play(self, query):
        
        print(f"Searching for: {query}")
        
        self.driver.get(url="https://www.youtube.com/results?search_query=" + query)
        time.sleep(3)  
        
        try:
            video = self.driver.find_element(By.XPATH, '(//*[@id="video-title"])[1]')
            video.click()
        except Exception as e:
            print(f"Error finding video: {e}") 