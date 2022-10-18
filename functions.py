from time import sleep
from helium import *
import json

def login(username, password, dpNumber):
    start_firefox('https://meroshare.cdsc.com.np')
    click(S("@selectBranch"))
    dp = S(".select2-search__field")
    write(dpNumber, into=dp)
    press(ENTER)
    write(username, into='username')
    write(password ,into='password')
    click(Button('Login'))

def applyForIPO():
    click(Link('My ASBA'))
    click(Link('Apply for Issue'))
    #write logic to click on IPOs

    # click(S(".company-name > span[tooltip='Company Name']")) you can click like this also
    # currentIssues = find_all(S(".company-name > span[tooltip='Company Name']"))
    # shareType = find_all(S(".company-name > span.share-of-type"))
    # currentIssuesList = [cell.web_element.text for cell in currentIssues]
    # shareTypeList = [cell.web_element.text for cell in shareType]
    # print(shareTypeList)
    # print(currentIssuesList)
    click(Button('Apply'))
    click(S("#selectBank"))


    

def showCurrentIssue():
    #TODO: separate company-name by tooltip=Share Type for IPO and non-IPO (Right Share / Reserved Share)
    # this prints the list of IPOs
    click(Link('Current Issue'))

    #gets the DOM elements for currentIssues 
    currentIssues = find_all(S(".company-name > span[tooltip='Company Name']"))
    shareType = find_all(S(".company-name > span.share-of-type"))
    currentIssuesList = [cell.web_element.text for cell in currentIssues]
    shareTypeList = [cell.web_element.text for cell in shareType]
    print(shareTypeList)
    print(currentIssuesList)

def createCredentials():
    username = input("Enter the username ")
    password = input("Enter the password ")
    dpNumber = input("Enter the dpNumber (bank code) ")
    name = input("Enter the name of the person ")
    return [username, password, dpNumber, name]
    
def updateJSON(fileName):
    with open(fileName, "r+") as credentials:
        data = json.load(credentials)

        mydict = {}
        key = "cred" + str(len(data) + 1)
        value = createCredentials()
        mydict = {key:value}
        data.append(mydict)
        credentials.seek(0)
        json.dump(data, credentials, indent=4)
    

