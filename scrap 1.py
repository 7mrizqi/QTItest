import requests
from bs4 import BeautifulSoup
from csv import writer


url = "https://www.pikiran-rakyat.com/"

webs = requests.get(url)  
soup = BeautifulSoup (webs.content, 'html.parser')

with open('QTI-test.csv', 'w', encoding='utf8', newline='')as file:
    write = writer(file)
    header = ['Title']
    write.writerow(header)

    populer = soup.find_all('div',class_='most__item')
    for p in populer:
        Title = p.find('h2',class_='most__title').get_text()
        res = [Title]
        # print (res)
        write.writerow(res)
