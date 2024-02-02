import requests
import bs4

# print("hhh")
url = "https://www.hinatazaka46.com/s/official/search/artist?ima=0000"

html = requests.get(url)

objSoup = bs4.BeautifulSoup(html.text,'lxml')

members = objSoup.find_all('div', class_ = "sorted sort-syllabary")[0] #togeher as one obj in the list, use [0] to extract


member_list = members.find_all('li', class_ = "p-member__item")

for member in member_list:
    names = member.find_all('div',class_ = "c-member__name")
    name = names[0].text.strip() #it has space at front and end, use "strip" to remove
    print(name) 

