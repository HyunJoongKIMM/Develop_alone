#########################################################################################################
import requests
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import random

# <--------------------------- 웹 크롤링 --------------------------->
url = "https://en.wiktionary.org/wiki/Wiktionary:Frequency_lists/Korean_5800"
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36'}
data  = requests.get(url, headers=headers)
soup = BeautifulSoup(data.text, 'html.parser')



# <------------ 해당 단어들 가져오기 및 리스트에 넣어두기 ------------>
wordList = []

spans = soup.find_all("span", "Kore")
for span in spans:
    wordList.append(span.text)

random.shuffle(wordList)                    # 리스트 내용들 매번 랜덤으로 섞음
#print(wordList)                            # 리스트 내용 출력
#print(len(wordList))                       # 5467 개


# <-------------------- 브라우저 자동 종료 방지 -------------------->
options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options)
driver.get('https://semantle-ko.newsjel.ly/')
driver.maximize_window()
time.sleep(3)

search_box = driver.find_element(By.XPATH, '//*[@id="guess"]')
for i in wordList:
    search_box.send_keys(i)                 # 리스트 값 넣기
    search_box.send_keys(Keys.RETURN)       # 엔터랑 같은 효과
time.sleep(1)


#########################################################################################################





# 일단 아래 코드는 미사용..
# def ggomantle_auto():
#     driver = webdriver.Chrome()
#     driver.get('https://semantle-ko.newsjel.ly/')
#     driver.maximize_window()
#     time.sleep(3)


#     search_box = driver.find_element(By.XPATH, '//*[@id="guess"]')

#     for i in wordList:
#         search_box.send_keys(i)
#         search_box.send_keys(Keys.RETURN)
#     time.sleep(1)

#     while(True):        # 창 안꺼지게 하기
#         pass

#ggomantle_auto()