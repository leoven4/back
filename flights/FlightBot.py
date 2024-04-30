import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement

x_path = {
    'accept':              '//*[@id="yDmH0d"]/c-wiz/div/div/div/div[2]/div[1]/div[4]/div[1]/div[1]/form[2]/div/div/button/span',
    'first_search_result': '/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div[1]/div[1]/div/div[2]/div[1]/div[6]/div[3]/ul/li',
    'add_departure':       '/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div[1]/div[1]/div/div[2]/div[1]/div[6]/div[2]/div[3]/span/button',
    
    'flight_from':         '/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div[1]/div[1]/div/div[2]/div[1]/div[1]/div/div/div[1]/div/div/input',
    'flight_from_2':       '/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div[1]/div[1]/div/div[2]/div[1]/div[6]/div[2]/div[2]/div[1]/div[2]/input',
    'flight_from_3':       '/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div[1]/div[1]/div/div[2]/div[1]/div[6]/div[2]/div[2]/div[1]/div[3]/input',

    'flight_to':           '/html/body/c-wiz[3]/div/div[2]/div/c-wiz/div[2]/div/div/div[1]/div[1]/section/div/div[1]/div[1]/div[1]/div[2]/div[1]/div/div[2]/div/div[1]/div/div/input',
    'everywhere':          '/html/body/c-wiz[3]/div/div[2]/div/c-wiz/div[2]/div/div/div[1]/div[1]/section/div/div[1]/div[1]/div[1]/div[2]/div[1]/div/div[2]/div/div[2]/div[3]/ul/li[1]',

    'n_stop':              '/html/body/c-wiz[3]/div/div[2]/div/c-wiz/div[2]/div/div/div[1]/div[1]/div/div/div/div/div[2]/div[1]/div/div[2]/span/button',
    '1_stop_max':          '/html/body/c-wiz[3]/div/div[2]/div/c-wiz/div[2]/div/div/div[1]/div[1]/div/div/div/div[2]/div[3]/div/div[1]/section/div[2]/div[1]/div/div/div[3]/div/input',
    
    }

class FlightBot:
     
    def __init__(self):
                      
        try:
            self.driver = webdriver.Chrome()

            self.driver.get('https://www.google.com/travel/flights')

            # accept cookies
            time.sleep(0.1)
            accept = self.driver.find_element(by=By.XPATH, value=x_path['accept'])
            accept.click()

            self.add_departure(['FCO', 'BLQ', 'MXP'])
            time.sleep(1)
            self.add_destination()
            self.one_stop_max()
            time.sleep(300)

        except Exception as e:
            print('Exception in check_webpage:')
            print(e)

        finally:
                self.driver.quit()
                print('Done!')

    def add_departure(self, airport):
            
            time.sleep(1)
            flight_from = self.find_and_clear(x_path['flight_from'])
            flight_from.send_keys(airport[0])
            
            time.sleep(1)
            self.find_and_click(x_path['first_search_result'])
            flight_from.click()

            time.sleep(0.5)
            self.find_and_click(x_path['add_departure'])

            time.sleep(0.5)
            self.find_and_send_key(x_path['flight_from_2'], airport[1])

            time.sleep(0.5)
            self.find_and_click(x_path['first_search_result'])
            
            time.sleep(0.5)
            self.find_and_send_key(x_path['flight_from_3'], airport[2])

            time.sleep(0.5)
            self.find_and_click(x_path['first_search_result'])
            self.find_and_send_key(x_path['flight_from'], Keys.ENTER)

    def add_destination(self):

        self.find_and_click(x_path['flight_to'])
        time.sleep(0.5)
        self.find_and_click(x_path['everywhere'])

    def one_stop_max(self):
        
        self.find_and_click(x_path['n_stop'])
        time.sleep(0.5)
        self.find_and_click(x_path['1_stop_max'])

    def find_and_clear(self, x_path) -> WebElement:
        elem = self.driver.find_element(by=By.XPATH, value=x_path)
        elem.clear()
        return elem
    
    def find_and_click(self, x_path) -> WebElement:
        elem = self.driver.find_element(by=By.XPATH, value=x_path)
        elem.click()
        return elem
    
    def find_and_send_key(self, x_path, key) -> WebElement:
        elem = self.driver.find_element(by=By.XPATH, value=x_path)
        elem.send_keys(key)
        return elem


if __name__ == '__main__':
    FlightBot()