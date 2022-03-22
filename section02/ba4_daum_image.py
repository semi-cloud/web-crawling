import requests
from bs4 import BeautifulSoup
headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36"}

# 이미지가 a태그의 링크로 연결되어 있는 경우는 다운로드 가 안뜸(img 태그에서야 저장 가능)
#2015-2019 상위 다섯개 영화 정보 저장
for year in range(2015, 2019):
    url = "https://search.daum.net/search?w=tot&q={}%EB%85%84%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&DA=MOR&rtmaxcoll=MOR".format(year)

    res = requests.get(url, headers)
    res.raise_for_status()

    soup = BeautifulSoup(res.text, "lxml")

    images = soup.find_all("img", attrs={"class", "thumb_img"})

    for idx, image in enumerate(images):
        # image_url= image["src"]
        # if image_url.startswith("//"):
        #     image_url = "https:" + image_url    
        image_res = requests.get(image["src"])
        image_res.raise_for_status()

        with open("movie_{}_{}.jpg".format(year, idx+1), "wb") as f:    #파일 저장
            f.write(image_res.content)

        if idx >= 4:    #상위 다섯개 이미지만 저장
            break


