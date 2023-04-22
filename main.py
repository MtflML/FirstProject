#from random import randint
from time import sleep
from os import environ
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchWindowException


def launch(browser):
    chromeOptions = Options()
    chromeOptions.add_argument('--headless')
    chromeOptions.add_argument("--no-sandbox")
    chromeOptions.add_argument("--disabled-gpu")
    chromeOptions.add_argument("--single-process")
    chromeOptions.add_argument("--disable-dev-shm-usage")
    chromeOptions.add_argument("blink-settings=imagesEnabled=false")
    browser = Chrome(options=chromeOptions)
    browser.implicitly_wait(20)
    sleep(5)


def login(browser, user, passwd, terminalUrl):
    print("Loading Login Page...", flush=True)
    login_url = "https://accounts.goorm.io/login?return_url=aHR0cHM6Ly9pZGUuZ29vcm0uaW8vbXkvZGFzaGJvYXJkP3JlZGlyZWN0PTE%3D&keep_login=true"
    browser.get(login_url)
    WebDriverWait(browser, 30). until(
        EC.visibility_of_element_located(
            (By.XPATH, '//*[@id="app"]/section/div[4]/button')
            )
    )
    print(f"Now Login With {user}/{passwd}", flush=True)
    inputEmail = browser.find_element(By.NAME, "email")
    inputPasswd = browser.find_element(By.NAME, "password")
    inputEmail.clear()
    inputEmail.click()
    sleep(1)
    inputEmail.send_keys(user)
    sleep(1)
    inputPasswd.clear()
    inputPasswd.click()
    sleep(1)
    inputPasswd.send_keys(passwd)
    sleep(1)
    browser.save_screenshot("1.png")
    browser.find_element(By.XPATH, '//*[@id="app"]/section/div[4]/button').click()
    try:
        WebDriverWait(browser, 30). until(
            EC.url_matches("ide.goorm.io/my/dashboard")
        )
        sleep(5)
        browser.save_screenshot("2.png")
        browser.get(terminalUrl)
        browser.implicitly_wait(30)
        sleep(15)
    except TimeoutException:
        if browser.find_element(By.CLASS_NAME, "invalid-feedback").is_displayed():
            print("Login Failed!Please Check Your Email And Password!", flush=True)
            browser.quit()
            sleep(5)
            return 0
    print("Login Successed!", flush=True)
    browser.save_screenshot("3.png")

    return 1


def keepAlive(browser, user, passwd, terminalUrl):
    print("Start KeepAlive Workflow!Enjoy it!", flush=True)
    while 1:
        try:
            if(EC.url_matches("ide-run.goorm.io/terminal/")):
                print("Container is Online...", flush=True)
                sleep(15)
                browser.save_screenshot("4.png")
                sleep(6900)
                browser.save_screenshot("5.png")
                browser.refresh()
                browser.implicitly_wait(30)
            else:
                print("Unexpected logout! Relogin...", flush=True)
                browser.quit()
                sleep(5)
                launch(browser)
                login(browser, user, passwd, terminalUrl)
        except NoSuchWindowException:
            print("Browser was crushed! Restart...", flush=True)
            browser.quit()
            sleep(5)
            launch(browser)
            if(login(browser, user, passwd, terminalUrl)):
                keepAlive(browser, user, passwd, terminalUrl)
            else:
                print("Something wrong, check it out.", flush=True)
                browser.quit()
                return -1

    return 0


def main():
    user = environ["DASHBOARD_USERNAME"]
    passwd = environ["DASHBOARD_PASSWORD"]
    terminalUrl = environ["TERMINAL_URL"]
    chromeOptions = Options()
    chromeOptions.add_argument('--headless')
    chromeOptions.add_argument("--no-sandbox")
    chromeOptions.add_argument("--disabled-gpu")
    chromeOptions.add_argument("--single-process")
    chromeOptions.add_argument("--disable-dev-shm-usage")
    chromeOptions.add_argument("blink-settings=imagesEnabled=false")
    browser = Chrome(options=chromeOptions)
    browser.implicitly_wait(20)
    if(login(browser, user, passwd, terminalUrl)):
        keepAlive(browser, user, passwd, terminalUrl)
    else:
        print("Login error! Check and try again.")
    browser.quit()

    return 0


if __name__ == "__main__":
    main()
