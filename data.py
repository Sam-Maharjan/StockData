import requests
from bs4 import BeautifulSoup



def findData(part):
    url = 'https://finance.yahoo.com/quote/'+part
    headers={'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Safari/605.1.15'}
    r=requests.get(url)
    soup=BeautifulSoup(r.text,'html.parser')
    price = soup.find('fin-streamer', {'class': 'Fw(b) Fz(36px) Mb(-4px) D(ib)'}).text
    title=soup.title.text
    title=title[0:title.index('(')-1]
    return (title,price,url)

print(findData("MSFT"))