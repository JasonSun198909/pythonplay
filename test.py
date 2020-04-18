import requests
from bs4 import BeautifulSoup
headers = {
  'user-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1'
}

login_data = {
  'username': '3065267',
  'password': '6653893Sunzhe'
}
with requests.Session() as s:
    url = 'https://www.directbroking.co.nz/DirectTrade/dynamic/signon.aspx?rst=637225806879999876'
   # r = s.get(url, headers=headers)
    #
    # soup = BeautifulSoup(r.content, 'html5lib')
    r = s.post(url, data=login_data, headers=headers)
    #print(r.content)
    print(r)