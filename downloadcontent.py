import requests
from bs4 import BeautifulSoup
import numpy as np
# stock satic data sequenced by stocks
stocks=['SPK','SML','OCA','CVT','AIR','SAN']
buyprice=[400,480,87,225,85,600]
buyquan=[720,830,19000,2100,6000,500]

#print(stocks)
def get_price(stocks):
    curprice=[]
    for istock in stocks: 
        url='https://www.nzx.com/instruments/' + istock
        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'html.parser')
        thing=soup.find_all('h1')
        thing=thing[-1]
        thing=str(thing)
        index=thing.find('$')
        price=float(thing[index+1:index+7])
        curprice.append(price)
    return curprice 

curprice=get_price(stocks)
diffprice=np.array(curprice)-np.array(buyprice)/100
totalgain=diffprice.dot(buyquan)
indigain=diffprice*buyquan 
print(stocks)
print(curprice)
print(indigain)
print(totalgain)

#sum=buyquan.dot(diffprice)
