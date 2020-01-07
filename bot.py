from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from random import randint
from login_info import username, password

class InstaBot:
    def __init__(self, username, pw):
        self.driver = webdriver.Chrome()
        self.driver.get('https://instagram.com')
        sleep(2)
        # login button on home page
        self.driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[2]/p/a').click()
        sleep(3)
        # username field
        self.driver.find_element_by_xpath('//input[@name=\"username\"]').send_keys(username)
        # password field
        self.driver.find_element_by_xpath('//input[@name=\"password\"]').send_keys(pw)
        # submit button
        self.driver.find_element_by_xpath('//button[@type=\"submit\"]').click()
        sleep(5)
        # close pop up
        self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div[3]/button[2]").click()
        sleep(2)

    def search_query(self, query):
        self.driver.find_element_by_xpath('/html/body/div[1]/section/nav/div[2]/div/div/div[2]/input').send_keys(query)
        sleep(2)
        self.driver.find_element_by_xpath('/html/body/div[1]/section/nav/div[2]/div/div/div[2]/input').send_keys(Keys.ENTER)
        self.driver.find_element_by_xpath('/html/body/div[1]/section/nav/div[2]/div/div/div[2]/input').send_keys(Keys.ENTER)
        sleep(5)

    def like_images(self,likes):
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[1]/div/div/div[1]/div[1]/a/div/div[2]").click()
        sleep(2)
        current_like = 0
        while current_like <= likes:
            self.driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/article/div[2]/section[1]/span[1]/button").click()
            sleep(randint(1,6))
            self.driver.find_element_by_xpath("//a[contains(text(), 'Next')]").click()
            sleep(1)
            current_like += 1  



my_bot = InstaBot(username,password)
my_bot.search_query("#vigia")
my_bot.like_images(5)