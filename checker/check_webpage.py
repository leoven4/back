from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from notifier.notifier import notify, notify_via_email
from constants import constants
import time


def check_webpage():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument('--disable-dev-shm-usage')

    # chrome_options.add_argument("--headless=chrome")
    # chrome_options.add_argument('--ignore-certificate-errors')
    # chrome_options.add_argument('--allow-running-insecure-content')
    # chrome_options.add_argument('--window-size=1200,1024')
    # chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    # chrome_options.add_experimental_option('useAutomationExtension', False)

    driver = webdriver.Chrome(chrome_options=chrome_options)


    try:
        driver.get('    ')
        time.sleep(2)
        # driver.implicitly_wait(1)
        # area_riservata = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.XPATH, '//*[@id="navbar"]/ul/li[6]/a')))
        # area_riservata = WebDriverWait(driver, 1).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="navbar"]/ul/li[6]/a')))

        area_riservata = driver.find_element(by=By.XPATH, value='//*[@id="navbar"]/ul/li[6]/a')
        # driver.get_screenshot_as_file("screenshot.png")
        driver.execute_script("arguments[0].click();", area_riservata)
        # area_riservata.click()

        time.sleep(1)
        username = driver.find_element(by=By.XPATH, value='//*[@id="idusername"]')
        username.send_keys(constants['USER'])

        time.sleep(1)
        psw = driver.find_element(by=By.XPATH, value='//*[@id="idpassword"]')
        psw.send_keys(constants['PASS'])
        psw.send_keys(Keys.ENTER)

        time.sleep(1)
        banca_sondrio = driver.find_element(by=By.XPATH, value='//*[@id="mainContent"]/div/div/div/div/div/div[28]/a/div')
        banca_sondrio.click()

        time.sleep(1)
        crediti = driver.find_element(by=By.XPATH, value='//*[@id="mainContent"]/div/div/div/div/div/div[4]/table/tbody/tr/td[1]/a')
        crediti.click()

        time.sleep(1)
        body = driver.find_element(by=By.XPATH, value='//*[@id="mainContent_inner"]/div')
        text = body.text

        print(text)
        result = text.find('il servizio è temporaneamente sospeso')
        driver.close()

        if result == -1:
            notify_via_email('', 'Cessazione crediti!!')
            notify_via_email('', 'Cessazione crediti!!')
            notify()

    except Exception as e:
        print('Exception in check_webpage:')
        print(e)

    finally:
            driver.quit()
            print('Done!')


