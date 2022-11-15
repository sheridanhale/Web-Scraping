from urllib.request import urlopen, Request
from bs4 import BeautifulSoup




##############FOR MACS THAT HAVE ERRORS LOOK HERE################
## https://timonweb.com/tutorials/fixing-certificate_verify_failed-error-when-trying-requests_html-out-on-mac/

############## ALTERNATIVELY IF PASSWORD IS AN ISSUE FOR MAC USERS ########################
##  > cd "/Applications/Python 3.6/"
##  > sudo "./Install Certificates.command"


#url = 'https://www.tradingview.com/markets/stocks-usa/market-movers-gainers/'
url = 'https://www.webull.com/quote/us/gainers'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}

#all of this is the same 
req = Request(url, headers=headers)

webpage = urlopen(req).read()

soup = BeautifulSoup(webpage, 'html.parser')
#now it changes
title= soup.title

print (title.text)






#SOME USEFUL FUNCTIONS IN BEAUTIFULSOUP
#-----------------------------------------------#
# find(tag, attributes, recursive, text, keywords)
# findAll(tag, attributes, recursive, text, limit, keywords)

#Tags: find("h1","h2","h3", etc.)
#Attributes: find("span", {"class":{"green","red"}})
#Text: nameList = Objfind(text="the prince")
#Limit = find with limit of 1
#keyword: allText = Obj.find(id="title",class="text")

#trying to grab the 1 that has no tags. .text
#[0] gets you first element

#print company name 
#<p class="txt">Selina Hospitality PLC</
#print percentage change
#<span class="csr88">+305.15%</span>

tablecells = soup.findAll("div",attrs={"class":"table-cell"})
counter = 1

for x in range(5):
    name = tablecells[counter].text
    change = tablecells[counter+2].text
    high = float(tablecells[counter+4].text)
    low = float(tablecells[counter+5].text)

    calc_change = round(((high - low)/low) * 100, 2)
    print(name)
    print(f"change%: {change}")
    print(f"High: {high}")
    print(f"Low: {low}")
    print(f"Calculated change%: {calc_change}%")
    print()
    print()
    counter += 11



#for row in tablecells:
    #print(row.text)

#trying to grab the 1 that has no tags. .text
#[0] gets you first element

#print company name 
#<p class="txt">Selina Hospitality PLC</
#print percentage change
#<span class="csr88">+305.15%</span>
#name = 1
#high = 5
#low = 6