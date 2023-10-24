import requests
from bs4 import BeautifulSoup



def findBasic(part):
    url = 'https://finance.yahoo.com/quote/'+part
    headers={'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Safari/605.1.15'}
    r=requests.get(url)
    soup=BeautifulSoup(r.text,'html.parser')
    price = soup.find('fin-streamer', {'class': 'Fw(b) Fz(36px) Mb(-4px) D(ib)'}).text
    title=soup.title.text
    title=title[0:title.index('(')-1]
    return (title,price,url)


def findPrecise(part):
    url = 'https://finance.yahoo.com/quote/'+part
    headers={'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Safari/605.1.15'}
    r=requests.get(url)
    soup=BeautifulSoup(r.text,'html.parser')
    data1 = soup.find('div', {'class': 'D(ib) W(1/2) Bxz(bb) Pend(12px) Va(t) ie-7_D(i) smartphone_D(b) smartphone_W(100%) smartphone_Pend(0px) smartphone_BdY smartphone_Bdc($seperatorColor)'}).text
    data2 = soup.find('div', {'class': 'D(ib) W(1/2) Bxz(bb) Pstart(12px) Va(t) ie-7_D(i) ie-7_Pos(a) smartphone_D(b) smartphone_W(100%) smartphone_Pstart(0px) smartphone_BdB smartphone_Bdc($seperatorColor)'}).text
    data=data1+data2

    formatData(data)

def formatData(result):
    nums='0123456789x,.'
    data={}
    temp=0

    for i in range(len(result)):
        key=''
        value=0.0
        if result[i] in nums:
            key=result[temp:i]
            temp=i
            while result[i] in nums:
                i+=1
            print(result[temp:i])
            value=float(result[temp:i])
            temp=i
            data[key]=value
    return data


        
print(findPrecise("AAPL"))        

