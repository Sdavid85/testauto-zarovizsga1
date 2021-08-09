import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
# options.add_argument("--headless")
options.add_argument("--disable-gpu")

driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)

try:
    driver.get("https://black-moss-0a0440e03.azurestaticapps.net/ioa8.html")
    time.sleep(2)

    number1 = driver.find_element_by_id('num1').get_attribute("value")
    number2 = driver.find_element_by_id('num2').get_attribute("value")
    op = driver.find_element_by_id('op')
    submit = driver.find_element_by_id('submit')
    result = driver.find_element_by_id('result')
    number = int()

    submit.click()

    # A műveleti jeltől függően elvégzem a műveletet a két számmal

    if op.get_attribute("value") == "+":
        number = int(number1) + int(number2)
    elif op.get_attribute("value") == "-":
        number = int(number1) - int(number2)
    elif op.get_attribute("value") == "*":
        number = int(number1) * int(number2)

    # A pythonban számolt eredményt összehasonlítom a weboldalon kalkulált eredménnyel.

    assert number == result.get_attribute("value")

finally:
    pass
# driver.close()
