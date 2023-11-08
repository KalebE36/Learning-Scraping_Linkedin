import csv
import getpass
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import time



file = open('linkedinjobdata', 'a')
exporter = csv.writer(file)
exporter.writerow(['Job Title', 'Company Name', 'Job Location'])

driver = webdriver.Chrome()
url = "https://linkedin.com/uas/login"

r = driver.get(url)
input_username = input("Enter linekdin username you want to use: ")
input_password = getpass.getpass("Enter linkedin password you want to use: ")
input_job_search = input("Enter what job you would like to search: ")

username = driver.find_element(By.ID, "username")
password = driver.find_element(By.ID, "password")

username.send_keys(input_username)
password.send_keys(input_password)

driver.find_element(By.XPATH, "//button[@type='submit']").click()
time.sleep(20)

driver.find_element(By.XPATH, "//*[@id='global-nav']/div/nav/ul/li[3]/a").click()
time.sleep(3)

search = driver.find_element(By.CLASS_NAME, "jobs-search-box__text-input")
time.sleep(1.5)

search.send_keys(input_job_search)
driver.find_element(By.CLASS_NAME, "jobs-search-box__submit-button").click()
time.sleep(3)

page_source = driver.page_source
clean_html = BeautifulSoup(page_source, 'html.parser')

jobs = clean_html.find_all('div', class_='job-card-container relative job-card-list')
print(jobs)




















