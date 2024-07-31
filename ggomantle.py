import requests
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# <-- 웹 크롤링 -->
url = "https://en.wiktionary.org/wiki/Wiktionary:Frequency_lists/Korean_5800"
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36'}
data  = requests.get(url, headers=headers)
soup = BeautifulSoup(data.text, 'html.parser')
# <-------------->

wordList = []

# <--- 해당 단어들 가져오기 및 리스트에 넣어두기 --->
divs = soup.find_all("span", "Kore")
for div in divs:
    wordList.append(div.text)
    #print(div.text)

#print(wordList)       # 리스트 내용 출력
#print(len(wordList))  # 5467 개
#<-------------------------------------------------->

# 일단은 while문으로 창 꺼지는 현상 방지함.
# 컴파일 종료하면 창도 같이 꺼져버림 -> 유지하는 방법 따로 생각..

def ggomantle_auto():
    driver = webdriver.Chrome()
    driver.get('https://semantle-ko.newsjel.ly/')
    driver.maximize_window()
    time.sleep(3)


    search_box = driver.find_element(By.XPATH, '//*[@id="guess"]')

    for i in wordList:
        search_box.send_keys(i)
        search_box.send_keys(Keys.RETURN)
    time.sleep(1)

    while(True):        # 창 안꺼지게 하기
        pass

ggomantle_auto()




# ================================== garbage code ===========================================

#from selenium.webdriver.chrome.options import Options

#chrome_options = Options()
#chrome_options.add_experimental_option("detach", True)    # == 브라우저가 종료되도 세션 유지하여 다시 접속 할 수 있게 하는 기능. 
