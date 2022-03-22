from idna import valid_contextj
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

browser = webdriver.Chrome('C:/chromedriver.exe')
browser.maximize_window()   #창 최대화

url = "https://flight.naver.com/"
browser.get(url)

#도착치 선택
browser.find_element(by=By.CLASS_NAME, value="tabContent_route__1GI8F.select_City__2NOOZ.end").click()
browser.find_elements(by=By.CLASS_NAME, value="autocomplete_Collapse__tP3pM")[0].click() #국내
city = browser.find_elements(by=By.CLASS_NAME, value="autocomplete_Airport__3_dRP")[2]   #부산
city.click()

#가는 날 선택
date_btn = browser.find_elements(by=By.CLASS_NAME, value="tabContent_option__2y4c6")
date_btn[0].click()   

#2022.03~2023.03 1년간의 캘린더 데이터(13개월) 모두 가져오기
month = browser.find_elements(by=By.CSS_SELECTOR, value="div.awesome-calendar div.month")

#2022.03월 각 주차별 데이터 가져오기
go_week = month[0].find_elements(by=By.CSS_SELECTOR, value="table tbody tr")

#2022.03.20 3주차 일별 데이터 가져오기
go_day = go_week[3].find_elements(by=By.CSS_SELECTOR, value="td")

#2022.03.20 일 선택
go_day[1].click()

#오는날 선택
back_week = month[0].find_elements(by=By.CSS_SELECTOR, value="table tbody tr")
back_day = back_week[4].find_elements(by=By.CSS_SELECTOR, value="td")
back_day[4].click()

#항공권 검색 버튼 클릭
flight = browser.find_element(by=By.CLASS_NAME, value="searchBox_search__2KFn3")
flight.click()

#효율적인 로딩 처리(element가 나오기 전까지 최대 10초 기다림)
try:
    elem = WebDriverWait(browser, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "result")))
    print(elem[0].text)   #첫번째 결과 출력
finally:
    browser.quit()








