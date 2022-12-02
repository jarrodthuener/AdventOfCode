import datetime
import os

import dateutil.parser
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import requests
from datetime import datetime
import pytz


"""define variables needed"""
# these will be pulled in dynamically
todayFlag = True
if todayFlag:
    current = datetime.now(pytz.timezone('US/Eastern'))
    day = current.strftime('%d').lstrip('0')
    year = current.strftime('%Y')
else:
    day = '2'
    year = '2021'


# if savepath is empty:
#     print(error)
# else
#     savePath = "..\data"

savePath = "..\data"
dataFileName = "day"+str(day)+".txt"
dataFilePath = os.path.join(savePath,dataFileName)
sessionId = ""
sampleDataURL = 'https://adventofcode.com/'+year+'/day/'+day
fullDataURL = 'https://adventofcode.com/'+year+'/day/'+day+"/input"




def pullSampleData():
    options = Options()
    options.headless = True
    browser = webdriver.Chrome(options=options)
    browser.get(sampleDataURL)
    browser.add_cookie({"name":"session", "value":sessionId})
    elements = browser.find_elements(By.TAG_NAME, "code")
    return elements[0].text

def pullFullData():
    headers = {"cookie":"session="+sessionId}
    fullData = requests.get(fullDataURL,headers=headers)
    print(fullData.text)
    return fullData.text


# """check to see if today's data exists"""
if os.path.exists(dataFilePath):
    fullDailyData = open(dataFilePath,"r").read()
else:
    try:
        finalSampleData = pullSampleData()
        try:
            finalFullData = pullFullData()
            fullDailyData = finalSampleData + "\nSplit From Here\n" + finalFullData
            print(fullDailyData)
            try:
                f = open(dataFilePath, "w")
                f.write(finalSampleData + "\nSplit From Here\n" + finalFullData)
                f.close()
                fullDailyData = finalSampleData + "\nSplit From Here\n" + finalFullData
            except:
                print("Error Writing files")
        except:
            print("Error pulling Full Data")
    except:
        print("Error pulling Sample Data")



print(type(fullDailyData))
print(fullDailyData)