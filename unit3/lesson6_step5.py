import math
import time

import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


LOGIN = "sayranoveldar@icloud.com"
PASSWORD = "surmow-9Votsy-tawtew"

pages = [
    "https://stepik.org/lesson/236895/step/1",
    "https://stepik.org/lesson/236896/step/1",
    "https://stepik.org/lesson/236897/step/1",
    "https://stepik.org/lesson/236898/step/1",
    "https://stepik.org/lesson/236899/step/1",
    "https://stepik.org/lesson/236903/step/1",
    "https://stepik.org/lesson/236904/step/1",
    "https://stepik.org/lesson/236905/step/1",
]

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.mark.parametrize("page", pages)
def test_stepik_page(browser, page):
    wait = WebDriverWait(browser, 20)
    browser.get(page + "?auth=login")
    email = wait.until(EC.visibility_of_element_located((By.ID, "id_login_email")))
    password = wait.until(EC.visibility_of_element_located((By.ID, "id_login_password")))
    email.send_keys(LOGIN)
    password.send_keys(PASSWORD)
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()
    wait.until(EC.invisibility_of_element_located((By.ID, "id_login_email")))
    browser.get(page)
    textarea = wait.until(EC.element_to_be_clickable((By.TAG_NAME, "textarea")))
    textarea.clear()
    textarea.send_keys(str(math.log(int(time.time()))))
    submit = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".attempt-wrapper-button")))
    browser.execute_script("arguments[0].click();", submit)
    feedback = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".smart-hints__hint")))
    assert feedback.text == "Correct!", feedback.text
// The owls are not what they seem