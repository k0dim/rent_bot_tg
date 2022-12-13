from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from datetime import datetime
from loguru import logger

def main(driver, URL, PAUSE_DURATION_SECONDS):
    # driver.get(URL)
    driver.get(URL)
    # logger.info(f"Success: Подключились, начинаем парсить")
    sleep(PAUSE_DURATION_SECONDS)

    article = driver.find_element(By.TAG_NAME, "article")
    get_ad = article.find_element(By.XPATH, '//div[@data-name="LinkArea"]') # Циклом проходим по каждому объявлению
    
    # get_block = get_ad.find_element(By.CLASS_NAME, "_93444fe79c--content--lXy9G") # В каждом объявлении залетаем в тэг 'span'
    # get_block_detal = get_block.find_element(By.CLASS_NAME, "_93444fe79c--general--BCXJ4") # В каждом объявлении залетаем в тэг 'span'
    # get_href = get_block_detal.find_element(By.TAG_NAME, "a").get_attribute("href")


    # get_href = get_block_detal.find_element(By.CSS_SELECTOR, "#frontend-serp > div > div._93444fe79c--wrapper--W0WqH > article:nth-child(1) > div._93444fe79c--card--ibP42 > div._93444fe79c--content--lXy9G > div._93444fe79c--general--BCXJ4 > div > a").get_attribute("href")


    # ad_text_href = ad_all.find_element(By.CLASS_NAME, 'iva-item-titleStep-pdebR')
    # get_info_tag_a = ad_text_href.find_element(By.TAG_NAME, 'a') # В каждом объявлении залетаем в тэг 'a'

    # text = get_info_tag_a.text # В тэге достаем текст объявления
    # href = get_info_tag_a.get_attribute("href") # В тэге достаем ссылку на объявление

    # price = ad_all.find_element(By.CLASS_NAME, 'iva-item-priceStep-uq2CQ').text # Достаем цену

    # date = ad_all.find_element(By.CLASS_NAME, 'date-root-__9qz').text # Достаем дату публикации

    # geo = ad_all.find_element(By.CLASS_NAME, 'iva-item-developmentNameStep-qPkq2').text # Достаем адрес

    # dict_ad = {
    #     'name':text,
    #     'href':href,
    #     'price':price,
    #     'geo':geo,
    #     'date':date,
    #     #'photo':photo,
    #     'date_add':datetime.now()
    # } # Для удобства все собрали вместе
    # return dict_ad
    print(get_ad)
    return

def cian_main():
    URL = 'https://samara.cian.ru/cat.php?currency=2&deal_type=rent&engine_version=2&maxprice=20000&offer_type=flat&region=4966&room1=1&room2=1&room9=1&sort=creation_date_desc&type=4'
    PAUSE_DURATION_SECONDS = 5
    try:
        ua = dict(DesiredCapabilities.CHROME)
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        options.add_argument('window-size=1920x935')
        browser = webdriver.Chrome(chrome_options=options)

        text = main(browser,URL,PAUSE_DURATION_SECONDS)
        
        # logger.info(f"Success: {text}")
    except Exception as e:
        print(e)
        # logger.debug(f"Error: {e}")
    finally:
        browser.quit()
    return text

if __name__ == '__main__':
    URL = 'https://samara.cian.ru/cat.php?currency=2&deal_type=rent&engine_version=2&maxprice=20000&offer_type=flat&region=4966&room1=1&room2=1&room9=1&sort=creation_date_desc&type=4'
    PAUSE_DURATION_SECONDS = 5
    try:
        ua = dict(DesiredCapabilities.CHROME)
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        options.add_argument('window-size=1920x935')
        browser = webdriver.Chrome(chrome_options=options)

        main(browser,URL,PAUSE_DURATION_SECONDS)
        
        # logger.info(f"Success: {text}")
    except Exception as e:
        print(e)
        # logger.debug(f"Error: {e}")
    finally:
        browser.quit()