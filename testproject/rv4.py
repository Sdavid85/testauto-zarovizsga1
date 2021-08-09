import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
# options.add_argument("--headless")
options.add_argument("--disable-gpu")

driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)

try:
    driver.get("https://black-moss-0a0440e03.azurestaticapps.net/rv4.html")
    time.sleep(2)

    cities = driver.find_element_by_id('cites').get_attribute("value")
    random_cities = driver.find_elements_by_xpath('//*[@id="randomCities"]/li')
    missing_city_field = driver.find_element_by_id('missingCity')
    result = driver.find_element_by_id('result')

    # Egy while ciklusba ágyazott for ciklussal kellene beküldeni a "cities" lista elemeit a
    # a "missing_city_field_" mezőbe, amíg el nem találja a hiányzó várost.

    # Assertezni pedig úgy lehetne, hogy a hiányzó várost hozzáadjuk "random_cities" listához, sorba állítjuk ABC szerint
    # ezt a kiegészített "random_cities" listát és a "cities" listát is, majd összehasonlítjuk a kettő tartalmát.

finally:
    pass
# driver.close()