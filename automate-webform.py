from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

bridge = webdriver.Chrome()
bridge.implicitly_wait(20)
bridge.get("https://www.selenium.dev/selenium/web/web-form.html")

inputtext = bridge.find_element(By.CSS_SELECTOR,'#my-text-id')
inputtext.send_keys("automation testing")
time.sleep(1)

password = bridge.find_element(By.NAME,"my-password")
password.send_keys("uthyfkl")
time.sleep(1)

textarea = bridge.find_element(By.NAME,"my-textarea")
textarea.send_keys('Automation testing with selenium in python')
time.sleep(1)

dropdown = Select(bridge.find_element(By.NAME,"my-select"))
dropdown.select_by_visible_text('Two')
time.sleep(1)

datalist = bridge.find_element(By.NAME,"my-datalist")
datalist.send_keys('New York')
time.sleep(1)

file = bridge.find_element(By.NAME,"my-file")
file.send_keys("C:\\Users\\chara\\Downloads\\hall_ticket (1).pdf")
time.sleep(1)

checkbox = bridge.find_element(By.ID,'my-check-2')
checkbox.click()
time.sleep(1)

radio = bridge.find_element(By.ID,'my-radio-2')
radio.click()
time.sleep(1)

datepicker = bridge.find_element(By.NAME,"my-date")
datepicker.click()

months = bridge.find_element(By.CSS_SELECTOR,".datepicker-switch")
months.click()
time.sleep(1)

janmonth = bridge.find_element(By.XPATH,"//span[text() = 'Jan']")
janmonth.click()

date = bridge.find_element(By.XPATH,"//td[text() = '17']")
date.click()

submitBtn = bridge.find_element(By.XPATH,"//button[@type = 'submit']")
submitBtn.click()



time.sleep(10)
