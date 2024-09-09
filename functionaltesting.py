from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pyautogui
import os

# Initialize the WebDriver
driver = webdriver.Chrome()
wait = WebDriverWait(driver, 20)

# URL and credentials
url = 'https://demo.dealsdray.com/'
username = 'prexo.mis@dealsdray.com'
password = 'prexo.mis@dealsdray.com'

# Path of the Excel file to be uploaded
file_name = "demo-data.xlsx"  # File name to select
file_path = os.path.join(os.path.expanduser('~'), 'Downloads', file_name)  # Default downloads folder

try:
    # Open the website
    driver.get(url)
    
    # Locate the username and password fields and log in
    wait.until(EC.presence_of_element_located((By.NAME, 'username'))).send_keys(username)
    wait.until(EC.presence_of_element_located((By.NAME, 'password'))).send_keys(password, Keys.RETURN)

    # Navigate to Orders section from the left dashboard
    wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='root']/div/div/div[1]/div/div[1]/button"))).click()
    wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='root']/div/div[1]/div/div[2]/div[1]/div[2]/button"))).click()
    wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='root']/div/div[1]/div/div[2]/div[1]/div[2]/div/div[1]/a/button"))).click()

    # Click on the right side of the screen to focus it
    time.sleep(1)  # Small delay to ensure elements are properly loaded
    driver.find_element(By.XPATH, "//body").click()  # Clicking on the body of the page to remove any overlay/focus issue

    # Click on 'Add Bulk Order' button
    wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='root']/div/div/div[2]/div/div/div[2]/div[2]/button"))).click()
    
    # Upload the Excel file
    wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='root']/div/div/div[2]/div/div/div[2]/div[3]/div/div"))).click()

    # Wait for the file picker dialog to appear
    time.sleep(2)

    # Automate the file selection using PyAutoGUI
    pyautogui.write(file_path)  # Types the full path of the file
    pyautogui.press('enter')    # Presses Enter to open the file

    # Click on the 'Import' button
    wait.until(EC.presence_of_element_located((By.XPATH, "//button[contains(text(),'Import')]"))).click()

    # Click the 'Validate' button after the file is uploaded
    wait.until(EC.presence_of_element_located((By.XPATH, "//button[contains(text(),'Validate')]"))).click()

    # Take a screenshot of the entire page
    time.sleep(2)  # Give some time for the page to render fully
    pyautogui.press('enter')
    driver.save_screenshot('validation_page_screenshot.png')
    print("Screenshot saved as 'validation_page_screenshot.png'.")

finally:
    # Close the browser
    driver.quit()
