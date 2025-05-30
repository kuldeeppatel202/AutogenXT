from selenium import webdriver
from selenium.webdriver.common.by import By

def scrape_indeed_jobs(keyword, location="India"):
    driver = webdriver.Chrome()
    driver.get(f"https://www.indeed.com/jobs?q={keyword}&l={location}")
    jobs = []
    for elem in driver.find_elements(By.CLASS_NAME, "result"):
        try:
            title = elem.find_element(By.CLASS_NAME, "jobTitle").text
            jd = elem.find_element(By.CLASS_NAME, "job-snippet").text
            jobs.append((title, jd))
        except:
            continue
    driver.quit()
    return jobs
