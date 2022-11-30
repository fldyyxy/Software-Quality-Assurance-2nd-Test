#Test case: User want to register on Facebook. 
#Test data:
 # •	First name: Faldinando 
 # •	Surname : Malelak
 # •	Email address: faldomalelak251199@gmail.com
 # •	Password: Tester0000
 # •	Date of birth: May 7th, 1999
 # •	Gender: Male
 
#Here is the script I create with selenium and pyhton

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://en-gb.facebook.com/reg/')
driver.implicitly_wait(10)
driver.find_element(By.NAME,"firstname").send_keys("Faldinando")
driver.find_element(By.NAME,"lastname").send_keys("Malelak")
driver.find_element(By.NAME,"reg_email__").send_keys("faldinando251199@gmail.com")
driver.find_element(By.NAME,"reg_email_confirmation__").send_keys("faldinando251199@gmail.com")
driver.find_element(By.ID,"password_step_input").send_keys("Tester0000")
sel = Select(driver.find_element(By.XPATH,"//select[@title='Day']"))
sel.select_by_visible_text("7")
sel = Select(driver.find_element(By.XPATH,"//select[@title='Month']"))
sel.select_by_visible_text("May")
sel = Select(driver.find_element(By.XPATH,"//select[@title='Year']"))
sel.select_by_visible_text("1999")
driver.find_element(By.XPATH,"//label[text()='Male']").click()
driver.find_element(By.XPATH,"//button[text()='Sign Up']").click()
