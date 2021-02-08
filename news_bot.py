import requests
from bs4 import BeautifulSoup
import telebot
from telebot import types
from decouple import config



bot = telebot.TeleBot(config('TOKEN'))

# Код Парсера

url = 'https://kaktus.media/'

def get_html(url):
    res = requests.get(url).text
    return res


def get_titles(html):
    soup = BeautifulSoup(html, 'html.parser')
    table = soup.find('div', class_ = 'lenta_block').find_all('span', class_ = 'n')
    titles = []
    for i in table:
        try:
            title = i.text
            titles.append(title)
        except:
            title = 'no title'
    return titles[:20]


def get_links(html):
    soup = BeautifulSoup(html, 'html.parser')
    table = soup.find('div', class_ = 'lenta_block').find_all('div', class_ = 'f_medium')
    links = []
    for i in table:
        link = i.find('a').get('href')
        links.append(link)
    return links


def get_page_data(html):
    soup = BeautifulSoup(html, 'html.parser')
    description = soup.find('div', class_ = 'topic').find_all('p')
    txts = []
    for i in description:
        txt = i.text
        txts.append(txt)
    text_ = ' '.join(txts)
    return text_


def get_page_img(html):
    soup = BeautifulSoup(html, 'html.parser')
    try:
        img = soup.find('div', id = 'topic').find_all('img')
        return img[1].get('src')
    except:
        img = ''


def titles():
    return get_titles(get_html(url))


# Код Бота

titles = titles()
link = get_links(get_html(url))

keybord = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2, one_time_keyboard=True)
btn1 = types.KeyboardButton('Главное Меню')
btn2 = types.KeyboardButton('Выйти')
keybord.add(btn1, btn2)

nokeybord = types.InlineKeyboardMarkup(row_width=6)
btn1 = types.InlineKeyboardButton('1', callback_data='1')
btn2 = types.InlineKeyboardButton('2', callback_data='2')
btn3 = types.InlineKeyboardButton('3', callback_data='3')
btn4 = types.InlineKeyboardButton('4', callback_data='4')
btn5 = types.InlineKeyboardButton('5', callback_data='5')
btn6 = types.InlineKeyboardButton('->', callback_data='next1')
nokeybord.add(btn1, btn2, btn3, btn4, btn5, btn6)


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, f'{message.chat.first_name}')
    bot.send_message(message.chat.id, 'Здраствуйте', reply_markup=keybord)
    bot.send_message(message.chat.id, f'''Новости за сегодня:\n
1){titles[0]}\n\n2){titles[1]}\n\n3){titles[2]}\n
4){titles[3]}\n\n5){titles[4]}\n\nВыберите новость по номеру''', reply_markup=nokeybord)


