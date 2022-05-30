import csv

from bs4 import BeautifulSoup
import requests
from csv import writer

url = "https://www.pararius.com/apartments/amsterdam?ac=1"
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')
lists = soup.find_all('section', class_="listing-search-item")

with open('housing.csv', 'w', newline='') as f:
    the_writer = writer(f)
    header = ['Title', 'Location', 'Price']
    the_writer.writerow(header)

    for list in lists:
        title = list.find('a', class_="listing-search-item__link--title").text
        location = list.find('div', class_="listing-search-item__location").text
        price = list.find('div', class_="listing-search-item__price").text


        info = [title, location, price]
        the_writer.writerow(info)
with open('housing.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)