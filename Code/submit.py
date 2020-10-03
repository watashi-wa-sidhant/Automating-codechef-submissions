# github : rkgeekoftheweek

from selenium import webdriver
from getpass import getpass
from configparser import ConfigParser
import time
from selenium.webdriver.common import keys, action_chains

def login_to_codechef (username,password) :
    driver = webdriver.Chrome()
    driver.get("https://www.codechef.com/")
    username_element = driver.find_element_by_id("edit-name")
    username_element.send_keys(username)
    print("Hi ", username)
    password_element = driver.find_element_by_id("edit-pass")
    password_element.send_keys(password)
    driver.find_element_by_id("edit-submit").click()
    print("Successfully logged In")
    return driver


def submit_solution (problemLink,submissionFile,driver) :
    driver.get(problemLink)
    mode = driver.find_element_by_xpath('//*[@id="edit-submit"]')
    if mode.get_attribute("value") == 'Switch to Non-IDE mode':
        mode.click()
    
    time.sleep(5)
    toggle = driver.find_element_by_id('edit_area_toggle_checkbox_edit-program')
    temp = driver.find_element_by_xpath('//*[@id="cc-footer-div"]/div[2]/div[1]/ul/li[1]/a')

    action = action_chains.ActionChains(driver)
    action.move_to_element(temp).perform()
    toggle.click()

    
    print("======================")
    with open(submissionFile, "r") as file:
        code = file.read()
    print(code)
    print("=====================")
  
    area = driver.find_element_by_xpath('//*[@id="edit-program"]')
    area.click()

    area.send_keys(keys.Keys.CONTROL + "a")
    area.send_keys(keys.Keys.DELETE)
    area.send_keys(code)
    
    time.sleep(10)
    button = driver.find_element_by_xpath('//*[@id="edit-submit-1"]')
    driver.execute_script("arguments[0].click();", button)
    
    
if __name__ == "__main__":
    parser = ConfigParser()
    parser.read('credentials.prop')
    username = parser.get('credentials', 'username')
    password=parser.get('credentials', 'password')
    problemLink =parser.get('submission', 'problemLink')
    submissionFile =parser.get('submission', 'submissionFile')
    print("=================================")
    driver = login_to_codechef(username,password)
    print("Submitting the code...")
    submit_solution(problemLink,submissionFile,driver)
    print("code submitted") 
    print("=================================")
    
    