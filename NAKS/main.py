from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By


if __name__ == '__main__':
    option = Options()
    option.add_argument("--disable-infobars")
    browser = webdriver.Chrome(option)
    browser.get('https://naks.ru/registry/reg/st/?arrSORT=&arrFilter_pf%5Bnum_acst%5D%5B%5D=3173145&arrFilter_pf%5Bnum_sv%5D=%C0%D6%D1%D2-87-02805&arrFilter_DATE_ACTIVE_TO_1=&arrFilter_DATE_ACTIVE_TO_2=&arrFilter_ff%5BNAME%5D=&arrFilter_ff%5BPREVIEW_TEXT%5D=&set_filter=%D4%E8%EB%FC%F2%F0&set_filter=Y')
    #html_text = browser.page_source
    #root = BeautifulSoup(html_text, 'html.parser')
    elements = browser.find_element(By.CLASS_NAME, 'zagolovok-tabl')
    print(elements.text)
    elem = browser.find_element_by_xpath(By.xpath, "//tr[@style='bgcolor:#eff7ff;']")
    print(elements.text)




