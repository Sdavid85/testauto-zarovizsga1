import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
# options.add_argument("--headless")
options.add_argument("--disable-gpu")

driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)

try:
    driver.get("https://black-moss-0a0440e03.azurestaticapps.net/x234.html")

    time.sleep(2)

    a_values = [99, "kiskutya", ""]
    b_values = [12, 12, ""]
    results = ['222', "NaN", "NaN"]

    a_field = driver.find_element_by_id('a')
    b_field = driver.find_element_by_id('b')
    submit_btn = driver.find_element_by_id('submit')
    result = driver.find_element_by_id('result')

    # TC1 Helyes kitöltés esete:
    #     * a: 99
    #     * b: 12
    #     * Eredmény: 222

    a_field.send_keys(a_values[0])
    b_field.send_keys(b_values[0])
    submit_btn.click()
    time.sleep(2)

    assert result.text == results[0]

    # TC2 Nem számokkal történő kitöltés:
    #     * a: kiskutya
    #     * b: 12
    #     * Eredmény: NaN

    a_field.clear()
    b_field.clear()

    a_field.send_keys(a_values[1])
    b_field.send_keys(b_values[1])
    submit_btn.click()
    time.sleep(2)

    assert result.text == results[1]

    # TC3 Üres kitöltés:
    #     * a: <üres>
    #     * b: <üres>
    #     * Eredmény: NaN

    a_field.clear()
    b_field.clear()

    a_field.send_keys(a_values[2])
    b_field.send_keys(b_values[2])
    submit_btn.click()
    time.sleep(2)

    assert result.text == results[2]

finally:
    pass
# driver.close()
