from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import requests
import pandas as pd
import time
import os

BASE_URL = "https://nastava.foi.hr"
EMPLOYEES_URL = f"{BASE_URL}/employees"

options = Options()
options.add_argument("--headless")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get(EMPLOYEES_URL)
time.sleep(4)  # wait for page to fully load

links = set()
elements = driver.find_elements(By.XPATH, "//a[contains(@href, '/employee/')]")
for el in elements:
    href = el.get_attribute("href")
    if href and "/employee/" in href:
        links.add(href)

driver.quit()

def parse_information(soup):
    info = {}
    for block in soup.select("div.foi-label"):
        label = block.get_text(strip=True)
        value_div = block.find_next_sibling("div", class_="foi-value")
        if value_div:
            value = value_div.get_text(" ", strip=True)
            info[label] = value
    return info

def parse_name(soup):
    name_div = soup.select_one("div.text-h6.mt-4")
    return name_div.get_text(strip=True) if name_div else ""

def parse_subjects(soup):
    return [
        a.get_text(strip=True)
        for a in soup.find_all("a", href=lambda x: x and "/course/" in x)
    ]

def parse_consultations(employee_url):
    """Use Selenium to get consultations including postponed info."""
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get(employee_url)
    time.sleep(2)  # wait for page to load

    try:
        tab_button = driver.find_element(By.XPATH, "//a[contains(text(),'Konzultacije')]")
        driver.execute_script("arguments[0].click();", tab_button)
        time.sleep(1)
    except Exception:
        pass  

    soup = BeautifulSoup(driver.page_source, "html.parser")
    driver.quit()

    consults = []
    tab2 = soup.find("div", {"id": "tab-2"})
    if tab2:
        day_cards = tab2.find_all("div", class_="v-card v-card--raised v-sheet theme--dark")
        for card in day_cards:
            day_tag = card.find("div", class_="text-h6")
            time_tag = card.find("div", class_="font-weight-bold")
            if day_tag and time_tag:
                day = day_tag.get_text(strip=True)
                time_str = time_tag.get_text(strip=True)
                consults.append(f"{day}: {time_str}")
    return consults

def parse_employee_page(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")

    name = parse_name(soup)
    info = parse_information(soup)
    consultations = parse_consultations(url)
    subjects = parse_subjects(soup)

    return {
        "url": url,
        "name": name,
        **info,
        "consultations": consultations,
        "subjects": subjects
    }


results = []
for link in links:
    data = parse_employee_page(link)
    results.append(data)

df = pd.DataFrame(results)
script_dir = os.path.dirname(os.path.abspath(__file__))  
csv_path = os.path.join(script_dir, "foi_employees.csv")

df.to_csv(csv_path, index=False)

