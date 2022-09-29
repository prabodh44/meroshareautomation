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
    # this prints the list of IPOs
    click(Link('Current Issue'))

    #gets the DOM elements for currentIssues 
    currentIssues = find_all(S(".company-name > span[tooltip='Company Name']"))
    currentIssuesList = [cell.web_element.text for cell in currentIssues]
    print(currentIssues)
    print(currentIssuesList)
    
