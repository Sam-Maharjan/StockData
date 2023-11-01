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
    t1_div=soup.find('div',{"class":"D(ib) W(1/2) Bxz(bb) Pend(12px) Va(t) ie-7_D(i) smartphone_D(b) smartphone_W(100%) smartphone_Pend(0px) smartphone_BdY smartphone_Bdc($seperatorColor)"})
    t1=t1_div.find('table').find_all("tr")
    lst=[]
    for i in range(len(t1)):
        lst.append(t1[i].text)

    t2_div=soup.find('div',{"class":"D(ib) W(1/2) Bxz(bb) Pstart(12px) Va(t) ie-7_D(i) ie-7_Pos(a) smartphone_D(b) smartphone_W(100%) smartphone_Pstart(0px) smartphone_BdB smartphone_Bdc($seperatorColor)"})
    t2=t1_div.find('table').find_all("tr")
    for i in range(len(t2)):
        lst.append(t2[i].text)

    return formatData(lst)


def formatData(lst):
    nums='0123456789'
    ex='52 Week Range'
    data={}
    for val in lst:
        for j in range(len(val)):
            if(val[j] in nums and j>2):  
                data[val[:j]]=val[j:]
                break
            

    return data
        


