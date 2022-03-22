import requests

res = requests.get('https://naver.com')
res.raise_for_status()    #응답 코드 체크(문제가 있으면 오류 내뱉고 종료)

# print("응답코드 : ", res.status_code)  #200 이면 정상

# if res.status_code == requests.codes.ok:
#     print("정상입니다")
# else:
#     print("문제가 생겼습니다. [에러코드 " ,res.status_code, "]")

with open("mygoogle.html", "w", encoding="utf8") as f:
    f.write(res.text)





