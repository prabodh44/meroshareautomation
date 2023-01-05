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


# categoryInput = S(".select2-search__field")
# write(searchCategory, into=categoryInput)
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
jobTypes = [jobType.string for jobType in jobList.find_all('li', class_='job-type')]
# deadlines = [deadline.string for deadline in jobList.find_all('li', class_='application-deadline  ')] -- cannot be printed
jobPostedDates = [jobPostedDate['datetime'] for jobPostedDate in jobList.find_all('time')]

# create a dataframe to store the data
df = pd.DataFrame({'Job Names' : jobNames,
      'Job Companies' : jobCompanies,
      'Job Type': jobTypes,
      'Job Posted Date': jobPostedDates})

print(df)










kill_browser()










