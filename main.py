# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re, random, glob, os, zipfile

what_is_download = [
    '80-55555555'
    , '80-66666666'
    , '80-77777777'
 ]


def chek_text_and_click(driver, xpath):
    i = 0
    while (i < 1000):
        try:
            print driver.find_element_by_xpath(xpath).click()
            break
        except:
            pass
        time.sleep(5)

        i = +1


def check_status(driver):
    status_download = u"Завершена"
    xpath_status_now = "//div[@id='v-Z7_01HA1A42KODT90AR30VLN22003']/div/div[2]/div/div[2]/div/div/div/div/div/div/div/div[3]/div/div/div[2]/div/table/tbody/tr/td[3]/div/div/div/div/div/div"
    xpath_download = "//div[@id='v-Z7_01HA1A42KODT90AR30VLN22003']/div/div[2]/div/div[2]/div/div/div/div/div/div/div/div[3]/div/div/div[2]/div/table/tbody/tr/td[4]/div/div/a/img"
    status_now = driver.find_element_by_xpath(xpath_status_now).text
    print status_now
    if status_now == status_download:
        driver.find_element_by_xpath(xpath_download).click()  # download скачать
        time.sleep(random.random())


def delete_sig(path_default):
    list_file = glob.glob(path_default + u"*.sig")
    if list_file:
        for file_name in list_file:
            os.remove(file_name)


def get_unzip(path_default, path_extract):
    list_file = glob.glob(path_default + u"*.zip")
    if list_file:
        for file_name in list_file:
            unzipper = zipfile.ZipFile(file_name)
            if path_extract:
                unzipper.extractall(path_extract)
            else:
                unzipper.extractall(path_default)
            unzipper.close()
            os.remove(file_name)


def download_every_one(driver):
    num = 1
    for number_what_download in what_is_download:
        print number_what_download, num
        num += 1
        driver.find_element_by_xpath("(//input[@type='text'])[3]").click()
        driver.find_element_by_xpath("(//input[@type='text'])[3]").clear()
        driver.find_element_by_xpath("(//input[@type='text'])[3]").send_keys(number_what_download)
        time.sleep(random.random())
        xpath_refresh = "//div[@id='v-Z7_01HA1A42KODT90AR30VLN22003']/div/div[2]/div/div[2]/div/div/div/div/div/div/div/div[2]/div/div/div/div[2]/div/div/div/div[2]/div/div/span/span"
        driver.find_element_by_xpath(xpath_refresh).click()  # refresh обновить
        xpath_now_number_response = "//div[@id='v-Z7_01HA1A42KODT90AR30VLN22003']/div/div[2]/div/div[2]/div/div/div/div/div/div/div/div[3]/div/div/div[2]/div/table/tbody/tr/td/div"

        i = 0
        while i < 1000:
            try:
                now_number_response = driver.find_element_by_xpath(xpath_now_number_response).text
                if number_what_download == now_number_response:
                    check_status(driver)
                    break
            except:
                pass
                time.sleep(random.random())
                i += 1


def pwd(driver):
    # enter
    # you key format 99cc99cc - 5555 - 6666 - 7777 - 999rr99rrr9r
    driver.find_element_by_xpath("(//input[@type='text'])[2]").click()
    driver.find_element_by_xpath("(//input[@type='text'])[2]").send_keys('99cc99cc')
    time.sleep(random.random() + 1)
    driver.find_element_by_xpath("(//input[@type='text'])[3]").click()
    driver.find_element_by_xpath("(//input[@type='text'])[3]").send_keys('5555')
    time.sleep(random.random() + 1)
    driver.find_element_by_xpath("(//input[@type='text'])[4]").click()
    driver.find_element_by_xpath("(//input[@type='text'])[4]").send_keys('6666')
    time.sleep(random.random() + 1)
    driver.find_element_by_xpath("(//input[@type='text'])[5]").click()
    driver.find_element_by_xpath("(//input[@type='text'])[5]").send_keys('7777')
    time.sleep(random.random() + 1)
    driver.find_element_by_xpath("(//input[@type='text'])[6]").click()
    driver.find_element_by_xpath("(//input[@type='text'])[6]").send_keys('999rr99rrr9r')
    time.sleep(random.random() + 1)
    xpath_enter = "//div[@id='v-Z7_01HA1A42KODT90AR30VLN22003']/div/div[2]/div/div[2]/div/div/div/div/div/div/div/div[2]/div/div/div/div/div/div/div/div/div/div/span/span"
    driver.find_element_by_xpath(xpath_enter).click()
    time.sleep(random.random() + 1)
    xpath_my_question = "//div[@id='v-Z7_01HA1A42KODT90AR30VLN22003']/div/div[2]/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div[2]/div/div/span/span"
    chek_text_and_click(driver, xpath_my_question)
    xpath_title_number_question = "//div[@id='v-Z7_01HA1A42KODT90AR30VLN22003']/div/div[2]/div/div[2]/div/div/div/div/div/div/div/div/div/div/div/div[2]/div/div/div/div/div/div"
    i = 0
    while (i < 1000):
        try:
            print "find title " + driver.find_element_by_xpath(xpath_title_number_question).text
            download_every_one(driver)
            break
        except:
            pass
        time.sleep(5)

        i = +1
    #





chromeOptions = webdriver.ChromeOptions()
path_download = "C:/xampp/htdocs/delete/tmp/"# where download fiels
path_xml_in = "C:/xampp/htdocs/delete/XMLtoCSV/in/" # extractall path xml fiels
path_xml_out = "C:/xampp/htdocs/delete/XMLtoCSV/out/"

prefs = {"download.default_directory": path_download}  # where download fiels
chromeOptions.add_experimental_option("prefs", prefs)

driver = webdriver.Chrome(executable_path='C:\chromedriver\chromedriver.exe', chrome_options=chromeOptions) # path chromedriver.exe
driver.implicitly_wait(30)

driver.get('https://rosreestr.ru/wps/portal/p/cc_present/ir_egrn')
pwd(driver)
time.sleep(5) # for download last file
driver.quit()

get_unzip(path_download, "")
delete_sig(path_download)
get_unzip(path_download, path_xml_in)
time.sleep(5)

