from distutils.log import error
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


# Initialize driver
driver = webdriver.Firefox()

# Navigate to page
driver.get("http://www.htmlcanvasstudio.com/")

# Wait for element to be clickable
draw_line = WebDriverWait(driver, 20).until(
EC.element_to_be_clickable((By.XPATH, "//input[@title='Draw a line']")))
draw_line.click()
WebDriverWait(driver, 20).until(
EC.visibility_of_element_located((By.XPATH, "//input[@class='button line clicked']")))

# Calculation X and Y Points
action = ActionChains(driver)
canvas = driver.find_element_by_xpath("//*[@id='imageTemp']")
canvas_location = canvas.location
canvas_size = canvas.size
canvas_width, canvas_height = canvas_size['width'], canvas_size['height']

# Draw Vertical Line
action.move_to_element_with_offset(canvas, canvas_width/2, canvas_height-300).click().perform()
action.move_to_element_with_offset(canvas, canvas_width/2, canvas_height-100).click().perform()

# Draw Horizontal Line
action.move_to_element_with_offset(canvas, canvas_width-350, canvas_height).click().perform()
action.move_to_element_with_offset(canvas, canvas_width-150, canvas_height).click().perform()


driver.quit()