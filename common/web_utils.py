from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

def hover_on_element(driver, element):
    action = ActionChains(driver)
    action.move_to_element(element).perform()