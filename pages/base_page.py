from selenium import webdriver
from locators import BasePageLocators

class BasePage():

    def __init__(self, driver):
        self.driver = driver

    def nav_to_etsy(self, url='https://www.etsy.com'):
        self.driver.get(url)
        return self.driver.find_element(*BasePageLocators.ETSY_LOGO)