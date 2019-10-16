import random
from datetime import date

database = {}

class link():
    def __init__(self, fullUrl, shortUrl):
        self.fullUrl = fullUrl
        self.shortUrl = shortUrl
        self.dateCreated = date.today()

## We'll take in a URL, generate a bitly link for it, then store that in a dictionary
def createNewUrl(fullUrl, shortUrl):
    if(shortUrl == None):
        shortUrl = generateLink()
    else:
        ## do check to make sure that shortUrl only has supported characters
        shortUrl = shortUrl ## i.e do nothing for now
    newUrl = 'bit.ly/' + shortUrl
    newLink = link(fullUrl, newUrl)

    ## For now we'll just overwrite existing items if it's already there
    database[fullUrl] = newLink

## Method to binary search for existing URL
def searchDatabase(key):
    return database[key]

## Method to generate a link
def generateLink():
    DICTIONARY = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789" ## 72 chars
    resultStr = ""

    for i in range(7):
        resultStr = resultStr + DICTIONARY[random.randint(0, len(DICTIONARY)-1)]

    return resultStr

createNewUrl("www.test.com", None)
print(searchDatabase("www.test.com").shortUrl)

createNewUrl("www.test2.com", "test")
print(searchDatabase("www.test2.com").shortUrl)