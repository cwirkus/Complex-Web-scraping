#Creating a csv file that has the list of Jobs from linkeldin, 
# Along with the company. Then once it does that, it will email 
# it to me to show me the jobs.


#Getting our basic imports
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from datetime import datetime
import time , smtplib , csv 


# Getting my email credentials:
email = "EMAIL_@gmail.com"  #Sending Email
password = "#APP_PASSWORD" #App password for the sending email


#Getting our website
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options = chrome_options)


driver.get("https://www.linkedin.com/login")


time.sleep(3)
#Getting a hold of the resources that we need

my_username = driver.find_element(By.ID , value = "username")
my_pass = driver.find_element(By.ID , value= "password")

#Loging in
my_username.send_keys("#USERNAME")  #Use linkedin email
my_pass.send_keys("#PASSWORD")  # Use linkedin password
my_pass.send_keys(Keys.RETURN)



time.sleep(10)

#redirecting to the different url

                                            #Xpath link
jobs_tab = driver.find_element(By.XPATH , value ='//*[@id="global-nav"]/div/nav/ul/li[3]/a/div/div/li-icon' )
jobs_tab.click()


time.sleep(6)

search_box = driver.find_element(By.XPATH , value= '//*[@id="jobs-search-box-keyword-id-ember222"]' )
search_box.click()
search_box.send_keys("It Support")
search_box.send_keys(Keys.RETURN)


#Getting the getting the job and making the list of jobs by [job title , company]
time.sleep(10)

job_titles = {}
company = {}


# Better selector targeting the job title elements
title_elements = driver.find_elements(By.CSS_SELECTOR, ".job-card-list__title--link strong")
job_location = driver.find_elements(By.CSS_SELECTOR , ".artdeco-entity-lockup__subtitle")
# Alternative approach using XPath
# title_elements = driver.find_elements(By.XPATH, "//span[@aria-label='IT Support Specialist with verification']/strong")

print(f"Number of title elements found: {len(title_elements)}")

for x in range(len(title_elements)):
    job_titles[x] = {
        "Title": title_elements[x].text 
         
    }

for x in range(len(title_elements)):
    company[x] = {
        "Company": job_location[x].text
    }

new_data = 'jobs.csv'
with open(new_data, "w") as new:
    csv_writer = csv.writer(new)
    csv_writer.writerow(["Job Title" , "Company"])

    for x in range(len(job_titles)):
        csv_writer.writerow([job_titles[x] , company[x]])
print(job_titles)


##Getting our email client
subject = 'Jobs picked for you today'
body = "here is list of jobs for you"
message = f"Subject: {subject}\n\n{body}\n\nAttachment: {new_data}"



connection = smtplib.SMTP("smtp.gmail.com", 587)
connection.starttls()
connection.login(email, password)
connection.sendmail(email, "#EMAIL", message) #The email is the recieving email address

# Finishing 
time.sleep(100)
driver.quit()




