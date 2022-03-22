from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome('C:/chromedriver.exe')
#1.네이버 이동
browser.get("http://naver.com")

#2.로그인 버튼 클릭
elem = browser.find_element(by=By.CLASS_NAME, value="link_login")
elem.click()

#3.id,pw 입력
browser.find_element(by=By.ID, value="id").send_keys("naver_id")
browser.find_element(by=By.ID, value="pw").send_keys("password")

#4.로그인 버튼 클릭
browser.find_element(by=By.ID, value="log.login").click()

time.sleep(3)

#5.아이디 새로 입력
browser.find_element(by=By.ID, value="id").clear()
browser.find_element(by=By.ID, value="id").send_keys("sksmsrkdtpal")
browser.find_element(by=By.ID, value="pw").send_keys("tpal7184!")

#6. html 정보 출력
print(browser.page_source)

#7. 브라우저 종료
browser.close()   #현재 탭만 종료
browser.quit()   #브라우저 전체 종료

# #검색창에 입력
# elem = browser.find_element_by_id("query")
# elem.send_keys("나도코딩")
# elem.send_keys(Keys.ENTER)    #엔터 키

# #모든 a태그 가져오기
# elem = browser.find_elements(by=By.TAG_NAME, value="a")
# for e in elem:
#     e.get_attribute("href")
    
