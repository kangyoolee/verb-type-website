import requests
from bs4 import BeautifulSoup

verb = str(input())
url = f'https://conjugator.reverso.net/conjugation-english-verb-{verb}.html'

response = requests.get(url)

if response.status_code == 200:
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
#   ch_divSimple > div > div:nth-child(1) > div:nth-child(2) > div > p

    past_participle2 = soup.select_one('#ch_divSimple > div > div:nth-child(2) > div:nth-child(1) > div > ul > li:nth-child(1) > i.verbtxt')
    present = soup.select_one('#ch_divSimple > div > div:nth-child(1) > div:nth-child(2) > div > ul > li:nth-child(1) > i.verbtxt')
    past = soup.select_one("#ch_divSimple > div > div:nth-child(1) > div:nth-child(3) > div > ul > li:nth-child(1) > i.verbtxt")

    print(present.string, past.string, past_participle2.string)

else :
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    error = soup.select_one('#ch_lblCustomMessage')
    print(error.string)
    
    
    
# 현재형 #ch_divSimple > div > div:nth-child(1) > div:nth-child(2) > div > ul > li:nth-child(1) > i.verbtxt
# 과거형 #ch_divSimple > div > div:nth-child(1) > div:nth-child(3) > div > ul > li:nth-child(1) > i.verbtxt
# 현재진행형 #ch_divSimple > div > div:nth-child(1) > div:nth-child(4) > div > ul > li:nth-child(1) > i.verbtxt
# 현재완료형 #ch_divSimple > div > div:nth-child(3) > div:nth-child(1) > div > ul > li:nth-child(1) > i.verbtxt
# 미래시제 #ch_divSimple > div > div:nth-child(3) > div:nth-child(2) > div > ul > li:nth-child(1) > i.verbtxt
# 미래완료시제 #ch_divSimple > div > div:nth-child(3) > div:nth-child(3) > div > ul > li:nth-child(1) > i.verbtxt
# 과거진행시제 #ch_divSimple > div > div:nth-child(4) > div:nth-child(1) > div > ul > li:nth-child(1) > i.verbtxt
# 과거완료시제 #ch_divSimple > div > div:nth-child(4) > div:nth-child(2) > div > ul > li:nth-child(1) > i.verbtxt
# 미래진행시제 #ch_divSimple > div > div:nth-child(4) > div:nth-child(3) > div > ul > li:nth-child(1) > i.verbtxt
# 현재완료진행시제 #ch_divSimple > div > div:nth-child(4) > div:nth-child(3) > div > ul > li:nth-child(1) > i.verbtxt
# 과거완료진행시제 #ch_divSimple > div > div:nth-child(5) > div:nth-child(2) > div > ul > li:nth-child(1) > i.verbtxt
# 미래완료진행시제 #ch_divSimple > div > div:nth-child(5) > div:nth-child(3) > div > ul > li:nth-child(1) > i.verbtxt