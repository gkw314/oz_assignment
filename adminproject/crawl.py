import requests
from bs4 import BeautifulSoup

base_url = 'https://kream.co.kr/search?tab='
keyword = input('검색할 키워드를 입력해주세요 : ')

url = base_url + keyword

req = requests.get(url)

html = req.text
soup = BeautifulSoup(html, "html.parser")

results = soup.select(".tab_name")

# for i in results:
#     title = i.select_one(".title_link").text
#     writer = i.select_one(".name").text

#     print(title)
#     print("작성자: ", writer)
#     print("")


print (results)
# print(soup)
# print(req.text)