from bs4 import BeautifulSoup
import requests

def save():
    with open('ebay_verizon_phones.txt', 'a') as file:
        file.write("\n")
        file.write(comp["title"])
        file.write("    ")
        file.write(comp["price"])
        file.write("    ")
        file.write(comp["link"])


def parse():
    url = 'https://www.ebay.com/b/Verizon-Cell-Phones-Smartphones/9355/bn_7117700158'
    HEADERS = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.72 Safari/537.36'}
    response = requests.get(url, headers = HEADERS)
    soup = BeautifulSoup(response.content, 'html.parser')
    items = soup.findAll('div', class_ = 's-item__wrapper clearfix')
    comps = []
    for item in items:
        comps.append({
            'title': item.find('a', class_ = 's-item__link').get_text(strip = True),
            'price': item.find('span',class_ = 's-item__price').get_text(strip = True),
            'link': item.find('a', class_ = 's-item__link').get('href')
        })

        global comp
        for comp in comps:
            print(comp["title"],"   ", comp["price"],"   ", comp["link"])
            save()

parse()
# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
