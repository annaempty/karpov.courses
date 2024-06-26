from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
import pandas as pd
from select_date import find_table_by_date, open_web, switch_webpage



def find_table_body(html_text):
    root = BeautifulSoup(html_text, 'html.parser')
    field = root.find('div', {"class": "col-md-8 col-xl-9 order-2 order-md-1"})
    table = field.find('table', {'class': 'tabl'})
    tbody = table.find('tbody')
    tbody_r = tbody.find_all('tr')
    return tbody_r


def read_title(tbody_r):
    dict_colum = {}
    flag = 0
    for i in tbody_r:
        tbody_d = i.find_all('td')
        number = 0
        for j in tbody_d:
            if flag < 9:
                dict_colum[number] = j.text.strip()
                flag += 1
            else:
                return dict_colum


def read_data(tbody_r):
    dict_tail = {0: [], 1: [], 2: [], 3: [], 4: [], 5: [],
                 6: [], 7: [], 8: []}
    flag = 0
    for i in tbody_r:
        tbody_d = i.find_all('td')
        number = 0
        for j in tbody_d:
            if flag < 9:
                flag = 10
                break
            else:
                dict_tail[number].append(j.text.strip())
            number += 1
    df = pd.DataFrame(dict_tail)
    return df


if __name__ == '__main__':
    # Необходимо будет вынести в текстовый файл:
    html = 'https://naks.ru/registry/reg/st/?arrSORT=&arrFilter_pf%5Bnum_acst%5D%5B%5D=3173145&arrFilter_pf%5Bnum_sv%5D=%C0%D6%D1%D2-87-&arrFilter_DATE_ACTIVE_TO_1=&arrFilter_DATE_ACTIVE_TO_2=&arrFilter_ff%5BNAME%5D=&arrFilter_ff%5BPREVIEW_TEXT%5D=&set_filter=%D4%E8%EB%FC%F2%F0&set_filter=Y'
    date_from = '01.01.2024'
    date_to = '31.12.2024'

    browser = open_web(html)
    browser, html_text = find_table_by_date(browser, date_from, date_to)
    start_table = find_table_body(html_text)
    dict_columns = read_title(start_table)
    df = read_data(start_table)
    df.rename(columns=dict_columns)
    df.to_csv('naks.csv', sep=';')
    #elements = browser.find_element(By.CLASS_NAME, 'zagolovok-tabl')
    #class ="col-md-8 col-xl-9 order-2 order-md-1"






