import requests
from bs4 import BeautifulSoup

url = 'https://www.ptt.cc/bbs/NBA/index.html'
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/127.0.0.0 Safari/537.36'}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html,parser")
articles = soup.find_all("div", class_="r-ent")
if response.status_code == 200:  # 檢查網址有無輸入錯誤
    with open('output.html', 'w', encoding='utf-8') as f:
        f.write(response.text)