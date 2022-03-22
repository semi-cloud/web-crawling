import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/list?titleId=675554"
res = requests.get(url)
res.raise_for_status()

#가우스 전자 웹툰 목록의 제목 + 링크 + 평점 정보 가져오기
soup = BeautifulSoup(res.text, "lxml")  
cartoons = soup.find_all("td", attrs={"class" : "title"})
ratings = soup.find_all("div", attrs={"class" : "rating_type"})

for cartoon in cartoons:
    title = cartoon.a.get_text()
    link = "https://comic.naver.com" + cartoon.a["href"]  
    print(title, link)    #완성된 링크 생성


total_rates = 0
for rate in ratings:
    rate_text = rate.find("strong").get_text()
    total_rates += float(rate_text)

print("평균 점수 : ", total_rates/len(ratings))
    
