from selenium import webdriver	 

# For using sleep function because selenium 
# works only when the all the elemets of the 
# page is loaded. 
import time 

from selenium.webdriver.common.keys import Keys 

# Creating an instance webdriver 
browser = webdriver.Chrome(executable_path='E:/Python_Course/whastapp_access/chromedriver/chromedriver.exe')
browser.get('https://www.twitter.com') 

# Let's the user see and also load the element 
#time.sleep(2) 



print("Loggin in Twitter") 

user = browser.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/section/form/div/div[1]/div/label/div/div[2]/div/input') 

# Enter User Name 
user.send_keys('************') 

#user = browser.find_element_by_name('//*[@id="login-dialog-dialog"]/div[2]/div[2]/div[2]/form/div[2]/input') 

# Reads password from a text file because 
# saving the password in a script is just silly. 
user = browser.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/section/form/div/div[2]/div/label/div/div[2]/div/input')
Password = '****************'
user.send_keys(Password)

button = browser.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/section/form/div/div[3]/div/div')
button.click() 


