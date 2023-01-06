from time import sleep
from helium import *
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
import pandas as pd
import re
import requests
import json

URL = "https://www.merorojgari.com/"
# searchTerm = input("enter the search term ")
searchTerm = "dental hygienist"
searchLocation = "kathmandu"
searchCategory = "government"


driver = start_firefox(URL, headless=True)
searchInput = S("@search_keywords")
write(searchTerm, into=searchInput)

locationInput = S("@search_location")
write(searchLocation, into=locationInput)


categoryInput = S(".select2-search__field")
write(searchCategory, into=categoryInput)
click(Button('Search Jobs'))

sleep(3) # wait 3 seconds before scraping


DOMTree = driver.execute_script("return document.body.outerHTML;")


# scrap data using BeautifulSoup
# soup = BeautifulSoup(driver.get_source, "html.parser") -- driver.get_source doesnot work for some reason
# jobListings = soup.find('ul', class_="job_listings").find("h3")

# scrap data using BeautifulSoup
# headers: jobName, jobCompany, jobType,  applicationDeadline, jobDate
soup = BeautifulSoup(DOMTree, "html.parser")
jobList = soup.find('ul', class_="job_listings")
jobNames = [jobName.string for jobName in jobList.find_all('h3')]
jobCompanies = [jobCompany.string for jobCompany in jobList.find_all('strong')]
# added to class full-time to display only full time jobs and filter out fresher jobs
jobTypes = [jobType.string for jobType in jobList.find_all('li', class_='job-type full-time')]
# deadlines = [deadline for deadline in jobList.find_all('li', class_="application-deadline expiring expired").contents[1]]
jobPostedDates = [jobPostedDate['datetime'] for jobPostedDate in jobList.find_all('time')]
jobLinks = [jobLink['href'] for jobLink in jobList.find_all('a')]


# deadlines = ["None" if deadline.find('label').nextSibling is None else deadline.find('label').nextSibling for deadline in jobList.find_all('li', class_='application-deadline expiring expired')]
# print(deadlines)
deadlines = []
jobStatuses = []
for deadline in jobList.find_all('ul', class_='meta'):
    jobDeadline = deadline.find('li', class_='application-deadline expiring expired')
    if jobDeadline is not None:
        deadlines.append(jobDeadline.find('label').nextSibling)
        jobStatuses.append(jobDeadline.find('label').string)
    else:
        deadlines.append('None')
        jobStatuses.append('None')    

print(len(jobNames))
print(jobTypes)
print(len(jobCompanies))
print(len(jobLinks))
print(len(jobStatuses))
print(len(jobPostedDates))
print(len(deadlines))
# create a dataframe to store the data
df = pd.DataFrame({'Job Names' : jobNames,
      'Job Companies' : jobCompanies,
      'Job Type': jobTypes,
      'Job Link': jobLinks,
      'Job Status' : jobStatuses,
      'Job Posted Date': jobPostedDates,
      'Job Deadline': deadlines})

print(df)

#create an excel file to put the data
df.to_excel('scrapped_data.xlsx')










kill_browser()










