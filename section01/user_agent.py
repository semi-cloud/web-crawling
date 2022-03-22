# 웹 크롤링 무단으로 접속 => 사이트에서 차단할 수 있음 = 올바른 정보를 안줌
# 접속하는 브라우저에 따라서 user agent가 달라짐
# user agent를 넣어주면 실제 크롬에서 접속하는 것고 동일한 결과를 나타냄
import requests

url = "http://nadocoding.tistory.com"
headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36"}

res = requests.get(url, headers = headers)      #유저 정보 넘겨주기
res.raise_for_status()  

with open("nadocoding.html", "w", encoding="utf8") as f:
    f.write(res.text)
