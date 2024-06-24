import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Path to the msedgedriver executable
EDGE_DRIVER_PATH = r'C:\Users\WELCOME\Downloads\edgedriver_win64\msedgedriver.exe'

# URL and login credentials
URL = 'https://www.saucedemo.com/'
USERNAME = 'standard_user'
PASSWORD = 'secret_sauce'

def initialize_driver():
    """
    Initialize the Microsoft Edge WebDriver.
    """
    edge_service = EdgeService(executable_path=EDGE_DRIVER_PATH)
    edge_options = webdriver.EdgeOptions()
    return webdriver.Edge(service=edge_service, options=edge_options)

def print_cookies(driver, message):
    """
    Print the cookies stored in the browser.
    """
    cookies = driver.get_cookies()
    print(f"{message}:")
    for cookie in cookies:
        print(cookie)
    print("="*50)

def login(driver):
    """
    Perform login operation on saucedemo.com.
    """
    driver.get(URL)
    
    # Wait for the username field to be present
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'user-name')))
    
    # Find username and password fields, and login button
    username_field = driver.find_element(By.ID, 'user-name')
    password_field = driver.find_element(By.ID, 'password')
    login_button = driver.find_element(By.ID, 'login-button')
    
    # Enter username and password, then click login
    username_field.send_keys(USERNAME)
    password_field.send_keys(PASSWORD)
    login_button.click()

    # Wait for the page to load after login (adjust time as needed)
    WebDriverWait(driver, 10).until(EC.title_contains('Swag Labs'))

def logout(driver):
    """
    Perform logout operation on saucedemo.com.
    """
    # Open the menu and click on the logout button
    menu_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, 'react-burger-menu-btn'))
    )
    menu_button.click()
    
    # Wait for the logout link to be clickable
    logout_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, 'logout_sidebar_link'))
    )
    logout_link.click()

def main():
    """
    Main function to perform login, display cookies, and logout.
    """
    driver = initialize_driver()

    try:
        # Display cookies before login
        driver.get(URL)
        print_cookies(driver, "Cookies before login")

        # Perform login
        login(driver)

        # Display cookies after login
        print_cookies(driver, "Cookies after login")

        # Perform logout
        logout(driver)
        
        # Display cookies after logout
        print_cookies(driver, "Cookies after logout")

    finally:
        # Close the browser window
        driver.quit()

if __name__ == "__main__":
    main()
