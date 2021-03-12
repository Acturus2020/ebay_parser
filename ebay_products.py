from bs4 import BeautifulSoup
import requests

def clear():
    with open('ebay_products.txt', 'w') as file:
        file.write("\n")

def save():
    with open('ebay_products.txt', 'a') as file:

        file.write(comp["title"])
        file.write("    ")
        file.write(comp["price"])
        file.write("\n")
        file.write(comp["link"])
        file.write("\n")
        file.write(specs)
        file.write("\n")
        file.write("\n")


def parse():
    url = 'https://www.ebay.com/globaldeals?_trkparms=pageci%3A78d0acc8-82f2-11eb-b4c4-82cd155e0238%7Cparentrq%3A24dfc6e41780a9b13c767ff6ffd61c42%7Ciid%3A1'
    HEADERS = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.72 Safari/537.36'}
    response = requests.get(url, headers = HEADERS)
    soup = BeautifulSoup(response.content, 'html.parser')
    items = soup.findAll('div', class_ = 'row')
    comps = []
    for item in items:
        comps.append({
            'title': item.find('span', class_ = 'ebayui-ellipsis-2').get_text(strip = True),
            'price': item.find('span',class_ = 'first').get_text(strip = True),
            'link': item.find('a', class_ = 'dne-itemtile-link').get('href')
        })


    global comp
    global href_
    for comp in comps:
        href_ = comp["link"]
        # print(comp["title"],"   ", comp["price"],"   ", comp["link"])
        parse2()
        save()


def parse2():
    url = href_
    HEADERS = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.72 Safari/537.36'}
    response = requests.get(url, headers = HEADERS)
    soup = BeautifulSoup(response.content, 'html.parser')
    items = soup.findAll('div', class_= 'prodDetailSec')
    global specs
    for item in items:
        specs = item.get_text()
        # items2 = item.findAll('tr')
        # print(items2.find('td'))
    print(specs)




clear()
parse()