@bot.callback_query_handler(func=lambda c: True)
def inline(c):

    chat_id = c.message.chat.id


    # Страница 1
    if c.data == "1":
        nokeybord = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('Описание', callback_data='data1')
        btn2 = types.InlineKeyboardButton('Фото', callback_data='img1')
        nokeybord.add(btn1, btn2)
        bot.send_message(chat_id, f'{titles[0]}\n\nВы можете просмотреть статью или фото', reply_markup=nokeybord)
    if c.data == "2":
        nokeybord = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('Описание', callback_data='data2')
        btn2 = types.InlineKeyboardButton('Фото', callback_data='img2')
        nokeybord.add(btn1, btn2)
        bot.send_message(chat_id, f'{titles[1]}\n\nВы можете просмотреть статью или фото', reply_markup=nokeybord)
    if c.data == "3":
        nokeybord = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('Описание', callback_data='data3')
        btn2 = types.InlineKeyboardButton('Фото', callback_data='img3')
        nokeybord.add(btn1, btn2)
        bot.send_message(chat_id, f'{titles[2]}\n\nВы можете просмотреть статью или фото', reply_markup=nokeybord)
    if c.data == "4":
        nokeybord = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('Описание', callback_data='data4')
        btn2 = types.InlineKeyboardButton('Фото', callback_data='img4')
        nokeybord.add(btn1, btn2)
        bot.send_message(chat_id, f'{titles[3]}\n\nВы можете просмотреть статью или фото', reply_markup=nokeybord)
    if c.data == "5":
        nokeybord = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('Описание', callback_data='data5')
        btn2 = types.InlineKeyboardButton('Фото', callback_data='img5')
        nokeybord.add(btn1, btn2)
        bot.send_message(chat_id, f'{titles[4]}\n\nВы можете просмотреть статью или фото', reply_markup=nokeybord)
    if c.data == "next1":
        nokeybord = types.InlineKeyboardMarkup(row_width=7)
        btn = types.InlineKeyboardButton('<-', callback_data='back1')
        btn1 = types.InlineKeyboardButton('6', callback_data='6')
        btn2 = types.InlineKeyboardButton('7', callback_data='7')
        btn3 = types.InlineKeyboardButton('8', callback_data='8')
        btn4 = types.InlineKeyboardButton('9', callback_data='9')
        btn5 = types.InlineKeyboardButton('10', callback_data='10')
        btn6 = types.InlineKeyboardButton('->', callback_data='next2')
        nokeybord.add(btn, btn1, btn2, btn3, btn4, btn5, btn6)
        bot.edit_message_text(f'''Новости на сегодня:\n
6){titles[5]}\n\n7){titles[6]}\n\n8){titles[6]}\n
9){titles[8]}\n\n10){titles[9]}\n\nВыберите новость по номеру''', chat_id, c.message.message_id, reply_markup= nokeybord)


    # Страница 2
    if c.data == "back1":
        nokeybord = types.InlineKeyboardMarkup(row_width=6)
        btn1 = types.InlineKeyboardButton('1', callback_data='1')
        btn2 = types.InlineKeyboardButton('2', callback_data='2')
        btn3 = types.InlineKeyboardButton('3', callback_data='3')
        btn4 = types.InlineKeyboardButton('4', callback_data='4')
        btn5 = types.InlineKeyboardButton('5', callback_data='5')
        btn6 = types.InlineKeyboardButton('->', callback_data='next1')
        nokeybord.add(btn1, btn2, btn3, btn4, btn5, btn6)
        bot.edit_message_text(f'''Новости на сегодня:\n
1){titles[0]}\n\n2){titles[1]}\n\n3){titles[2]}\n
4){titles[3]}\n\n5){titles[4]}\n\nВыберите новость по номеру''', chat_id, c.message.message_id, reply_markup= nokeybord)

    if c.data == "6":
        nokeybord = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('Описание', callback_data='data6')
        btn2 = types.InlineKeyboardButton('Фото', callback_data='img6')
        nokeybord.add(btn1, btn2)
        bot.send_message(chat_id, f'{titles[5]}\n\nВы можете просмотреть статью или фото', reply_markup=nokeybord)
    if c.data == "7":
        nokeybord = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('Описание', callback_data='data7')
        btn2 = types.InlineKeyboardButton('Фото', callback_data='img7')
        nokeybord.add(btn1, btn2)
        bot.send_message(chat_id, f'{titles[6]}\n\nВы можете просмотреть статью или фото', reply_markup=nokeybord)
    if c.data == "8":
        nokeybord = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('Описание', callback_data='data8')
        btn2 = types.InlineKeyboardButton('Фото', callback_data='img8')
        nokeybord.add(btn1, btn2)
        bot.send_message(chat_id, f'{titles[7]}\n\nВы можете просмотреть статью или фото', reply_markup=nokeybord)
    if c.data == "9":
        nokeybord = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('Описание', callback_data='data9')
        btn2 = types.InlineKeyboardButton('Фото', callback_data='img9')
        nokeybord.add(btn1, btn2)
        bot.send_message(chat_id, f'{titles[8]}\n\nВы можете просмотреть статью или фото', reply_markup=nokeybord)
    if c.data == "10":
        nokeybord = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('Описание', callback_data='data10')
        btn2 = types.InlineKeyboardButton('Фото', callback_data='img10')
        nokeybord.add(btn1, btn2)
        bot.send_message(chat_id, f'{titles[9]}\n\nВы можете просмотреть статью или фото', reply_markup=nokeybord)
    if c.data == "next2":
        nokeybord = types.InlineKeyboardMarkup(row_width=7)
        btn = types.InlineKeyboardButton('<-', callback_data='back2')
        btn1 = types.InlineKeyboardButton('11', callback_data='11')
        btn2 = types.InlineKeyboardButton('12', callback_data='12')
        btn3 = types.InlineKeyboardButton('13', callback_data='13')
        btn4 = types.InlineKeyboardButton('14', callback_data='14')
        btn5 = types.InlineKeyboardButton('15', callback_data='15')
        btn6 = types.InlineKeyboardButton('->', callback_data='next3')
        nokeybord.add(btn, btn1, btn2, btn3, btn4, btn5, btn6)
        bot.edit_message_text(f'''Новости на сегодня:\n
11){titles[10]}\n\n12){titles[11]}\n\n13){titles[12]}\n
14){titles[13]}\n\n15){titles[14]}\n\nВыберите новость по номеру''', chat_id, c.message.message_id, reply_markup= nokeybord)


    # Страница 3
    if c.data == "back2":
        nokeybord = types.InlineKeyboardMarkup(row_width=7)
        btn = types.InlineKeyboardButton('<-', callback_data='back1')
        btn1 = types.InlineKeyboardButton('6', callback_data='6')
        btn2 = types.InlineKeyboardButton('7', callback_data='7')
        btn3 = types.InlineKeyboardButton('8', callback_data='8')
        btn4 = types.InlineKeyboardButton('9', callback_data='9')
        btn5 = types.InlineKeyboardButton('10', callback_data='10')
        btn6 = types.InlineKeyboardButton('->', callback_data='next2')
        nokeybord.add(btn, btn1, btn2, btn3, btn4, btn5, btn6)
        bot.edit_message_text(f'''Новости на сегодня:\n
6){titles[5]}\n\n7){titles[6]}\n\n3){titles[7]}\n
4){titles[8]}\n\n5){titles[9]}\n\nВыберите новость по номеру''', chat_id, c.message.message_id, reply_markup= nokeybord)

    if c.data == "11":
        nokeybord = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('Описание', callback_data='data11')
        btn2 = types.InlineKeyboardButton('Фото', callback_data='omg')
        nokeybord.add(btn1, btn2)
        bot.send_message(chat_id, f'{titles[10]}\n\nВы можете просмотреть статью или фото', reply_markup=nokeybord)
    if c.data == "12":
        nokeybord = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('Описание', callback_data='data12')
        btn2 = types.InlineKeyboardButton('Фото', callback_data='omg')
        nokeybord.add(btn1, btn2)
        bot.send_message(chat_id, f'{titles[11]}\n\nВы можете просмотреть статью или фото', reply_markup=nokeybord)
    if c.data == "13":
        nokeybord = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('Описание', callback_data='data13')
        btn2 = types.InlineKeyboardButton('Фото', callback_data='omg')
        nokeybord.add(btn1, btn2)
        bot.send_message(chat_id, f'{titles[12]}\n\nВы можете просмотреть статью или фото', reply_markup=nokeybord)
    if c.data == "14":
        nokeybord = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('Описание', callback_data='data14')
        btn2 = types.InlineKeyboardButton('Фото', callback_data='omg')
        nokeybord.add(btn1, btn2)
        bot.send_message(chat_id, f'{titles[13]}\n\nВы можете просмотреть статью или фото', reply_markup=nokeybord)
    if c.data == "15":
        nokeybord = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('Описание', callback_data='data15')
        btn2 = types.InlineKeyboardButton('Фото', callback_data='omg')
        nokeybord.add(btn1, btn2)
        bot.send_message(chat_id, f'{titles[14]}\n\nВы можете просмотреть статью или фото', reply_markup=nokeybord)
    if c.data == "next3":
        nokeybord = types.InlineKeyboardMarkup(row_width=6)
        btn = types.InlineKeyboardButton('<-', callback_data='back3')
        btn1 = types.InlineKeyboardButton('16', callback_data='16')
        btn2 = types.InlineKeyboardButton('17', callback_data='17')
        btn3 = types.InlineKeyboardButton('18', callback_data='18')
        btn4 = types.InlineKeyboardButton('19', callback_data='19')
        btn5 = types.InlineKeyboardButton('20', callback_data='20')
        nokeybord.add(btn, btn1, btn2, btn3, btn4, btn5)
        bot.edit_message_text(f'''Новости на сегодня:\n
16){titles[15]}\n\n17){titles[16]}\n\n18){titles[17]}\n
19){titles[18]}\n\n20){titles[19]}\n\nВыберите новость по номеру''', chat_id, c.message.message_id, reply_markup= nokeybord)


    # Страница 4
    if c.data == "back3":
        chat = c.message.chat.id
        nokeybord = types.InlineKeyboardMarkup(row_width=7)
        btn = types.InlineKeyboardButton('<-', callback_data='back2')
        btn1 = types.InlineKeyboardButton('11', callback_data='11')
        btn2 = types.InlineKeyboardButton('12', callback_data='12')
        btn3 = types.InlineKeyboardButton('13', callback_data='13')
        btn4 = types.InlineKeyboardButton('14', callback_data='14')
        btn5 = types.InlineKeyboardButton('15', callback_data='15')
        btn6 = types.InlineKeyboardButton('->', callback_data='next3')
        nokeybord.add(btn, btn1, btn2, btn3, btn4, btn5, btn6)
        bot.edit_message_text(f'''Новости на сегодня:\n
11){titles[10]}\n\n12){titles[11]}\n\n13){titles[12]}\n
14){titles[13]}\n\n15){titles[14]}\n\nВыберите новость по номеру''', chat_id, c.message.message_id, reply_markup= nokeybord)

    if c.data == "16":
        nokeybord = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('Описание', callback_data='data16')
        btn2 = types.InlineKeyboardButton('Фото', callback_data='img16')
        nokeybord.add(btn1, btn2)
        bot.send_message(chat_id, f'{titles[15]}\n\nВы можете просмотреть статью или фото', reply_markup=nokeybord)
    if c.data == "17":
        nokeybord = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('Описание', callback_data='data17')
        btn2 = types.InlineKeyboardButton('Фото', callback_data='img17')
        nokeybord.add(btn1, btn2)
        bot.send_message(chat_id, f'{titles[16]}\n\nВы можете просмотреть статью или фото', reply_markup=nokeybord)
    if c.data == "18":
        nokeybord = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('Описание', callback_data='data18')
        btn2 = types.InlineKeyboardButton('Фото', callback_data='img18')
        nokeybord.add(btn1, btn2)
        bot.send_message(chat_id, f'{titles[17]}\n\nВы можете просмотреть статью или фото', reply_markup=nokeybord)
    if c.data == "19":
        nokeybord = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('Описание', callback_data='data19')
        btn2 = types.InlineKeyboardButton('Фото', callback_data='img19')
        nokeybord.add(btn1, btn2)
        bot.send_message(chat_id, f'{titles[18]}\n\nВы можете просмотреть статью или фото', reply_markup=nokeybord)
    if c.data == "20":
        nokeybord = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('Описание', callback_data='data20')
        btn2 = types.InlineKeyboardButton('Фото', callback_data='img20')
        nokeybord.add(btn1, btn2)
        bot.send_message(chat_id, f'{titles[19]}\n\nВы можете просмотреть статью или фото', reply_markup=nokeybord)


    # Внутренняя Страница  1
    if c.data == 'data1':
        data_ = get_page_data(get_html(link[0]))
        bot.send_message(chat_id, f'{data_[:1000]}')
    if c.data == 'img1':
        try:
            data_ = get_page_img(get_html(link[0]))
            bot.send_photo(chat_id, data_)
        except:
            bot.send_message(chat_id, 'Фотографий к сожалению нет')
        

    if c.data == 'data2':
        data_ = get_page_data(get_html(link[1]))
        bot.send_message(chat_id, f'{data_[:1000]}')
    if c.data == 'img2':
        try:
            data_ = get_page_img(get_html(link[1]))
            bot.send_photo(chat_id, data_)
        except:
            bot.send_message(chat_id, 'Фотографий к сожалению нет')

    if c.data == 'data3':
        data_ = get_page_data(get_html(link[2]))
        bot.send_message(chat_id, f'{data_[:1000]}')
    if c.data == 'img3':
        try:
            data_ = get_page_img(get_html(link[2]))
            bot.send_photo(chat_id, data_)
        except:
            bot.send_message(chat_id, 'Фотографий к сожалению нет')

    if c.data == 'data4':
        data_ = get_page_data(get_html(link[3]))
        bot.send_message(chat_id, f'{data_[:1000]}')
    if c.data == 'img4':
        try:
            data_ = get_page_img(get_html(link[3]))
            bot.send_photo(chat_id, data_)
        except:
            bot.send_message(chat_id, 'Фотографий к сожалению нет')

    if c.data == 'data5':
        data_ = get_page_data(get_html(link[4]))
        bot.send_message(chat_id, f'{data_[:1000]}')
    if c.data == 'img5':
        try:
            data_ = get_page_img(get_html(link[4]))
            bot.send_photo(chat_id, data_)
        except:
            bot.send_message(chat_id, 'Фотографий к сожалению нет')

    # Внутренняя Страница  2

    if c.data == 'data6':
        data_ = get_page_data(get_html(link[5]))
        bot.send_message(chat_id, f'{data_[:1000]}')
    if c.data == 'img6':
        try:
            data_ = get_page_img(get_html(link[5]))
            bot.send_photo(chat_id, data_)
        except:
            bot.send_message(chat_id, 'Фотографий к сожалению нет')
        

    if c.data == 'data7':
        data_ = get_page_data(get_html(link[6]))
        bot.send_message(chat_id, f'{data_[:1000]}')
    if c.data == 'img7':
        try:
            data_ = get_page_img(get_html(link[6]))
            bot.send_photo(chat_id, data_)
        except:
            bot.send_message(chat_id, 'Фотографий к сожалению нет')

    if c.data == 'data8':
        data_ = get_page_data(get_html(link[7]))
        bot.send_message(chat_id, f'{data_[:1000]}')
    if c.data == 'img8':
        try:
            data_ = get_page_img(get_html(link[7]))
            bot.send_photo(chat_id, data_)
        except:
            bot.send_message(chat_id, 'Фотографий к сожалению нет')

    if c.data == 'data9':
        data_ = get_page_data(get_html(link[8]))
        bot.send_message(chat_id, f'{data_[:1000]}')
    if c.data == 'img9':
        try:
            data_ = get_page_img(get_html(link[8]))
            bot.send_photo(chat_id, data_)
        except:
            bot.send_message(chat_id, 'Фотографий к сожалению нет')

    if c.data == 'data10':
        data_ = get_page_data(get_html(link[9]))
        bot.send_message(chat_id, f'{data_[:1000]}')
    if c.data == 'img10':
        try:
            data_ = get_page_img(get_html(link[9]))
            bot.send_photo(chat_id, data_)
        except:
            bot.send_message(chat_id, 'Фотографий к сожалению нет')

    # Внутренняя Страница 3

    if c.data == 'data11':
        data_ = get_page_data(get_html(link[10]))
        bot.send_message(chat_id, f'{data_[:1000]}')
    if c.data == 'img11':
        try:
            data_ = get_page_img(get_html(link[10]))
            bot.send_photo(chat_id, data_)
        except:
            bot.send_message(chat_id, 'Фотографий к сожалению нет')
        

    if c.data == 'data12':
        data_ = get_page_data(get_html(link[11]))
        bot.send_message(chat_id, f'{data_[:1000]}')
    if c.data == 'img12':
        try:
            data_ = get_page_img(get_html(link[11]))
            bot.send_photo(chat_id, data_)
        except:
            bot.send_message(chat_id, 'Фотографий к сожалению нет')

    if c.data == 'data13':
        data_ = get_page_data(get_html(link[12]))
        bot.send_message(chat_id, f'{data_[:1000]}')
    if c.data == 'img13':
        try:
            data_ = get_page_img(get_html(link[12]))
            bot.send_photo(chat_id, data_)
        except:
            bot.send_message(chat_id, 'Фотографий к сожалению нет')

    if c.data == 'data14':
        data_ = get_page_data(get_html(link[13]))
        bot.send_message(chat_id, f'{data_[:1000]}')
    if c.data == 'img14':
        try:
            data_ = get_page_img(get_html(link[13]))
            bot.send_photo(chat_id, data_)
        except:
            bot.send_message(chat_id, 'Фотографий к сожалению нет')

    if c.data == 'data15':
        data_ = get_page_data(get_html(link[14]))
        bot.send_message(chat_id, f'{data_[:1000]}')
    if c.data == 'img15':
        try:
            data_ = get_page_img(get_html(link[14]))
            bot.send_photo(chat_id, data_)
        except:
            bot.send_message(chat_id, 'Фотографий к сожалению нет')

    # Внутренняя Страница 4

    if c.data == 'data16':
        data_ = get_page_data(get_html(link[15]))
        bot.send_message(chat_id, f'{data_[:1000]}')
    if c.data == 'img16':
        try:
            data_ = get_page_img(get_html(link[15]))
            bot.send_photo(chat_id, data_)
        except:
            bot.send_message(chat_id, 'Фотографий к сожалению нет')
        

    if c.data == 'data17':
        data_ = get_page_data(get_html(link[16]))
        bot.send_message(chat_id, f'{data_[:1000]}')
    if c.data == 'img17':
        try:
            data_ = get_page_img(get_html(link[16]))
            bot.send_photo(chat_id, data_)
        except:
            bot.send_message(chat_id, 'Фотографий к сожалению нет')

    if c.data == 'data18':
        data_ = get_page_data(get_html(link[17]))
        bot.send_message(chat_id, f'{data_[:1000]}')
    if c.data == 'img18':
        try:
            data_ = get_page_img(get_html(link[17]))
            bot.send_photo(chat_id, data_)
        except:
            bot.send_message(chat_id, 'Фотографий к сожалению нет')

    if c.data == 'data19':
        data_ = get_page_data(get_html(link[18]))
        bot.send_message(chat_id, f'{data_[:1000]}')
    if c.data == 'img19':
        try:
            data_ = get_page_img(get_html(link[18]))
            bot.send_photo(chat_id, data_)
        except:
            bot.send_message(chat_id, 'Фотографий к сожалению нет')

    if c.data == 'data20':
        data_ = get_page_data(get_html(link[19]))
        bot.send_message(chat_id, f'{data_[:1000]}')
    if c.data == 'img20':
        try:
            data_ = get_page_img(get_html(link[19]))
            bot.send_photo(chat_id, data_)
        except:
            bot.send_message(chat_id, 'Фотографий к сожалению нет')


@bot.message_handler(content_types=['text'])
def send_text(message):
    chat_id = message.chat.id
    if message.text.title() == 'Выйти':
        bot.send_message(chat_id, 'Пока')
    if message.text == 'Главное Меню':
        bot.send_message(message.chat.id, f'''Новости на сегодня:\n
1){titles[0]}\n\n2){titles[1]}\n\n3){titles[2]}\n
4){titles[3]}\n\n5){titles[4]}\n\nВыберите новость по номеру''', reply_markup=nokeybord)



bot.polling()