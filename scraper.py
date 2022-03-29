# Program to Scrape the Government Jobs website for new jobs.
from plyer import notification
import requests
from bs4 import BeautifulSoup

# Query must have the sorting by date and requires a isDecendingSort boolean.
location = input("Enter your city: ")
state = input("Enter your state (Two letter initials ONLY): ") 
keyword = input("Enter the type of job you are looking for (No input for all job search): ")

if (keyword.strip() == ""):
    keyword = ""
else:
    keyword = "keyword=" + keyword

url = "https://www.governmentjobs.com/jobs?{}&location={}%2C+{}&sort=date&isDescendingSort=True".format(keyword, location, state)


r = requests.get(url)
soup = BeautifulSoup(r.text, "html.parser")


#In this case, we want to look for all list classes with the name job-item
# they will also contain a data job id which i might be able to use for something. not sure.
# maybe use that id to make a link to whatever job might be posted.
# there is a job details href that i can make use of within the listing.

#This loop should allow me to go through the entire first page, if I want to edit this
# to be able to go through the entire site in terms of finishing all the pages, I would have
# to figure out how to change the link after the end of a page.

for job_listing in soup.find_all("li", {"class":"job-item"}):
    for job_link in soup.find_all("a", {"class":"job-details-link"}):
        print(job_link.prettify())

print(url)