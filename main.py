import telebot
import buttons
from database import Data

bot = telebot.TeleBot('Token')



@bot.message_handler(commands=['start'])
def admin_message(message):
    user_id = message.from_user.id

    text = 'Добро пожаловать \n Здесь вы можете хронить свои накопительные карточки'

    bot.send_message(user_id, text, reply_markup=buttons.menu_button())

    bot.register_next_step_handler(message, add_card)
@bot.message_handler(content_types=['text'])
def add_card(message):
    user_id = message.from_user.id
    if message.text == 'Добавить карту':
        text = 'Напишите название накопительной'
        bot.send_message(user_id, text, reply_markup=buttons.back_button())
        bot.register_next_step_handler(message, get_name)
    elif message.text == 'Мои карты':
        text = 'Выберите карту'
        bot.send_message(user_id, text, reply_markup=buttons.prod_button())
        bot.register_next_step_handler(message, about_prod)

def get_name(message):
    user_id = message.from_user.id
    if message.text == 'Назад':
        bot.register_next_step_handler(message, admin_message)
    else:
        card_name = message.text
        bot.send_message(user_id, 'Отправьте фото для продукта', reply_markup=buttons.back_button())
        bot.register_next_step_handler(message, get_photo, card_name)


def get_photo(message, card_name):
    db = Data()
    if message.photo:
        photo_id = message.photo[0].file_id

        db.add_product(card_name, photo_id)

        bot.send_message(message.from_user.id, 'Карта добавлена', reply_markup=buttons.menu_button())
    else:
        bot.register_next_step_handler(message, admin_message)

def about_prod(message):
    user_id = message.from_user.id
    if message.text in Data().show_all_products():
        about_product = Data().get_current_product(message.text)
        bot.send_message(user_id, f'{about_product[0]}', reply_markup=None)
        bot.send_photo(user_id, f'{about_product[1]}', reply_markup=None)
        bot.register_next_step_handler(message, about_prod)

    if message.text == 'Назад':
        bot.register_next_step_handler(message, admin_message)














bot.polling()