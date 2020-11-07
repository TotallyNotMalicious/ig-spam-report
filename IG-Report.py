import os
import time
from selenium import webdriver as wd
from selenium.webdriver.chrome.options import Options

def main(gayuser, gayname, delay):
    times_reported = 0
    while True:
        options = Options()
        options.headless = False
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        driver = wd.Chrome('chromedriver.exe', options=options)

        driver.get('https://help.instagram.com/contact/723586364339719')
        driver.find_element_by_xpath('//input[@name="Field258021274378282"]').send_keys(gayuser)
        driver.find_element_by_xpath('//input[@name="Field735407019826414"]').send_keys(gayname)
        driver.find_element_by_xpath('//span[@class="_55pe"]').click()
        driver.find_element_by_xpath('//ul[@class="_54nf"]//a[@title="2008"]').click()
        driver.find_element_by_xpath('//a[@class="_p _55pi _5vto _55_p _2agf _4o_4 _4jy0 _4jy3 _517h _51sy _42ft"]//span[@class="_55pe"]').click()
        driver.find_element_by_xpath('//a[@title="February"]//span[@class="_54nh"]').click()
        driver.find_element_by_xpath('//a[@class="_p _55pi _5vto _55_p _2agf _4o_4 _4jy0 _4jy3 _517h _51sy _42ft"]//span[@class="_55pe"]').click()
        driver.find_element_by_xpath('//a[@title="9"]//span[@class="_54nh"]').click()
        driver.find_element_by_xpath('//select[@id="294540267362199"]//option[@value="Other"]').click()
        driver.find_element_by_xpath('//button[@class="_42ft _4jy0 _4jy4 _4jy1 selected _51sy"]').click()
        time.sleep(4)
        driver.close()
        times_reported += 1
        os.system('cls')
        print(f'Sent {times_reported} Reports Successfully')
        time.sleep(delay)

def getthegoodies():
    os.system('title IG Spam Report')
    os.system('cls')
    gayuser = input('Users @: ')
    os.system('cls')
    gayname = input('Users Full Name: ')
    os.system('cls')
    delay = int(input('Delay Between Reports: '))
    os.system('cls')
    main(gayuser, gayname, delay)

getthegoodies()
