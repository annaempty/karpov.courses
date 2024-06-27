from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def open_web(html):
    option = Options()
    option.add_argument("--disable-infobars")
    browser = webdriver.Chrome(option)
    browser.get(html)
    return browser


def find_table_by_date(browser, date_from, date_to):
    # id первой кнопки аттестации до - arrFilter_DATE_ACTIVE_TO_1
    elem_data_1 = browser.find_element(By.ID, 'arrFilter_DATE_ACTIVE_TO_1')
    elem_data_1.send_keys(date_from + Keys.RETURN)
    # id второй кнопки аттестации до -arrFilter_DATE_ACTIVE_TO_2
    time.sleep(4)
    elem_data_1 = browser.find_element(By.ID, 'arrFilter_DATE_ACTIVE_TO_2')
    elem_data_1.send_keys(date_to + Keys.RETURN)
    time.sleep(10)
    # class кнопки фильтр inputbuttonflat
    # На кнопку фильтр тыкать не нужно, фильтруется после ввода дат
    # browser.find_element(By.CLASS_NAME, 'inputbuttonflat').click()
    # time.sleep(10)
    html_text = browser.page_source
    return browser, html_text


def switch_webpage(browser):
    staff = browser.find_element(By.CLASS_NAME, 'all-staff')
    staff.find_element(By.CLASS_NAME)