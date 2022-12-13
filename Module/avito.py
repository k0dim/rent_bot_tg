from time import sleep

from loguru import logger
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

def gotolink():
    ua = dict(DesiredCapabilities.CHROME)
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('window-size=1920x935')
    browser = webdriver.Chrome(chrome_options=options)
    return browser

def get_name(ad_all):
    next_class = ad_all.find_element(By.CLASS_NAME, 'iva-item-titleStep-pdebR')
    text = next_class.find_element(By.TAG_NAME, 'a').text
    return text

def get_href(ad_all):
    next_class = ad_all.find_element(By.CLASS_NAME, 'iva-item-titleStep-pdebR')
    href = next_class.find_element(By.TAG_NAME, 'a').get_attribute("href")
    return href

def get_price(ad_all):
    price = ad_all.find_element(By.CLASS_NAME, 'iva-item-priceStep-uq2CQ').text
    return price

def get_geo(ad_all):
    geo = ad_all.find_element(By.CLASS_NAME, 'iva-item-developmentNameStep-qPkq2').text
    return geo

def get_photo(ad_all):
    URL = get_href(ad_all)
    browser = gotolink()
    browser.get(URL)
    next_class = browser.find_element(By.CLASS_NAME, 'image-frame-wrapper-_NvbY')
    photo = next_class.find_element(By.TAG_NAME, 'img').get_attribute("src")
    return photo

def get_deposit(ad_all):
    URL = get_href(ad_all)
    browser = gotolink()
    browser.get(URL)
    next_class = browser.find_element(By.CLASS_NAME, 'style-item-price-sub-price-_5RUD')
    deposit = next_class.text
    return deposit

def main(driver, URL, PAUSE_DURATION_SECONDS):
    driver.get(URL)
    logger.info(f"Success: Подключились, начинаем парсить")
    sleep(PAUSE_DURATION_SECONDS)
    ad_all = driver.find_element(By.CLASS_NAME, "iva-item-content-rejJg") 

    dict_ad = {
        'name':get_name(ad_all),
        'href':get_href(ad_all),
        'price':get_price(ad_all),
        'geo':get_geo(ad_all),
        'photo':get_photo(ad_all),
        'deposit':get_deposit(ad_all),
    } 
    return dict_ad


def avito_main():
    URL = 'https://www.avito.ru/samara/kvartiry/sdam/na_dlitelnyy_srok-ASgBAgICAkSSA8gQ8AeQUg?district=794-795-796-797-798-799-801&f=ASgBAQECAkSSA8gQ8AeQUgFAzAg0kFmOWYxZAUXGmgwVeyJmcm9tIjowLCJ0byI6MjAwMDB9&i=1&s=104&user=1'
    PAUSE_DURATION_SECONDS = 150
    try:
        browser = gotolink()
        text = main(browser,URL,PAUSE_DURATION_SECONDS)
        logger.info(f"Success: {text}")
    except Exception as e:
        print(e)
        logger.debug(f"Error: {e}")
    finally:
        browser.quit()
    return text

if __name__ == '__main__':
   print(avito_main())