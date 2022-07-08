from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
#from bs4 import BeautifulSoup
#import requests
import time



# Creating class for executing multiple tasks
class Umesh:
    url = "https://www.zenclass.in/login"

    driver = webdriver.Firefox()

# Login into Zen Portal using Selenium
    def Login(self):
         username = "umeshinfomech@gmail.com"
         password = "*******"
         self.driver.get(self.url)
         time.sleep(5)
         username_xpath = '//*[@id="root"]/div/div/div[1]/div[2]/div/div[1]/form/div[1]/div/input'
         password_xpath = '//*[@id="root"]/div/div/div[1]/div[2]/div/div[1]/form/div[2]/div/input'
         login_button_xpath = '//*[@id="root"]/div/div/div[1]/div[2]/div/div[1]/form/button'


         username1 = self.driver.find_element(by=By.XPATH, value=username_xpath)
         password1 = self.driver.find_element(by=By.XPATH, value=password_xpath)
         login1 = self.driver.find_element(by=By.XPATH, value=login_button_xpath)


# Send Username , Password & Click the login button
         username1.send_keys(username)
         password1.send_keys(password)
         login1.click()
         time.sleep(5)

# Scrap information from Left side pane
    #def Leftsidepane(self):
         #url2="https://www.zenclass.in/class"
         #data = requests.get(url2)
         #soup = BeautifulSoup(data.content, 'html.parser')

         #Menu_list=[]
         #menu_items=soup.findall('div',class_='list-scroll py-3 active-area active-left-bar')
         #Menu_list.append(menu_items.text)
         #print(Menu_list)

# Raising queries using method "Query"
    def Query(self):

         Queries_page_xpath = '//*[@id="root"]/div[1]/nav/ul/div[6]/li/span/div/div[2]'
         random_page_xpath = '//*[@id="root"]/nav'
         
         query_section=self.driver.find_element(by=By.XPATH, value=Queries_page_xpath)         
         random_click=self.driver.find_element(by=By.XPATH, value=random_page_xpath)

         query_section.click()
         random_click.click()
        
         Create_query_xpath = '//*[@id="root"]/div[2]/div/div[1]/div[1]'

         querybutton1 = self.driver.find_element(by=By.XPATH, value=Create_query_xpath)

         querybutton1.click()
         time.sleep(5)

         Warning_window_xpath='/html/body/div/div[2]/div/div[2]/div[6]/div[2]/div/div/section[3]/div[2]/button[1]'

         Warning_cancel=self.driver.find_element(by=By.XPATH, value=Warning_window_xpath)

         Warning_cancel.click()

         Query_title1="Guvi Python AT - 1 &2 Automation Project"
         Query_description="This is a Project Test Code Running for the Python Automation - 1&2 Project Given by mentor Mr. Suman Gangopadhyay."

         Category_dropdown_xpath='//*[@id="root"]/div[2]/div/div[2]/div/div/form/div[2]/div[1]/select'
         Option_select_xpath='//*[@id="root"]/div[2]/div/div[2]/div/div/form/div[2]/div[1]/select/option[3]'

         Query_title_xpath='//*[@id="root"]/div[2]/div/div[2]/div/div/form/div[5]/div[1]/input'
         Query_description_xpath='//*[@id="root"]/div[2]/div/div[2]/div/div/form/div[5]/textarea'
         Create_button_xpath='//*[@id="root"]/div[2]/div/div[2]/div/div/form/div[13]/div/button'


         Category_button =self.driver.find_element(by=By.XPATH, value=Category_dropdown_xpath)
         Option_Select=self.driver.find_element(by=By.XPATH, value=Option_select_xpath)

         Category_button.click()
         Option_Select.click()

         Language_button_xpath='//*[@id="root"]/div[2]/div/div[2]/div/div/form/div[2]/div[2]/select'
         Language_select_xpath='//*[@id="root"]/div[2]/div/div[2]/div/div/form/div[2]/div[2]/select/option[2]'

         Language_button=self.driver.find_element(by=By.XPATH, value=Language_button_xpath)
         Language_select_button=self.driver.find_element(by=By.XPATH, value=Language_select_xpath)
         Query_title=self.driver.find_element(by=By.XPATH, value=Query_title_xpath)
         Query_description_text=self.driver.find_element(by=By.XPATH, value=Query_description_xpath)
         Create_button=self.driver.find_element(by=By.XPATH, value=Create_button_xpath)


         Language_button.click()
         Language_select_button.click()
         Query_title.send_keys(Query_title1)
         Query_description_text.send_keys(Query_description)
         Create_button.click()
         time.sleep(5)

# Executing the objects under the class Umesh
s = Umesh()
s.Login()
s.All_Data()
s.Query()
s.Query()
s.Query()
s.Query()
s.Query()
#s.Leftsidepane()

