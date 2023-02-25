import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from constants import constants

def check_webpage():

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")

    driver = webdriver.Chrome(options=chrome_options)
    try:
        driver.get('https://www.google.com/')
        print('got')
        # area_riservata = driver.find_element(by=By.XPATH, value='//*[@id="navbar"]/ul/li[6]/a')
        # area_riservata.click()
        # driver.implicitly_wait(0.5)

        # username = driver.find_element(by=By.XPATH, value='//*[@id="idusername"]')
        # username.send_keys(constants['USER'])

        # psw = driver.find_element(by=By.XPATH, value='//*[@id="idpassword"]')
        # psw.send_keys(constants['PASS'])
        # psw.send_keys(Keys.ENTER)
        # driver.implicitly_wait(1)

        # banca_sondrio = driver.find_element(by=By.XPATH, value='//*[@id="mainContent"]/div/div/div/div/div/div[28]/a/div')
        # banca_sondrio.click()

        # crediti = driver.find_element(by=By.XPATH, value='//*[@id="mainContent"]/div/div/div/div/div/div[4]/table/tbody/tr/td[1]/a')
        # crediti.click()

        # body = driver.find_element(by=By.XPATH, value='//*[@id="mainContent_inner"]/div')

        # text = body.text
        # result = text.find('il servizio è temporaneamente sospeso')
        # driver.close()

        # if result == -1:
        #     print('result == -1')
            # notify_via_email('leonardo.ventura@live.com', 'Cessazione crediti!!')
            # notify_via_email('geom.ventura@tiscali.it', 'Cessazione crediti!!')
    except:
        print('except check_webpage')
    finally:
        driver.quit()
        print('finally')

counter = 0

def check():
    print('-------------------------------------------TASK RUN @------------------------------------------------')
    print('Day:', time.localtime().tm_mday, '/', time.localtime().tm_mon, '\n')
    print('Time:', time.localtime().tm_hour, ':', time.localtime().tm_min, ':', time.localtime().tm_sec, '\n')
    check_webpage()


while counter<2:
    try:
        check()
        time.sleep(180)
        counter = counter + 1
    except Exception as e:
        print(e)
        print('except main')
        # notify_via_email('leonardo.ventura@live.com', 'Error in pycode')

# sys.stdout.close()


