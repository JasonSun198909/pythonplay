from urllib import request

airnzurl='https://query1.finance.yahoo.com/v7/finance/download/AIR.NZ?period1=1555406535&period2=1587028935&interval=1d&events=history'

def downloadStockData(csv_ural):
    response=request.urlopen(csv_ural)
    csv=response.read()
    csv_str=str(csv)
    lines=csv_str.split("\\n")
    lastline=lines[-1]
    thing=lastline.split(",")
    print(thing[-2])
    # dest_url=r'airnz.csv'
    # fx=open(dest_url,'w')
    # for line in lines:    
    #     fx.write(line + "\n")
    # fx.close()

downloadStockData(airnzurl)
