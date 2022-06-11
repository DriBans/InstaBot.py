# Selenium library is used to control the web browser and automate sending the message
# to use a browser, we import webdriver from selenium library.

from email import message
from unittest import result
from selenium import webdriver
import time
import random
import requests
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager

def jokes():
    #open the website to scrape the jokes from
    result = requests.get('https://jokojokes.com/nonsense-jokes.html')
    #HTML parser using beautiful soup
    soup = BeautifulSoup(result.content, 'html.parser')
    print(result.status_code)
    #Choose a random joke
    joke_no = random.randint(1, 22)
    joke = soup.ol.find_all("li")
    print(len(joke))
    return joke.text

def login_to_insta():
    username = browser.find_element_by_name("username")
    username.send_keys("Enter your username: ")
    password = browser.find_element_by_name("password")
    password.send_keys("Then enter your password: ")
    browser.find_element_by_xpath("//button[@type='submit']").click()

def skip_buttons():
    #not now for not saving the password
    browser.find_element_by_xpath("//div[@class='cmbtv']/button[@type='button']").click()
    #turn off the notification button
    browser.find_element_by_xpath("//dic[@class='mt3GC']/button[@class='aOOlW HoLwm ']").click()

def navigate_to_sender():
    #find the messages button
    browser.find_element_by_css_selector('html.js.logged-in.client-root.js-focus-visible.sDN5V body div#react-root section._9eogI.E3X2T nav.NXc7H.jLuN9 div._8MQSO.Cx7Bp div._lz6s div.MWDvN div.ctQZg div._47KiJ div.XrOey a.xWeGp svg._8-yf5').click()
    #Find the chat of the intended person
    elements = browser.find_elements_by_xpath('/html/body/div[1]/section/div/div[2]/div/div/div[1]/div[2]/div/div/div/div/div')
    length = len(elements)
    for i in range(length):
        find_user = browser.find_element_by_xpath('/html/body/div[1]/section/div/div[2]/div/div/div[1]/div[2]/div/div/div/div/div[{}]/a/div/div[2]/div[1]/div/div/div/div'.format(str(i+1)))
        if find_user.text == username:
            find_user.click()

def send_jokes(time_between_jokes):
    message_entry = browser.find_element_by_css_selector('html.js.logged-in.client-root.js-focus-visible.sDN5V body div#react-root section._9eogI.DT7qQ div.t30g8.L1C6I div.Igw0E.IwRSH.eGOV_._4EzTm div.oYYFH div.pV7Qt._6Rvw2.Igw0E.IwRSH.YBx95.ybXk5._4EzTm.i0EQd div.DPiy6.Igw0E.IwRSH.eGOV_.vwCYk div.uueGX div.JiVIq._0NM_B div.Igw0E.IwRSH.eGOV_._4EzTm div.Igw0E.IwRSH.eGOV_._4EzTm.L-sTb.HcJZg div.X3a-9 div.Igw0E.IwRSH.eGOV_.vwCYk.ItkAi textarea')
    while True:
        joke = jokes()
        message_entry.send_keys('Howdy Partner! ' + joke + ' Joke was sent on {time}'.format(time = time.ctime()))
        browser.find_element_by_xpath("/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button").click()
        time.sleep(time_between_jokes)

#Read user input to set a delay between jokes and obtain the username
time_between_jokes = int(input("Enter the seconds of delay between each joke: "))
username = input("Enter username: ")
#Open the webbrowser and use it for autonomous control
browser = webdriver.Chrome(ChromeDriverManager().install()3)
#Open the URL in the opened webbrowser
browser.get('https://instagram.com/')
#Start using the functions after a delay
browser.implicitly_wait(5)
#Call all the functions in order based on webpages
login_to_insta()
skip_buttons()
navigate_to_sender()
send_jokes(time_between_jokes)
