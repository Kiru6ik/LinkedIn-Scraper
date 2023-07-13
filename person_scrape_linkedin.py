import csv
from selenium import webdriver
from linkedin_scraper import Person, actions, Company
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time, pickle
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import WebDriverException

def person_scrape(link, driver):
    person = Person(link, driver=driver, scrape=False)
    time.sleep(10)
    person.scrape(close_on_complete=False)

    name = person.name
    title = person.job_title
    now_company = person.company

    experience = person.experiences
    current_company = experience[0]
    link_to_company = current_company.linkedin_url
    location = current_company.location
    about_person=person.about
    time.sleep(7)
    # company = Company(link_to_company, driver=driver, close_on_complete=False, get_employees=False)
    # company_size = company.company_size
    # company_website = company.website
    # about_company = company.about_us

    list=[name, title, about_person, now_company, link_to_company, location] #, company_size, company_website, about_company, location]
    # print(list)
    return list

def company_scrape(link_to_company, driver):
    company = Company(link_to_company, driver=driver, close_on_complete=False)
    company_size = company.company_size
    company_website = company.website
    about = company.about_us
    list=[company_size, company_website, about]
    # print(company_size, company_website, about)
    return list

options = Options()
options.add_argument("user-data-dir=C:\\Users\\User\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 3")

new_data=[]
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

#update to include normail formatting, now it saves all the rows
i=0
with open(r'C:\Users\User\Downloads\Telegram Desktop\consulting_profiles1(1-103).csv', 'r', encoding='utf8') as file:
    reader=csv.reader(file)
    data=list(reader)
    try:
        for row in data:
            row=[row]
            try:
                person_info=person_scrape(row[0], driver)
                # print(person_info)
                row.extend(person_info)
                i+=1
                print(row)
                new_data.append(row)
                print('new person', i)
                # if i>4:
                #     break
                if i % 5 == 0:
                    time.sleep(30)
                else:
                    time.sleep(7)
            except WebDriverException as e:
                print(e)
                pass
            except Exception as e:
                print(e)
                pass
    except KeyboardInterrupt:
        try:
            with open('emergency_save_person_data.pickle', 'wb') as file:
                pickle.dump(new_data, file)
        except:
            pass
try:
    with open('person_data.pickle', 'wb') as file:
        pickle.dump(new_data, file)
except:
    pass
try:
    with open('talent_linkedin.csv', 'w', encoding="utf-8", newline='') as file:
        writer=csv.writer(file)
        writer.writerows(new_data)
        print(new_data)
except:
    print(new_data)

try:
    with open('linkedin_consulting_extra_save.csv', 'w', encoding="utf-8", newline='') as file:
        writer=csv.writer(file)
        writer.writerows(data)
        print(data)
except:
    print(data)
