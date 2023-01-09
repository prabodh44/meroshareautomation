from time import sleep
from helium import *
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
import pandas as pd

URL = "https://www.merorojgari.com/"
# searchTerm = input("enter the search term ")
searchTerm = "Human Resource"
searchLocation = "kathmandu"
searchCategory = "Information Technology"


driver = start_firefox(URL)
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
jobList = soup.find_all('li', class_="job_listing")
# print(jobList)



# Create a dataframe
df = pd.DataFrame({'Job Names' : [''],
      'Job Companies' : [''],
      'Job Type': [''],
      'Job Link': [''],
      'Job Status' : [''],
      'Job Posted Date': [''],
      'Job Deadline': ['']})

for job in jobList:
        jobName = job.find('h3').text
        jobCompany = job.find('strong').text
        jobType = job.find('li', class_='job-type full-time').text

        date = job.find('time')
        jobPostedDate = date['datetime']

        link = job.find('a')
        jobLink = link['href']

        try:
            jobStatus = job.find('label').text
            jobDeadline = job.find('label').nextSibling
        except:
            jobStatus = 'N/A'
            jobDeadline = 'N/A'
      
        df = df.append({'Job Names' : jobName,
            'Job Companies' : jobCompany,
            'Job Type': jobType,
            'Job Link': link,
            'Job Status' : jobStatus,
            'Job Posted Date': jobPostedDate,
            'Job Deadline': jobDeadline}, ignore_index=True)

try:
      loadMore = soup.find('a', class_="load_more_jobs")
      click(Link('Load more listings'))
      print('load more button found')
except:
      print('load more button not found')



#create an excel file to put the data
df.to_excel('webscrapper.xlsx')


kill_browser()










