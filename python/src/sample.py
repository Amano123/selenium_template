from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import os

def open_website(driver: webdriver.Remote, wait: WebDriverWait):
    driver.get('https://qiita.com')


def main() -> None:
    # Selenium サーバーへ接続する。
    driver = webdriver.Remote(
        command_executor=os.environ["SELENIUM_URL"],
        desired_capabilities=DesiredCapabilities.CHROME.copy()
    )
    # ドライバとタイムアウト値を指定
    wait = WebDriverWait(driver, 10)
    open_website(driver, wait)


if __name__ == '__main__':
    main()