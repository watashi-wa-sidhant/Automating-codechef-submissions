# github : rkgeekoftheweek

from selenium import webdriver
from getpass import getpass
from configparser import ConfigParser
import time


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
    driver.find_element_by_id("edit-submit").click()
    time.sleep(10)
    driver.find_element_by_id("edit_area_toggle_checkbox_edit-program").click()
   
    with open(submissionFile, "r") as file:
        code = file.read()
    print(code)
    print("========")
    code_element = driver.find_element_by_id("edit-program")
    code_element.send_keys(code)
    
    time.sleep(10)
    driver.find_element_by_id("edit-submit-1").click()
    
    
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
    driver.find_element_by_id("oauth-login-form").click()
    print("{0} logged out".format(username))  
    print("=================================")
    
    