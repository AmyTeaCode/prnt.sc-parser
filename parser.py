from bs4 import BeautifulSoup
import requests
import random
print('Задонатить автору - https://www.donationalerts.com/r/amytea')



HEADERS = {'User-Agent': 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.12; rv:85.1) Gecko/20100101 Firefox/85.1', 'accept':'*/*'}
ch = 'abcdefghijklnopqrstuvwxyz1234567890'  

v = int(input('Введите количество повторений! Если вы хотите, чтобы парсер работал до завершения работы, то введите ноль! (ВНИМАНИЕ! ЕСЛИ У ВАС ВМЕСТО 1000 ИЗОБРАЖЕНИЙ БУДЕТ 500, \n ТО ЭТО ЗНАЧИТ, ЧТО НЕКОТОРЫЕ ИЗОБРАЖЕНИЯ НЕ БЫЛИ НАЙДЕНЫ! ССЫЛКИ НА НИХ ГЕНЕРИРУЮТСЯ РАНДОМНО!) \n Enter the number of repetitions! If you want the parser to run before it finishes, enter zero! (ATTENTION! IF YOU HAVE 500 IMAGES INSTEAD OF 1000 IMAGES, \n THIS MEANS THAT SOME IMAGES WERE NOT FOUND! \n LINKS ARE GENERATED REMARKLY TO THEM!) '))
if v > 0:
    for a in range (0, v):
        dl = int(3)
        number= int(1)
        for n in range(number):
            gen =''
            name = ''
            for i in range(dl):
                gen +=random.choice(ch)
                name += random.choice(ch)
        URL = f'https://prnt.sc/{name}{gen}'


        print(URL)


        def get_html(url, params=None):
            r = requests.get(url, headers = HEADERS, params = params )
            return r
        photo = []

        def get_content(html):
            try:

                soup = BeautifulSoup(html, 'html.parser')
    
                articles = soup.find_all('div', class_='image-container image__pic js-image-pic')
                for a in articles:
                    photo.append(a.find('img')['src'])
            except:
                pass
        def parse():
            html = get_html(URL)
            get_content (html.text)
        parse()


        print(f'Парсинг изображения {photo[0]}')
        try:
            url = photo[0]

            img = requests.get(url)

            img_option = open(name + '.jpg', 'wb')
            img_option.write(img.content)
            img_option.close()
        except:
            pass
    

if v == 0:

    while True:
        dl = int(3)
        number= int(1)
        for n in range(number):
            gen =''
            name = ''
            for i in range(dl):
                gen +=random.choice(ch)
                name += random.choice(ch)
        URL = f'https://prnt.sc/{name}{gen}'


        print(URL)


        def get_html(url, params=None):
            r = requests.get(url, headers = HEADERS, params = params )
            return r
        photo = []

        def get_content(html):
            try:

                soup = BeautifulSoup(html, 'html.parser')
    
                articles = soup.find_all('div', class_='image-container image__pic js-image-pic')
                for a in articles:
                    photo.append(a.find('img')['src'])
            except:
                pass
        def parse():
            html = get_html(URL)
            get_content (html.text)
        parse()


        print(f'Парсинг изображения {photo[0]}')
        try:
            url = photo[0]

            img = requests.get(url)

            img_option = open(name + '.jpg', 'wb')
            img_option.write(img.content)
            img_option.close()
        except:
            pass
if v <0:
    print('err. Отрицательное число.')

