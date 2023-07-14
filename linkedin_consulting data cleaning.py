import csv
from urllib.parse import urlparse

with open(r'C:\Users\User\PycharmProjects\pythonProject\pythonProject\linkedin_consulting_1.csv', 'r', encoding='utf8') as file:
    reader = csv.reader(file)
    data = list(reader)
    new_data=[]
    for i, row in enumerate(data):
        if i%2==0:
            website1=(urlparse(row[1]).netloc).lower()
            website2=(urlparse(row[14]).netloc).lower()
            # print(row[1], row[14])
            print(website1, website2)
            if website1==website2:
                name=row[2].split()
                name=name[0]+ ' ' +name[1]
                print(name, row[8])
                if name==row[8]:
                    new_data.append(row)
                    print(row)
with open('cleaned_linkedin_consulting_1.csv', 'w', encoding="utf-8", newline='') as file:
        writer=csv.writer(file)
        writer.writerows(new_data)
        print(new_data)