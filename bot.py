from pyrogram import Client
from pyrogram.types import ReplyKeyboardMarkup
from config import CAR_BRANDS, MOBILE_BRANDS, CURRENCY_GOLD_NAME
from car import car
from mobile import mobile
from currency_gold import currency_gold

app = Client(
    'my_bot',
    # api_id,    your api id
    # api_hash,  your api hash
    # bot_token=bot_token  your bot token
)

with app:
    def main_menu(user_id):
        app.send_message(
            user_id,
            'لطفا درخواست خود را انتخاب کنید.',
            reply_markup=ReplyKeyboardMarkup(
                [
                    ['خودرو 🚗'],
                    ['موبایل 📱'],
                    ['ارز 💵'],
                    ['سکه 💰']
                ],
                resize_keyboard=True
            )
        )


    def currency_menu(user_id):
        app.send_message(
            user_id,
            'لطفا درخواست خود را انتخاب کنید.',
            reply_markup=ReplyKeyboardMarkup(
                [
                    ['🏠'],
                    ['دلار'],
                    ['دلار کانادا'],
                    ['دلار استرالیا'],
                    ['دلار سنگاپور'],
                    ['یورو'],
                    ['روبل روسیه'],
                    ['لیر ترکیه'],
                    ['دینار عراق'],
                    ['ریال قطر'],
                ],
                resize_keyboard=True
            )
        )


    def gold_menu(user_id):
        app.send_message(
            user_id,
            'لطفا درخواست خود را انتخاب کنید.',
            reply_markup=ReplyKeyboardMarkup(
                [
                    ['🏠'],
                    ['آزادی'],
                    ['امامی'],
                    ['نیم سکه'],
                    ['ربع سکه'],
                    ['سکه گرمی']
                ],
                resize_keyboard=True
            )
        )


    def mobile_menu(user_id):
        app.send_message(
            user_id,
            'لطفا درخواست خود را انتخاب کنید.',
            reply_markup=ReplyKeyboardMarkup(
                [
                    ['🏠'],
                    ['اپل'],
                    ['سامسونگ'],
                    ['هواوی'],
                    ['شیائومی']
                ],
                resize_keyboard=True
            )
        )


    def reg_cars_menu(user_id):
        app.send_message(
            user_id,
            'لطفا نوع خودرو را انتخاب کنید.',
            reply_markup=ReplyKeyboardMarkup(
                [
                    ['🏠'],
                    ['خودروهای داخلی 🚙'],
                    ['خودروهای خارجی 🏎'],
                ],
                resize_keyboard=True
            )
        )


    def iranian_cars_menu(user_id):
        app.send_message(
            user_id,
            'لطفا برند مورد نظر رو انتخاب کنید.',
            reply_markup=ReplyKeyboardMarkup(
                [
                    ['🏠'],
                    ['pride', 'peugeot', 'tiba'],
                    ['dena', 'runna', 'quick'],
                    ['brilliance', 'saina', 'samand'],
                ],
                resize_keyboard=True
            )
        )


    def foreign_cars_menu(user_id):
        app.send_message(
            user_id,
            'لطفا برند مورد نظر رو انتخاب کنید.',
            reply_markup=ReplyKeyboardMarkup(
                [
                    ['🏠'],
                    ['mercedes-benz', 'bmw', 'swm', 'besturn'],
                    ['mvm', 'borgward', 'toyota', 'geely'],
                    ['jac', 'changan', 'chery', 'dongfeng'],
                    ['renault', 'zotye', 'rigan', 'ssang-yong'],
                    ['lexus', 'kia', 'capra', 'volkswagen'],
                    ['foton', 'citroen', 'suzuki', 'lifan'],
                    ['mazda', 'mitsubishi', 'mini', 'nissan'],
                    ['pick-up', 'haval', 'haima', 'hyundai']
                ],
                resize_keyboard=True
            )
        )


@app.on_message()
def my_handler(client, message):
    if message.text == '/start':
        main_menu(message.from_user.id)
    elif message.text == '🏠':
        main_menu(message.from_user.id)
    elif message.text == 'خودرو 🚗':
        reg_cars_menu(message.from_user.id)
    elif message.text == 'خودروهای داخلی 🚙':
        iranian_cars_menu(message.from_user.id)
    elif message.text == 'خودروهای خارجی 🏎':
        foreign_cars_menu(message.from_user.id)
    elif message.text == 'موبایل 📱':
        mobile_menu(message.from_user.id)
    elif message.text == 'ارز 💵':
        currency_menu(message.from_user.id)
    elif message.text == 'سکه 💰':
        gold_menu(message.from_user.id)
    else:

        for key, value in CAR_BRANDS.items():
            if value == message.text:
                app.send_message(
                    message.from_user.id,
                    f'<b>{"#" * 12} {message.text} {"#" * 12}</b>'
                )
                text_message = car(key)

                for text in text_message:
                    app.send_message(message.from_user.id, text)
                app.send_message(message.from_user.id, f'<b>{"#" * 30}</b>')

        for key, value in MOBILE_BRANDS.items():
            if message.text == key:
                app.send_message(
                    message.from_user.id,
                    f'<b>{"#" * 12} {message.text} {"#" * 12}</b>'
                )
                text_message = mobile(value)

                for text in text_message:
                    app.send_message(message.from_user.id, text)

                app.send_message(message.from_user.id, f'<b>{"#" * 30}</b>')

        for key, value in CURRENCY_GOLD_NAME.items():
            if message.text == key:
                text_message = currency_gold(value)
                text_message = f'{message.text}\n {text_message}'

                app.send_message(message.from_user.id, text_message)


app.run()
