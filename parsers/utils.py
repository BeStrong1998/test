import time
from selenium import webdriver

def get_html(url):
    """
    -Функция работает с пакетом selenium(помогает обойти блакировки get-запросов на авито и циан).
    -Для работы нужно скачать ChromeDriver(https://sites.google.com/chromium.org/driver/).
    -Помесить ChromeDriver в паку с вертульным окружением проекта (env/bin).
    """
    # start web browser
    browser=webdriver.Chrome()

    # get source code
    browser.get(url)
    html = browser.page_source
    time.sleep(2)

    # close web browser
    browser.close()
    return html