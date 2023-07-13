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
    data=['https://www.linkedin.com/in/talhia-pompa-13638260?miniProfileUrn=urn%3Ali%3Afs_miniProfile%3AACoAAAzeejoBwfuJXCp875koUrs8mSl-Jw-w6yI&lipi=urn%3Ali%3Apage%3Ad_flagship3_search_srp_people%3BxQ%2Bu%2B27sR%2Fy3lGGq7Fae6Q%3D%3D', 'https://www.linkedin.com/in/arielmeagher/ https://www.linkedin.com/in/tammy-connelly-3a428013/', 'https://www.linkedin.com/in/ferzeen-najfi-69776a8/', 'https://www.linkedin.com/in/bharti-dhar-9bb8a9109/', 'https://www.linkedin.com/in/anilpuli/', 'https://www.linkedin.com/in/adeelawaller/', 'https://www.linkedin.com/in/adeelawaller/',
'https://www.linkedin.com/in/jennifer-moceri-a825032, https://www.linkedin.com/in/fiona-clare-cicconi-304249/',  'https://www.linkedin.com/in/gluke?miniProfileUrn=urn%3Ali%3Afs_miniProfile%3AACoAABas124BVip_eZiyR6JCi0oeWeFB0SL-lAg&lipi=urn%3Ali%3Apage%3Ad_flagship3_search_srp_people%3BT0ILf5XBTquJrGBhjnkeKw%3D%3D',
'https://www.linkedin.com/in/carol-surface/', 'https://www.linkedin.com/in/jennifertylau/',' https://www.linkedin.com/in/christamumman/','  https://www.linkedin.com/in/divya-ejjigani-5bab7555/ ','https://www.linkedin.com/in/jeremyyjones/',
'https://www.linkedin.com/in/kathleenthogan/',   'https://www.linkedin.com/in/kamaraswaby/',' https://www.linkedin.com/in/vicannia-merisma-ba632934/','  https://www.linkedin.com/in/chioma-acholonu/',' https://www.linkedin.com/in/bethteigue/',  'https://www.linkedin.com/in/jerilynsamuel/', 'https://www.linkedin.com/in/brookesimpson/',
'https://www.linkedin.com/in/nickle-lamoreaux/',   'https://www.linkedin.com/in/seema-balani-68876b121/',' https://www.linkedin.com/in/jill-bunnell-9b66758/','  https://www.linkedin.com/in/deirdre-angus-987b533/', ' https://www.linkedin.com/in/davidwatkins29/',
'https://www.linkedin.com/in/matthew-saxon-aa75245/', 'https://www.linkedin.com/in/laurenmcmillan2015/',' https://www.linkedin.com/in/carrieyuill/','  https://www.linkedin.com/in/karensxiao/', ' https://www.linkedin.com/in/jennifermhall/', 'https://www.linkedin.com/in/jodysimon/', 'https://www.linkedin.com/in/jerrysastri/', 'https://www.linkedin.com/in/ethan-scharf/', 'https://www.linkedin.com/in/valerie-massa-40b16370/',
'https://www.linkedin.com/in/carmelgalvin/', 'https://www.linkedin.com/in/mackenzie-standish-santos-695b581a/',' https://www.linkedin.com/in/madelinemcasey/',  'https://www.linkedin.com/in/nikmedrano/', ' https://www.linkedin.com/in/nushaettefagh/ ' ,
'https://www.linkedin.com/in/kathleen-pacini-phr-b115986/', 'https://www.linkedin.com/in/debbielee/',' https://www.linkedin.com/in/samanthagoffredi/ ',' https://www.linkedin.com/in/brittany-doorish-18395a31/', ' https://www.linkedin.com/in/rockmanha/']
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

# person=Person("https://www.linkedin.com/in/amit-kumar-9a216816b", driver=driver, scrape=False)
# time.sleep(15)
# person.scrape(close_on_complete=False)
#
# name=person.name
# title=person.job_title
# now_company=person.company
# print(name, title, now_company)
# experience=person.experiences
# print(experience)
# current_company=experience[0]
# print(current_company)
# link_to_company=current_company.linkedin_url
# print(link_to_company)
# location=current_company.location
# print(location)
# company=Company(link_to_company, driver=driver)
# company_name=company.name
# company_size=company.company_size
# company_website=company.website
# about=company.about_us
# print(company_name, company_size, company_website, about)

