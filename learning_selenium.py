from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

# Initialize the Chrome driver
driver = webdriver.Chrome()

# Open the checkboxes page
driver.get('http://the-internet.herokuapp.com/checkboxes')

# Wait until the checkbox elements are loaded
wait = WebDriverWait(driver, 10)
checkbox1 = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="checkboxes"]/input[1]')))
checkbox2 = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="checkboxes"]/input[2]')))

# Click the checkboxes
if not checkbox1.is_selected():
    checkbox1.click()

if not checkbox2.is_selected():
    checkbox2.click()

# Open the horizontal slider page
driver.get('http://the-internet.herokuapp.com/horizontal_slider')

# Wait until the slider element is loaded
slider = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="content"]/div/div/input')))
slider_label = driver.find_element(By.XPATH, '//*[@id="range"]')

# Adjust the slider
actions = ActionChains(driver)
actions.click_and_hold(slider).move_by_offset(30, 0).release().perform()  # Adjust the offset as needed

# Open the inputs page
driver.get('http://the-internet.herokuapp.com/inputs')

# Wait until the text box element is loaded
text_box = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="content"]/div/div/div/input')))

# Set a new value in the text box
text_box.clear()
text_box.send_keys('12345')

# Close the browser
driver.quit()
