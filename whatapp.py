from selenium import webdriver	 

# For using sleep function because selenium 
# works only when the all the elemets of the 
# page is loaded. 
import time 

from selenium.webdriver.common.keys import Keys 

# Creating an instance webdriver 
browser = webdriver.Chrome(executable_path='E:/Python_Course/whastapp_access/chromedriver/chromedriver.exe')
browser.get('https://web.whatsapp.com/') 

# Let's the user see and also load the element 
#time.sleep(30) 
t = time.localtime()
current_time = time.strftime("%H:%M:%S", t)
print(type(current_time))



print("Loggin in Whatsapp") 


user = browser.find_element_by_xpath('//*[@id="side"]/div[1]/div/label/div/div[2]') 
user.send_keys('harikrishna Whatsapp'+Keys.ENTER)
i=1

while i<1000:

	emoji=browser.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[1]/div/button[2]/span')
	emoji.click()

	input2=browser.find_element_by_xpath('//*[@id="main"]/footer/div[2]/div/div[3]/div[1]/div[1]/div[2]/div/span/div/label/div/input')
	input2.send_keys('smile')
	input2.send_keys(Keys.ENTER)
	i=i+1
	text_area=browser.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
	text_area.send_keys(Keys.ENTER)
	time.sleep(1)
	
	





#laugh=browser.find_element_by_xpath('//*[@id="main"]/footer/div[2]/div/div[3]/div[1]/div[1]/div[2]/div/div/div/div[1]/div/div[6]/div/div/div/span[8]')
#i=0
#while i==100:
#	laugh.click()
#	i=i+1

#send=browser.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
#send.click()

# Enter User Name 
#user.send_keys('************') 

#user = browser.find_element_by_name('//*[@id="login-dialog-dialog"]/div[2]/div[2]/div[2]/form/div[2]/input') 

# Reads password from a text file because 
# saving the password in a script is just silly. 

#user = browser.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/section/form/div/div[2]/div/label/div/div[2]/div/input')
#Password = '****************'
#user.send_keys(Password)
#user.send_keys(Keys.ENTER)

#button = browser.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/section/form/div/div[3]/div/div')
#button.click() 


