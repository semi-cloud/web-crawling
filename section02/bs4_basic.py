#pip install beautifulsoup4
#pip instll lxml

import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")    #soup 객체 생성(모든 html 문서 정보)
# print(soup.title.get_text())
# print(soup.a)          #soup 객체에서 처음 발견되는 a element 반환
# print(soup.a.attrs)    #딕셔너리 형태로 element의 속성 가져오기
# print(soup.a["href"])   #element의 특정 속성 값 가져오기

soup.find("a", attrs={"class" : "Nbtn_upload"})   #element, 속성
rank1 = soup.find("li", attrs={"class" : "rank01"})

#형제 element으로 접근하기
# print(rank1.a.get_text())
# rank2 = rank1.next_sibling.next_sibling     #다음 형제 element
# rank3 = rank2.next_sibling.next_sibling
# print(rank3.a.get_text())
# rank2 = rank3.previous_sibling.previous_sibling   #이전 형제 element

#next sibling 2번 쓰는 대신 아래 코드를 사용
rank2 = rank1.find_next_sibling("li")      #개행 문자는 자동으로 건너뜀
rank1 = rank2.find_previous_sibling("li")

#부모 element으로 접근하기
print(rank1.parent)

#형제들 모두 가져오기
print(rank1.find_next_siblings("li"))

#전체에서 찾아서 가져오기
webtoon = soup.find("a", text = "독립일기-11화 밥공기 딜레마")
print(webtoon)










