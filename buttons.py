from telebot import types
from database import Data

def menu_button():
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)

    # Сама кнопка
    number = types.KeyboardButton('Добавить карту')
    cards = types.KeyboardButton('Мои карты')

    # Добвить в пространство
    kb.add(number, cards)

    # Результат нужно вернуть
    return kb

def back_button():
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)

    # Сама кнопка
    back = types.KeyboardButton('Назад')

    # Добвить в пространство
    kb.add(back)

    # Результат нужно вернуть
    return kb

def prod_button():
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    back = types.KeyboardButton('Назад')
    names = Data().show_all_products()
    for i in names:
        kb.add(types.KeyboardButton(i))
    kb.add(back)
    return kb