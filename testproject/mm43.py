import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
# options.add_argument("--headless")
options.add_argument("--disable-gpu")

driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)

try:
    driver.get("https://black-moss-0a0440e03.azurestaticapps.net/mm43.html")
    time.sleep(2)

    email = driver.find_element_by_id('email')
    submit_btn = driver.find_element_by_id('submit')
    mail_addresses = ["teszt@elek.hu", "teszt@", ""]

    # TC1 Helyes kitöltés esete:
    # email: teszt@elek.hu
    # Nincs validációs hibazüzenet

    email.send_keys(mail_addresses[0])
    submit_btn.click()

    assert not driver.find_elements_by_class_name('validation-error').is_displayed()

    # TC2 Helytelen:
    # email: teszt@
    # Please enter a part following '@'. 'teszt@' is incomplete.

    email.clear()
    email.send_keys(mail_addresses[1])
    submit_btn.click()

    assert driver.find_element_by_class_name('validation-error').get_attribute("value") == "Kérjük, adja meg a „@” utáni részt is. A(z) „teszt@” cím nem teljes."

    # TC3 Üres:
    # email: <üres>
    # b: <üres>
    # Please fill out this field.

    email.clear()
    email.send_keys(mail_addresses[2])
    submit_btn.click()

    assert driver.find_element_by_class_name('validation-error').get_attribute("value") == "Kérjük, töltse ki ezt a mezőt."

finally:
    pass
# driver.close()
