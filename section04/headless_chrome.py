from attr import attr
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import time

#크롬 드라이버 자동 업데이트
from webdriver_manager.chrome import ChromeDriverManager


url = "https://play.google.com/store/movies/collection/cluster?clp=0g4XChUKD3RvcHNlbGxpbmdfcGFpZBAHGAQ%3D:S:ANO1ljJvXQM&gsr=ChrSDhcKFQoPdG9wc2VsbGluZ19wYWlkEAcYBA%3D%3D:S:ANO1ljK7jAA&hl=ko&gl=US"
# headers = {
#     "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36",
#     "Accept-Language" : "ko-KR,ko"
# }

#브라우저 꺼짐 방지
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

#headless chrome 추가 : 창 띄우지 않고 실행 해서 메모리 줄임
#headless chrome 사용시 user-agent 넣어주기!
chrome_options.headless = True
chrome_options.add_argument("window-size=1920x1080")
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36")

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

#웹페이지 해당 주소 이동
driver.get(url)
driver.maximize_window()  
# driver = webdriver.Chrome('C:/chromedriver.exe')

#모니터(해상도) 높이인 1080 위치로 스크롤 내리기
driver.execute_script("window.scrollTo(0 , 1080)")

#현재 문서 높이 가져와서 저장
interval = 2
prev_height = driver.execute_script("return document.body.scrollHeight")

while True:
    #화면 가장 아래로 스크롤 내리기
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    time.sleep(interval)

    curr_height = driver.execute_script("return document.body.scrollHeight")
    if curr_height == prev_height:
        break

    prev_height = curr_height

print("스크롤 완료")
#실행 결과 확인(스크린샷)
driver.get_screenshot_as_file("google_movie.png")

soup = BeautifulSoup(driver.page_source, "lxml")

movies = soup.find_all("div", attrs={"class":"Vpfmgd"})     #데이터 일부만 가져옴(50개)
print(len(movies))

for movie in movies:
    title = movie.find("div", attrs={"class":"WsMG1c nnK0zc"}).get_text()
    
    #할인 전 가격
    original_price = movie.find("span", attrs={"class","SUZt4c djCuy"})
    if original_price:
        original_price = original_price.get_text()
    else:
        continue

    #할인 된 가격
    price = movie.find("span", attrs={"class":"VfPpfd ZdBevf i5DZme"}).get_text()

    #링크
    link = movie.find("a", attrs={"class":"JC71ub"})["href"]

    print(f"제목 : {title}")
    print(f"할인 전 금액 : {original_price}")
    print(f"할인 후 금액 : {price}")
    print("링크 : ", "https://play.google.com" + link)
    print("-" * 100)

