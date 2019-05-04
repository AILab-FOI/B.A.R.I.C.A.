
import urllib.request

from bs4 import BeautifulSoup

from time import sleep

import os

from PIL import Image

import selenium 
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

def scrapProfessorsForTrain():

    print('--> SCRAP PROFESSORS FOR TRAIN AND DICTIONARY')

    urlpage =  'https://nastava.foi.hr/'

    page = urllib.request.urlopen(urlpage)

    soup = BeautifulSoup(page, 'html.parser')

    nastavnici = soup.findAll('div', {'class': 'media-body'})

    professors = {}
    
    for div in nastavnici:
        h = div.find('h4', {'class': 'media-heading'})
        a = h.find('a')
        b = a.get_text().split(',')[0].strip()
        arr = b.split(' ')
        name = []
        for elem in arr:
            if not elem.endswith('.'):
                name.append([elem])
        professors[' '.join(word[0] for word in name)] = a['href'].split('=')[1]

    return(professors)


def scrapProfessorsForPresentation():

    print('--> SCRAP PROFESSORS FOR PRESENTATION')

    dirname = os.path.dirname(os.path.abspath('__file__'))
    filename = os.path.join(dirname, 'build/images/professors')
    
    if not os.path.exists(filename):
        os.makedirs(filename)

    professors = scrapProfessorsForTrain()

    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--window-size=1920x1080')
    
    driver = webdriver.Chrome(options=chrome_options)

    for name, user_name in professors.items():
        driver.get('https://nastava.foi.hr/?username=' + user_name)
        user_name_split = user_name.split('#')
        driver.find_element_by_id("teacherRightContentPanel").screenshot(
        os.path.join(filename, user_name_split[0]+ '.png'))
        print('spremljeno')

def scrapSchedule(kind_of_study, year_of_study, group):

    print('--> SCRAP SCHEDULE')

    chrome_options = Options()
    chrome_options.add_argument("--window-size=1920x1080")
    
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://nastava.foi.hr/public/schedule")

    select_kind_of_study = Select(driver.find_element(By.ID, "study" ))   
    select_kind_of_study.select_by_value(kind_of_study)

    select_year_of_study = Select(driver.find_element(By.ID, "year" ))   
    select_year_of_study.select_by_value(year_of_study)

    element = WebDriverWait(driver, 5).until(
                    EC.presence_of_element_located((By.NAME, "studentGroup")))
    select_group = Select(driver.find_element(By.ID, "studentGroup" ))   
    select_group.select_by_visible_text(group)

    button = driver.find_element(By.NAME, "_action_schedule")
    button.click()

    element = driver.find_element(By.ID, "calendar")

    actions = ActionChains(driver)
    actions.move_to_element(element).perform()

    return driver
    

def scrapGroups(kind_of_study, year_of_study):

    print('--> SCRAP GROUPS FOR SCHEDULE')

    options = Options()
    options.add_argument('headless')
    driver = selenium.webdriver.Chrome(options=options)
    driver.get("https://nastava.foi.hr/public/schedule")

    select_kind_of_study = Select(driver.find_element(By.ID, "study" ))   
    select_kind_of_study.select_by_value(kind_of_study)

    select_year_of_study = Select(driver.find_element(By.ID, "year" ))   
    select_year_of_study.select_by_value(year_of_study)
    
    button = driver.find_element(By.NAME, "_action_schedule")
    button.click()

    sleep(1)
    td = driver.find_element(By.NAME, "studentGroup")
    
    if (td.text != ''):
        return_text = '<blockquote><ul>'
        groups = td.text.split('\n')
        for group in groups:
            return_text += ('<li>' + group + '</li>')
        return_text += '</ul></blockquote>'
        return return_text
    else: return 'Nema'

def scrapAllGroups():

    print('--> SCRAP ALL GROUPS')

    options = Options()
    options.add_argument('headless')
    driver = selenium.webdriver.Chrome(options=options)
    driver.get("https://nastava.foi.hr/public/schedule")

    kinds_of_study = driver.find_element(By.ID, "study").find_elements_by_css_selector("*")
    years_of_study = ["1", "2", "3"]

    groups = set()
    
    for kind in kinds_of_study:

        select_kind_of_study = Select(driver.find_element(By.ID, "study" ))
        select_kind_of_study.select_by_visible_text(kind.text)
        
        for year in years_of_study:

            select_year_of_study = Select(driver.find_element(By.ID, "year" ))   
            select_year_of_study.select_by_value(str(year))

            try:
                element = WebDriverWait(driver, 3).until(
                    EC.presence_of_element_located((By.NAME, "studentGroup")))
                g = driver.find_element(By.NAME, "studentGroup").text
                if g != '':
                    g_list = g.split('\n')
                    for elem in g_list:
                        groups.add(elem)
            except: pass       

    return groups
    

def scrapSchedulesForPresentation():

    print ('--> SCRAP SCHEDULES FOR PRESENTATION')

    chrome_options = Options()
    #chrome_options.add_argument("--headless")
    #chrome_options.add_argument("--window-size=1920x1080")
    
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://nastava.foi.hr/public/schedule")

    kinds_of_study = ['2824', '2825', '44700']
    '''kinds = []
    for k in kinds_of_study:
        kinds.append(k.get_attribute('value'))
    print(kinds)'''
    #kinds_of_study = driver.find_element(By.ID, "study").find_elements_by_css_selector("*")
    years_of_study = ['1', '2', '3']
    
    for kind in kinds_of_study:
        try:
            
            driver.execute_script("window.scrollTo(0, 0)")
            

            #element = WebDriverWait(driver, 10).until(
                    #EC.frame_to_be_available_and_switch_to_it((By.ID, "study")))
            
            select_kind_of_study = Select(driver.find_element(By.ID, "study" ))
            #select_kind_of_study.select_by_value(kind.get_attribute('value'))
            select_kind_of_study.select_by_value(kind)

            #string_kind = str(kind.get_attribute('value'))
            string_kind = str(kind)
            
            for year in years_of_study:

                driver.execute_script("window.scrollTo(0, 0)")

                select_year_of_study = Select(driver.find_element(By.ID, "year" ))   
                select_year_of_study.select_by_value(str(year))


                element = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.NAME, "studentGroup")))
                
                g = driver.find_element(By.NAME, "studentGroup").text
                if g != '':
                    g_list = g.split('\n')
                    for elem in g_list:
                        scSchedule(driver, string_kind, year, elem)
                                               
        except Exception as e:
            #print(e)
            pass

def scSchedule(driver, kind, year, elem):

    select_group = Select(driver.find_element(By.ID, "studentGroup" ))
    select_group.select_by_visible_text(elem)

    driver.execute_script("window.scrollTo(0, 0)")

    button = driver.find_element(By.NAME, "_action_schedule")
    button.click()
    sleep(1)

    image_name = os.path.join('build\\images\\schedules', 'sch-' + kind
                     + '-' + str(year) + '-' + elem +  '.png')

    driver.find_element_by_id("calendar").screenshot(image_name)

    size = (0, 0, 1800, 900)
    image = Image.open(image_name)
    region = image.crop(size)
    region.save(image_name, 'PNG', optimize=True, quality=95)
	
    print('spremljeno')



    


                
    
    

