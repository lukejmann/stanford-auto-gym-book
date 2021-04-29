from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import datetime
import time


driver = webdriver.Chrome('./chromedriver')
driver.get("https://recwell.stanford.edu/")
wait = WebDriverWait(driver, 100)
wait.until(EC.visibility_of_element_located(
    (By.CSS_SELECTOR, '#logoutForm')))

while(1 == 1):
    curr_time = time.localtime()
    curr_clock = time.strftime("%H:%M:%S", curr_time)
    print(curr_clock)
    if(curr_clock[0:5] == "00:00"):
        print("running!")
        driver.get('https://recwell.stanford.edu/booking')
        text_lines = driver.find_elements_by_xpath(
            "//*[contains(text(), 'AOERC Fitness Center')]")
        a_line = text_lines[0].find_element_by_xpath("..")
        booking_url = a_line.get_attribute("href")
        driver.get(booking_url)
        today = datetime.date.today()
        tomm = today + datetime.timedelta(days=1)
        tomm_date = tomm.day
        sel_string = f'button[data-day="{tomm_date}"]'
        driver.implicitly_wait(1)
        tomm_buttoms = driver.find_elements_by_css_selector(sel_string)
        driver.implicitly_wait(1)
        tomm_buttoms[1].click()
        driver.implicitly_wait(3)
        cont = driver.find_element_by_css_selector(
            '.booking-slot-item[data-slot-number="8"]')
        driver.implicitly_wait(3)
        button_cont = cont.find_elements_by_class_name(
            "booking-slot-action-item")
        buttons = button_cont[0].find_elements_by_class_name("btn")
        buttons[0].click()
        print("booked!")
        time.sleep(60)
    else:
        time.sleep(30)
