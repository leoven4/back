from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
# import sys
# print(sys.path)

# Data
your_username = "anticoreste" 
your_password = "Inore20am"
time_step = 5

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--no-sandbox")
# chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument('--disable-dev-shm-usage')

# chrome_options.add_argument('--ignore-certificate-errors')
# chrome_options.add_argument('--allow-running-insecure-content')
# chrome_options.add_argument('--window-size=1200,1024')
# chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
# chrome_options.add_experimental_option('useAutomationExtension', False)

# driver = webdriver.Chrome(options=chrome_options, executable_path='./chromedrover.exe')
driver = webdriver.Chrome(options=chrome_options, service=Service(ChromeDriverManager().install()))

xpath_collection = {
    'cookies_button': "/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/button[1]",
    'username' :      "/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[1]/div/label/input",
    'password' :      "/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[2]/div/label/input", 
    'lens' :          "/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[2]/div/a/div",
    'search' :        "/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div[1]/div/input",
    'first_result' :  "/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div[2]/div/div[1]/div/a/div",
    'first_hashtag' : "/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/article/div[2]/div/div[1]/div[1]/a/div/div[2]",
    'like' :          "/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/section[1]/span[1]/button"
}

try:
    while True:

        print('@@@@@@@@@@@@@@ Getting the page ')
        driver.get('https://www.instagram.com/')
        cookies_button = driver.find_element(By.XPATH, xpath_collection['cookies_button']).click()
        time.sleep(time_step)

        # Login
        print('-------------- logging in ')
        username = driver.find_element(By.XPATH, xpath_collection['username'])
        username.send_keys(your_username)
        psw = driver.find_element(By.XPATH, xpath_collection['password'])
        psw.send_keys(your_password)
        psw.send_keys(Keys.ENTER)
        print('Day:', time.localtime().tm_mday, '/', time.localtime().tm_mon)
        print('Time:', time.localtime().tm_hour, ':', time.localtime().tm_min, ':', time.localtime().tm_sec)
        time.sleep(time_step)
       
        # save or not
        # try:
        #     driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div/button").click()
        # except Exception as e:
        #     print('Exception in save or not')
        #     print(e)
        # time.sleep(2)
        # notification
        # try:
        #     driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]").click()
        # except Exception as e:
        #     print('Exception in save or not')
        #     print(e)
        # time.sleep(5)

        print('////////////// Looking for hashtags ')
        lens = driver.find_element(By.XPATH, xpath_collection['lens']).click()
        search = driver.find_element(By.XPATH, xpath_collection['search'])
        search.send_keys('#bike')
        search.send_keys(Keys.ENTER)
        time.sleep(time_step)

        print('<3<3<3<3<3<3<3<3<3<3<3 ONE MORE LIKE')
        first_result = driver.find_element(By.XPATH, xpath_collection['first_result']).click()
        time.sleep(time_step)
        first_hashtag = driver.find_element(By.XPATH, xpath_collection['first_hashtag']).click()
        time.sleep(time_step)
        like =driver.find_element(By.XPATH, xpath_collection['like']).click()


        time.sleep(100)


except Exception as e:
    print('Exception in main_selenium:')
    print(e)

finally:
    driver.quit()
    print('Done!')


