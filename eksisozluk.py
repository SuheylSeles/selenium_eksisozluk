from selenium import webdriver
import random
import time

browser = webdriver.Firefox()

url = "https://eksisozluk.com/besiktas--37894?p="

pageCount = 1

entries = []

entryCount = 1

while pageCount <= 10:

    randomPage = random.randint(1,4627)

    newUrl = url + str(randomPage)

    browser.get(newUrl)

    elements = browser.find_elements_by_css_selector(".content")

    for element in elements:

        entries.append(element.text)

    time.sleep(5)

    pageCount += 1

with open("entries.txt","w",encoding="UTF-8") as file:

    for entry in entries:

        file.write(str(entryCount)+".\n"+entry+"\n")
        file.write("***********************************************************\n")
        entryCount += 1

for entry in entries:

    print(str(entryCount)+"*******************************************************")
    print(element.text)
    entryCount += 1

browser.close()


"""
browser.get(url)

time.sleep(5)
"""
"""
elements = browser.find_elements_by_css_selector(".content")

for element in elements:

    print("***********************************************")
    print(element.text)
"""

