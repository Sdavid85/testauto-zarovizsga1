import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
# options.add_argument("--headless")
options.add_argument("--disable-gpu")

driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)

try:
    driver.get("https://black-moss-0a0440e03.azurestaticapps.net/tts4.html")
    time.sleep(2)

    submit_btn = driver.find_element_by_id('submit')
    results = driver.find_element_by_id('lastResult')
    fej_list = []

    for _ in range(101):
        submit_btn.click()
        if results.text == "fej":
            fej_list.append(results.text)

    print(len(fej_list))

    assert len(fej_list) >= 30

finally:
    pass
# driver.close()