from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import csv
import keys2
from twilio.rest import Client

url = 'https://cryptoslate.com/coins/'
# Request in case 404 Forbidden error
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}

req = Request(url, headers=headers)

webpage = urlopen(req).read()

soup = BeautifulSoup(webpage, 'html.parser')

rows = soup.findAll("tr")

for row in rows[1:6]:
    column = row.findAll("td")
    if column:
        name = column[1].text
        price = column[2].text
        change = column[3].text
        
        if '-' in change:
            change = change.split('-')
            change = '-' + change[1]
        else:
            change = change.split('+')
            change = '+' + change[1] 

        price1 = price.replace("$","")
        price1 = price1.replace(",","")
        price1 = float(price1)
        
        if '+' in change:
            change1 = change.replace("+","")
            change1 = change1.replace("%","")
            change1 = float(change1)
            percent = change1/100
            percent_change = 1 - percent
            old_price = price1 * percent_change

        if '-' in change:
            change1 = change.replace("-","")
            change1 = change1.replace("%","")
            change1 = float(change1)
            percent = change1/100
            percent_change = 1 + percent
            old_price = price1 * percent_change

        print("Name:", name)
        print("Price:", price)
        print("Change:", change)  
        print("Old Price:", "${:,.2f}".format(old_price))
        print()

         
        
####


client = Client(keys2.accountSID,keys2.authToken)

TwilioNumber = '+15304866233'

myCellPhone = '+18326289593'

for row in rows[1:2]:
    column = row.findAll("td")
    if column:
        Bitcoin_Price = column[2].text
        Bitcoin_Price = Bitcoin_Price.replace("$","")
        Bitcoin_Price = Bitcoin_Price.replace(",","")
        Bitcoin_Price = float(Bitcoin_Price)

if Bitcoin_Price < 40000:
    textmessage = client.messages.create(to=myCellPhone,from_=TwilioNumber, body="BTC has fallen below $40,000!")

for row in rows[2:3]:
    column = row.findAll("td")
    if column:
        Ethereum = column[2].text
        Ethereum = Ethereum.replace("$","")
        Ethereum = Ethereum.replace(",","")
        Ethereum = float(Ethereum)

if Ethereum < 3000:
    textmessage = client.messages.create(to=myCellPhone,from_=TwilioNumber, body="ETH has fallen below $3,000!")

