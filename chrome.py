from selenium import webdriver
from time import sleep
import time


usr = input('Enter Email Id:')
pwd = input('Enter Password:')
contr = input('Enter count:')
kwrds = input('Enter keywords:')



driver = webdriver.Chrome()
driver.get('https://www.facebook.com/')
print("Opened facebook")
sleep(1)

username_box = driver.find_element_by_id('email')
username_box.send_keys(usr)
print("Email Id entered")
sleep(1)

password_box = driver.find_element_by_id('pass')
password_box.send_keys(pwd)
print("Password entered")

login_box = driver.find_element_by_id('loginbutton')
login_box.click()


search = driver.find_element_by_css_selector("input[aria-label='Поиск']")
# search.send_keys("Elections")
search.send_keys(kwrds)
button = driver.find_element_by_css_selector("button[aria-label='Поиск']")
driver.execute_script("arguments[0].click();", button)
print("Search input")
# Scroll down depth-times and wait delay seconds to load
# between scrolls
for scroll in range(6):

    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    time.sleep(2)



print("Scroll")

# count = 4
selected_posts = []
posts_list = driver.find_elements_by_xpath("//div[@class='_401d']")
cnt = 0
# print("Contr:", int(contr))
count = int(contr)
for post in posts_list:
    if cnt < count:
        # print(post.text)
        selected_posts.append(post.text)
        cnt = cnt + 1
print(cnt)
print("posts:",selected_posts)
print("Done")
input('Press anything to quit')
driver.quit()
print("Finished")
