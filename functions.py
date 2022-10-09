from helium import *

def login(username, password):
    start_firefox('https://meroshare.cdsc.com.np')
    click(S("@selectBranch"))
    dp = S(".select2-search__field")
    write('10600', into=dp)
    press(ENTER)
    write(username, into='username')
    write(password ,into='password')
    click(Button('Login'))

def applyForIPO():
    click(Link('My ASBA'))
    #write logic to click on IPOs

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
    
