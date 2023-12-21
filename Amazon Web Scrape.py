#!/usr/bin/env python

## Create a script that webScrape Amazon using scrapy and Xpath to get the text of the xpath and write it to a file

import requests
from lxml import html
import csv

#url = 'https://www.amazon.com/Apple-iPhone-64GB-Space-Gray/dp/B07J2XQZ9S/ref=sr_1_1?keywords=iphone+11&qid=1573120003&sr=8-1'
url = 'https://www.amazon.ae/dp/B09V3JN357'
# Get the page

page = requests.get(url)

print(page.content)

# Parse the page

tree = html.fromstring(page.content)

# Get the title

title = tree.xpath('//span[@id="productTitle"]/text()')

# Get the price

price = tree.xpath('//span[@id="priceblock_ourprice"]/text()')

# Get the rating

rating = tree.xpath('//span[@id="acrPopover"]/@title')

# Get the number of reviews

reviews = tree.xpath('//span[@id="acrCustomerReviewText"]/text()')

# Get the availability

availability = tree.xpath('//div[@id="availability"]/span/text()')

# Get the description

description = tree.xpath('//div[@id="feature-bullets"]/ul/li/span/text()')

# Get the image

image = tree.xpath('//div[@id="imgTagWrapperId"]/img/@data-a-dynamic-image')

# Get the features

features = tree.xpath('//div[@id="feature-bullets"]/ul/li/span/text()')

# Get the details

details = tree.xpath('//div[@id="detail-bullets"]/table/tbody/tr/td/span/text()')

# Get the seller

seller = tree.xpath('//div[@id="merchant-info"]/a/text()')

# Get the seller rating

seller_rating = tree.xpath('//div[@id="averageCustomerReviews"]/span/a/i/span/text()')

# Get the seller reviews

seller_reviews = tree.xpath('//div[@id="averageCustomerReviews"]/span/a/text()')

# Get the seller price

seller_price = tree.xpath('//div[@id="olp_feature_div"]/div/span/span/span/text()')



# Export the Results

with open('amazon.csv', 'w', encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(['Title', 'Price', 'Rating', 'Reviews', 'Availability', 'Description', 'Image', 'Features', 'Details', 'Seller', 'Seller Rating', 'Seller Reviews', 'Seller Price',])
    writer.writerow([title, price, rating, reviews, availability, description, image, features, details, seller, seller_rating, seller_reviews, seller_price])

# Print the Results

print('Title: ', title)
print('Price: ', price)
print('Rating: ', rating)
print('Reviews: ', reviews)


