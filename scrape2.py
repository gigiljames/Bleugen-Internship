import csv
import requests
import pandas as pd
from lxml import html

#$x('//div[@class="summary entry-summary"]/p/span/text()')


url1='https://scrapeme.live/shop/page/{}/'
url2='https://scrapeme.live/shop/{}/'
names,items,csv1=[],[],[['Name','Price','Description','Stock','SKU','Categories','Tags','URL']]
urls=[]
for i in range(1,11):
    r1 = requests.get(url1.format(i))
    html_response1 = html.fromstring(r1.content)
    names.append(html_response1.xpath('//a[@class="woocommerce-LoopProduct-link woocommerce-loop-product__link"]/h2/text()'))
    urls.append(html_response1.xpath('//a[@class="woocommerce-LoopProduct-link woocommerce-loop-product__link"]/@href'))

for j in range(0,len(names)):
    for n in names[j]:
        r2 = requests.get(url2.format(n))
        html_response2 = html.fromstring(r2.content)
        rows=html_response2.xpath('//div[@class="summary entry-summary"]')
        for row in rows:
            name=n
            desc = row.xpath('div/p/text()')
            stock = row.xpath('p[@class="stock in-stock"]/text()')
            price = row.xpath('p[@class="price"]/span/text()')
            sku = row.xpath('div[@class="product_meta"]/span[@class="sku_wrapper"]/span[@class="sku"]/text()')
            cat = row.xpath('div[@class="product_meta"]/span[@class="posted_in"]/a/text()')
            tags = row.xpath('div[@class="product_meta"]//span[@class="tagged_as"]/a/text()')
            csv1.append([name,''.join(price),''.join(desc),''.join(stock),''.join(sku),','.join(cat),','.join(tags),urls[j][names[j].index(n)]])

with open('scrape2.csv','w',newline='') as f:
    w=csv.writer(f)
    w.writerows(csv1)

