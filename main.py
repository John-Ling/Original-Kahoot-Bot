# import necessary libraries
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time
import random

''' Kahoot Bot '''
''' a simple program  that will put a number of bots into Kahoot lobbies'''
'''during games bots will function indenpendently and randomly pick options'''

global tab, botNum, botCount

# variables
botChoice = 0
botOptions = ["/html/body/div/div/main/div[2]/div/button[1]", "/html/body/div/div/main/div[2]/div/button[2]", "/html/body/div/div/main/div[2]/div/button[3]", "/html/body/div/div/main/div[2]/div/button[4]"]
user = False
bool1 = False
bool2 = False
bool3 = False
tab = 0
choice = 0
botCount = 0

def openWindow():
    #open window and go to kahoot
    global tab
    
    print("Opening window...")
    driver.execute_script("window.open('');")
    driver.switch_to_window(driver.window_handles[tab])
    print("Navigating to Kahoot...")
    driver.get("https://kahoot.it/")
    tab += 1

def enterCredentials():
    #enter given credentials from input values
    global botNum, botCount

    openWindow()

    # input PIN
    input1 = driver.find_element_by_id("game-input")
    print("Entering game pin...")

    input1.send_keys(PIN)
    input1.send_keys(Keys.ENTER)
    
    time.sleep(5) # max bots before crash against time sleep is in ratio 10 : 5
    input2 = driver.find_element_by_id("nickname")
    print("Entering name...")

    # give bot personal number
    botNum = random.randint(1,999)
    botName = name + str(botNum) 

    input2.send_keys(botName)
    input2.send_keys(Keys.ENTER)

    print("Success!")
    botCount += 1

def botAns():
    #choose a random option during questions
    global botChoice
    num = random.randint(0,3)

    if url != "https://kahoot.it/v2/ranking":
        botChoice = botOptions[num]

        try:
            print("Picking valid answer...")
            shape = driver.find_element_by_xpath(botChoice)
            shape.send_keys(Keys.ENTER)

        # if question is true or false/less than 4 options
        except NoSuchElementException as exception:
            print("Repicking...")
            botAns()

# input values
print("")
print("Kahoot Bot")
print("")  
while user == False:
    PIN = (int(input("Enter game PIN: ")))
    name = input("Enter bot name: ")
    if len(name) > 12:
        print("Name is too long")
    name = str(name)
    num  = (int(input("Enter amount: ")))
    user = True

print("Opening Chrome...")
driver = webdriver.Chrome()

# join bots
try:
    for i in range(num): 
        enterCredentials()

except Exception:
    #stop any bots from joining if error occurs
    print("Login Failed")
    print("Aborting...")
    driver.close()


# close blank window
time.sleep(2)
driver.switch_to_window(driver.window_handles[tab])
driver.close()
driver.switch_to_window(driver.window_handles[0])
tab = 0

# lobby
print(botCount, " bots in game")
print('')
print("Waiting for game to start...")
while bool1 == False:
    url = "https://kahoot.it/v2/gameblock"
    if url == driver.current_url:
        bool1 = True
        print('')
        print("Answering questions...")
        url = ''

# answer questions
if bool1 == True:
    time.sleep(1)
    while bool2 == False:
        while tab != num:
            print("Switching tabs...")
            driver.switch_to_window(driver.window_handles[tab])
            botAns()
            tab += 1
        if driver.current_url == "https://kahoot.it/v2/getready":
            tab = 0
            time.sleep(6)
        # check if game has finished
        if driver.current_url == "https://kahoot.it/v2/ranking":
            bool2 = True
            print("Process Finished ")
            quit()