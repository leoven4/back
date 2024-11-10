from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from constants_insta import constants
from time import sleep, localtime
import pickle
# import sys
# print(sys.path)


from constants import constants

class Instabot:
    def __init__(self, isRemote=False):
        # file_name = './output_' + str(time.localtime().tm_mday) + '.txt'
        # sys.stdout = open(file_name, 'w')
        print('-------------------------------------------TASK RUN @------------------------------------------------')
        print('Day:', localtime().tm_mday, '/', localtime().tm_mon, '\n')
        print('Time:', localtime().tm_hour, ':', localtime().tm_min, ':', localtime().tm_sec, '\n')
        # sys.stdout.close()
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--no-sandbox")

        if isRemote:
            chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument('--disable-dev-shm-usage')

        # driver = webdriver.Chrome(options=chrome_options, executable_path='./chromedrover.exe')
        
        self.isRemote = isRemote
        if isRemote:
            self.driver = webdriver.Chrome(options=chrome_options)
        else:
            self.driver = webdriver.Chrome(options=chrome_options, service=Service(ChromeDriverManager().install()))

        self.loaded = False
        self.logged = False
        self.liked = False

        self.xpath_collection = {
            'cookies_button': "/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/button[1]",
            'username' :      "/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[1]/div/label/input",
            'password' :      "/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[2]/div/label/input",
            'lens' :          "/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[2]/div/a/div",
            'search' :        "/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div[1]/div/input",
            'first_hashtag' :  "/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div[2]/div/div[1]/div/a/div",
            'first_result' : "/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/article/div[2]/div/div[1]/div[1]/a/div/div[2]",
            'like' :          "/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/section[1]/span[1]/button",
            'exit' :           "/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div",
            'second_result' : "/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/article/div[2]/div/div[1]/div[2]/a/div/div[2]",
            'third_result' :  "/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/article/div[2]/div/div[1]/div[3]/a/div[1]/div[2]",
            'verification_button' : "/html/body/div[1]/section/div/div/div[3]/form/span/button",
            'verification_code' : "/html/body/div[1]/section/div/div/div[2]/form/div/input"}
    
        self.time_step = 2

    @staticmethod
    def get_cookies(self):

        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument('--disable-dev-shm-usage')    

        driver = webdriver.Chrome(options=chrome_options, service=Service(ChromeDriverManager().install()))
        driver.get("https://www.instagram.com/")
        while True:
            sleep(10)
            try:
                state=driver.get_cookies()
            except:
                break
        pickle.dump(state,open("authDT_v2.pkl","wb"))
        print(state)

    def load_cookies(self):

        cookies = pickle.load(open("authDT.pkl", "rb"))
        for cookie in cookies:
            self.driver.add_cookie(cookie)

    def get_the_page(self):

        if not self.loaded:
            try:
                print('@@@@@@@@@@@@@@ Getting the page ')
                self.driver.get('https://www.instagram.com/')
                self.load_cookies()
                self.driver.get('https://www.instagram.com/')
                sleep(self.time_step)
                # cookies_button = self.driver.find_element(By.XPATH, self.xpath_collection['cookies_button']).click()

                self.loaded = True            
            except Exception as e:
                print('Page not loaded:')

                if self.isRemote:
                    self.driver.save_screenshot('fetching.png')
                print(e)
            finally:
                print('Done!')

    def add_credential(self):

        if not self.logged:
            try:
                print('-------------- logging in ')
                # Login
                your_username = constants['USER']
                your_password = constants['PASS']
                username = self.driver.find_element(By.XPATH, self.xpath_collection['username'])
                username.send_keys(your_username)
                psw = self.driver.find_element(By.XPATH, self.xpath_collection['password'])
                psw.send_keys(your_password)
                psw.send_keys(Keys.ENTER)
                # print('Day:', localtime().tm_mday, '/', localtime().tm_mon)
                # print('Time:', localtime().tm_hour, ':', localtime().tm_min, ':', localtime().tm_sec)
                sleep(3 * self.time_step)
                self.logged = True            
            except Exception as e:
                print('Not logged:')

                if self.isRemote:
                    self.driver.save_screenshot('logging.png')
                print(e)
            finally:
                print('Done!')

    def looking_for_hashtag(self, hashtag):

        try:
            print('////////////// Looking for hashtags ')
            # # save or not
            # try:
            #     self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div/button").click()
            # except Exception as e:
            #     print('Exception in save or not')
            #     print(e)
            # sleep(2)
            # notification
            # try:
            #     self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]").click()
            # except Exception as e:
            #     print('Exception in notification')
            #     print(e)
            # sleep(5)

            lens = self.driver.find_element(By.XPATH, self.xpath_collection['lens']).click()
            search = self.driver.find_element(By.XPATH, self.xpath_collection['search'])
            search.send_keys(hashtag)
            search.send_keys(Keys.ENTER)
            sleep(self.time_step)
            self.found = True
        except Exception as e:
            print('Not found:')
            if self.isRemote:
                self.driver.save_screenshot('looking.png')
            print(e)
        finally:
            print('Done!')

    def like_most_recents(self):

        try:
            # print('<3<3<3<3<3<3<3<3<3<3<3 ONE MORE LIKE')
            first_hashtag = self.driver.find_element(By.XPATH, self.xpath_collection['first_hashtag']).click()
            sleep(3 * self.time_step)
            first_result = self.driver.find_element(By.XPATH, self.xpath_collection['first_result']).click()
            sleep(2 * self.time_step)
            like = self.driver.find_element(By.XPATH, self.xpath_collection['like']).click()
            exit = self.driver.find_element(By.XPATH, self.xpath_collection['exit']).click()

            sleep(2 * self.time_step)
            second_result = self.driver.find_element(By.XPATH, self.xpath_collection['second_result']).click()
            sleep(2 * self.time_step)
            like = self.driver.find_element(By.XPATH, self.xpath_collection['like']).click()
            exit = self.driver.find_element(By.XPATH, self.xpath_collection['exit']).click()

            sleep(2 * self.time_step)
            third_result = self.driver.find_element(By.XPATH, self.xpath_collection['third_result']).click()
            sleep(2 * self.time_step)
            like = self.driver.find_element(By.XPATH, self.xpath_collection['like']).click()
            exit = self.driver.find_element(By.XPATH, self.xpath_collection['exit']).click()

            self.liked = True
        except Exception as e:
            print('Not liked:')
            if self.isRemote:
                self.driver.save_screenshot('liking.png')
            print(e)
        finally:
            # self.driver.quit()
            print('Done!')

    def login(self):

        while not self.loaded:
            self.get_the_page()
            sleep(5)
            # self.add_credential()
            # sleep(5)



    def add_like(self):
        while not self.liked:
            self.looking_for_hashtag('#cyclinglife')
            sleep(5)
            self.like_most_recents()

    def verification(self):
        button = self.driver.find_element(By.XPATH, self.xpath_collection['verification_button']).click()

        code = input('did you get a code?')
        verification_code = self.driver.find_element(By.XPATH, self.xpath_collection['verification_code'])
        verification_code.send_keys(code)
        verification_code.send_keys(Keys.ENTER)
        verification_code.send_keys(Keys.ENTER)










