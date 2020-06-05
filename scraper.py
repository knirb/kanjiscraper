#This is a scraper I used to get kanji and keywords from a website hosting all of the kanji from the book "Rememebring the Kanji"

from selenium import webdriver #Dealing with browser commands
from bs4 import BeautifulSoup as bs #Html/xml parser
import pandas as pd #To create csvs

#chromedriver is seleniums way of using the browser and needs to be installed. Found at: https://chromedriver.chromium.org/downloads
driver = webdriver.Chrome("C:/Users/vicke/Documents/Python Scripts/Kanjiscraper/chromedriver_win32/chromedriver")

kanjis = []
keywords = []
urls = []
onyomis = []
kunyomis = []


url = "https://hochanh.github.io/rtk/%E4%B8%80/index.html"
stop_url = "https://hochanh.github.io/rtk//index.html"

while url != stop_url:
    driver.get(url)
    urls.append(url)
    content = driver.page_source
    soup = bs(content)
    kanji = soup.find('a', href= "../index.html").text
    keyword = soup.find('h2').find('code').text
    keywords.append(keyword)
    kanjis.append(kanji)
    new_url = soup.find('span', attrs={'class':'right-arrow'}).find('a')['href'][3:]
    url = "https://hochanh.github.io/rtk/" + new_url
    readings = soup.find('h3').find_all('a')
    onyomis.append(readings[0].text)
    if len(readings)!=1:
        kunyomis.append(readings[1].text)
    else:
        kunyomis.append('None')

df = pd.DataFrame({ "Link":urls, 'Onyomi':onyomis, 'Kunyomi':kunyomis, 'Kanji':kanjis, 'Keyword':keywords,})
df.to_csv('rtk-kanjis.csv', index=False, encoding='utf-8')
