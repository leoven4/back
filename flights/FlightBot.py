import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
x_path = {
    'accept':              '//*[@id="yDmH0d"]/c-wiz/div/div/div/div[2]/div[1]/div[4]/div[1]/div[1]/form[2]/div/div/button/span',
    'first_search_result': '/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div[1]/div[1]/div/div[2]/div[1]/div[6]/div[3]/ul/li',
    'add_departure':       '/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div[1]/div[1]/div/div[2]/div[1]/div[6]/div[2]/div[3]/span/button',
    
    'flight_from':         '/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div[1]/div[1]/div/div[2]/div[1]/div[1]/div/div/div[1]/div/div/input',
    'flight_from_2':       '/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div[1]/div[1]/div/div[2]/div[1]/div[6]/div[2]/div[2]/div[1]/div[2]/input',
    'flight_from_3':       '/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div[1]/div[1]/div/div[2]/div[1]/div[6]/div[2]/div[2]/div[1]/div[3]/input',

    'flight_to':           '/html/body/c-wiz[3]/div/div[2]/div/c-wiz/div[2]/div/div/div[1]/div[1]/section/div/div[1]/div[1]/div[1]/div[2]/div[1]/div/div[2]/div/div[1]/div/div/input',
    'everywhere':          '/html/body/c-wiz[3]/div/div[2]/div/c-wiz/div[2]/div/div/div[1]/div[1]/section/div/div[1]/div[1]/div[1]/div[2]/div[1]/div/div[2]/div/div[2]/div[3]/ul/li[1]'
}

class FlightBot:
     
    def __init__(self):
                      
        try:
            driver.get('https://www.google.com/travel/flights')

            # accept cookies
            time.sleep(0.1)
            accept = driver.find_element(by=By.XPATH, value=x_path['accept'])
            accept.click()

            self.add_departure(['FCO', 'BLQ', 'MXP'])
            time.sleep(1)
            self.add_destination()
            time.sleep(100)

        except Exception as e:
            print('Exception in check_webpage:')
            print(e)

        finally:
                driver.quit()
                print('Done!')

    def add_departure(self, airport):
            
            time.sleep(1)
            flight_from_1 = driver.find_element(by=By.XPATH, value=x_path['flight_from'])
            flight_from_1.clear()
            flight_from_1.send_keys(airport[0])
            
            time.sleep(1)
            driver.find_element(by=By.XPATH, value=x_path['first_search_result']).click()
            flight_from_1.click()

            time.sleep(1)
            add_departure = driver.find_element(by=By.XPATH, value=x_path['add_departure']).click()
            flight_from_2 = driver.find_element(by=By.XPATH, value=x_path['flight_from_2'])

            time.sleep(1)
            flight_from_2.send_keys(airport[1])
            time.sleep(1)
            driver.find_element(by=By.XPATH, value=x_path['first_search_result']).click()
            
            time.sleep(1)
            flight_from_3 = driver.find_element(by=By.XPATH, value=x_path['flight_from_3'])
            time.sleep(1)

            flight_from_3.send_keys(airport[2])
            time.sleep(1)
            driver.find_element(by=By.XPATH, value=x_path['first_search_result']).click()
            driver.find_element(by=By.XPATH, value=x_path['flight_from']).send_keys(Keys.ENTER)

    def add_destination(self):

        time.sleep(1)
        flight_to = driver.find_element(by=By.XPATH, value=x_path['flight_to'])
        flight_to.click()
        time.sleep(1)
        driver.find_element(by=By.XPATH, value=x_path['everywhere']).click()


if __name__ == '__main__':
    FlightBot()