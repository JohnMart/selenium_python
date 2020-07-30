import web_utils
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from base_page import BasePage
from locators import SearchPageLocators

class SearchPage(BasePage):

    def __init__(self, driver):
        self.driver = driver
    
    def search_for_item(self, item='handbags'):
        #set the search bar text, click the search button, verify the search results are returned.
        self.driver.find_element(*SearchPageLocators.SEARCH_TEXTBOX).send_keys(item)
        self.driver.find_element(*SearchPageLocators.SEARCH_BUTTON).click()
        return self.driver.find_element(*SearchPageLocators.SEARCH_RESULTS).text.strip() == item

    def search_for_category(self, category='Clocks'):
        #locate and hover on the category link/section element.
        top_nav_element = self.driver.find_element(*SearchPageLocators.TOP_NAV_CATEGORY_LINK)
        web_utils.hover_on_element(self.driver, top_nav_element)
        
        #wait for the visibility of the sub category link, click it, and verify the search results are returned.
        sub_category_link = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//div[@data-ui='sub-nav-container']//li//a[@role='menuitem' and contains(text(), '"+ category +"')]")))
        sub_category_link.click()
        return self.driver.find_element_by_xpath("//div[@id='content']//h1[text()='"+ category +"']")