import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()

def beginDriver():
    driver.get("https://humanbenchmark.com/tests/verbal-memory")

def getWord():
    word = driver.find_element(By.CLASS_NAME, "word").get_attribute("textContent")
    return word

def getSeenWordButton():
    seenButton = driver.find_element(By.CLASS_NAME, "css-1bnidmp")
    return seenButton

def getNewWordButton():
    newButton = driver.find_element(By.CLASS_NAME, "css-1bnidmp")
    return newButton

def clickStart():
    startButton = driver.find_element(By.CLASS_NAME, "css-1bnidmp")
    startButton.send_keys(Keys.ENTER)

def clickSeen(seenButton):
    seenButton.send_keys(Keys.ENTER)

def clickNew(newButton):
    newButton.send_keys(Keys.ENTER)