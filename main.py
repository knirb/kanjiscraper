from selenium import webdriver #Dealing with browser commands
from bs4 import BeautifulSoup as bs #html/xml parser
import pandas as pd #csvs and stuff
driver = webdriver.Chrome("C:/Users/vicke/Documents/Python Scripts/Kanjiscraper/chromedriver_win32/chromedriver")
print("a")
kanjis = []
keywords = []
url = "https://hochanh.github.io/rtk/%E4%B8%80/index.html"
stop_url = "https://hochanh.github.io/rtk//index.html"
while url != stop_url:
    driver.get(url)
    content = driver.page_source
    soup = bs(content)
    kanji = soup.find('a', href= "../index.html").text
    keyword = soup.find('h2').find('code').text
    keywords.append(keyword)
    kanjis.append(kanji)
    new_url = soup.find('span', attrs={'class':'right-arrow'}).find('a')['href'][3:]
    url = "https://hochanh.github.io/rtk/" + new_url
df = pd.DataFrame({'Kanji':kanjis, 'Keyword':keywords})
df.to_csv('rtk-kanjis.csv', index=False, encoding='utf-8')
