import requests
import re
from bs4 import BeautifulSoup

url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page=2&rocketAll=false&searchIndexingToken=1=6&backgroundColor="
headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36"}
res = requests.get(url, headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

#광고 붙은/붙지 않은 모든 제품 가져오기

items = soup.find_all("li", attrs={"class":re.compile("^search-product")})

for item in items:
    # 광고 제품은 제외
    ad_badge = item.find("span", attrs={"class":"ad-badge-text"})
    if ad_badge:
        print(" <광고 상품은 제외합니다>")
        continue

    name = item.find("div", attrs={"class":"name"}).get_text()
    
    #애플 제품 제외
    if "Apple" in name:
        print("  <Apple 상품 제외합니다>")
        continue
    
    price = item.find("strong", attrs={"class":"price-value"}).get_text()
    rate = item.find("em", attrs={"class":"rating"})
    
    #리뷰 100개 이상, 평점 4.5이상 되는 것만 조회
    if rate:
        rate = rate.get_text()
    else:
        print("  <평점 없는 상품 제외합니다>")
        continue

    rate_cnt = item.find("span", attrs={"class":"rating-total-count"})

    if rate_cnt:
        rate_cnt = rate_cnt.get_text()    #예 : (26)
        rate_cnt = rate_cnt[1:-1]
    else:
        print("  <평점 수 없는 상품 제외합니다>")
        continue

    if float(rate) >=4.5 and int(rate_cnt) > 100 :
        print(name, price, rate, rate_cnt)





