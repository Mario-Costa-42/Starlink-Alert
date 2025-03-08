from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://findstarlink.com/#3451668;3').text
soup = BeautifulSoup(html_text, 'lxml')


resultBox = soup.find_all('span', class_ = 'entryTiming bold')
print(resultBox)
