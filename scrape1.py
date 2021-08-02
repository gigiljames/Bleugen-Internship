import requests
from lxml import html
import pandas as pd
import csv

#$x('//a[@class="woocommerce-LoopProduct-link woocommerce-loop-product__link"]/h2/text()')
#$x('//a[@class="woocommerce-LoopProduct-link woocommerce-loop-product__link"]/span/span/span/text()')



items=[]
csv1=[['Name','Price','URL']]
url='https://scrapeme.live/shop/page/{}/'
for i in range(1,11):
    r=requests.get(url.format(i))
    html_response=html.fromstring(r.content)
    rows=html_response.xpath('//a[@class="woocommerce-LoopProduct-link woocommerce-loop-product__link"]')
    for row in rows:
        name=row.xpath('h2/text()')
        price=row.xpath('span/span/text()')
        link=row.xpath('@href')
        #print(price,name)
        item = {
            'Name': ''.join(name),
            'Price': '£'+price[0],
            'URL': ''.join(link)
        }
        items.append(item)
        csv1.append([''.join(name),''.join(price),''.join(link)])
print(items)

with open('scrape1.csv','w',newline='') as f:
    w=csv.writer(f)
    w.writerows(csv1)
df=pd.read_csv('scrape1.csv')
