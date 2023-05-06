# Coded by Kriva


from inline_keyboards import main_keyboards, confirm, close_message, back
import speedtest
import os
import tempfile
import time
from PIL import ImageGrab
from config import TOKEN
import telebot
import requests
import platform
import psutil
import socket





bot = telebot.TeleBot(TOKEN)



""""Проверка интернет соединения и вычисление скорости"""
def check_ineternet_connection(call):

    con = requests.get('https://www.google.com')

    if con.status_code == 200:
        sticker = bot.send_sticker(call.message.chat.id,
                                   sticker='CAACAgEAAxkBAAEI3QRkVOP3WcGZvr2VYnGlenSsEtfZ9wACLQIAAqcjIUQ9QDDJ7YO0ti8E')
        mes = bot.send_message(call.message.chat.id, '<b>Подлючаюсь к сети пк...</b>', parse_mode='HTML',
                               reply_markup=back)
        time.sleep(3)
        mes_2 = bot.send_message(call.message.chat.id, '<b> Вычисляю скорость интернета...</b>',
                                           parse_mode='HTML', reply_markup=back)
        time.sleep(3)
        hostname = socket.gethostname()
        ip_address = socket.gethostbyname(hostname)
        servers = []
        threads = None
        s = speedtest.Speedtest()
        s.get_servers(servers)
        s.download(threads=threads)
        results_dict = s.results.dict()
        download_speed = round(results_dict["download"] / 1000000, 2)
        bot.delete_message(call.message.chat.id, sticker.message_id)
        bot.delete_message(call.message.chat.id, mes.message_id)
        bot.delete_message(call.message.chat.id, mes_2.message_id)

        bot.send_message(call.message.chat.id, '<b><i>✅ Подключение к интернету присутствует.</i></b>\n<b><i>⚡️ Скорость интернета: </i></b>'+(str(download_speed))+' Мб'+'\n<b><i>📌Ip-Адрес: </i></b>'+(str(ip_address)), parse_mode='HTML', reply_markup=back)
    else:
        bot.send_message(call.message.chat.id, '<b><i>❌ Подключение к интернету отсутствует</i></b>', reply_markup=back, parse_mode='HTML')




"""Сборка информации о пк"""
def computer(call):
    system = (str(platform.system()))
    processor = (str(platform.processor()))
    architecture = (str(platform.architecture()))
    memory = psutil.virtual_memory().total
    memory_gb = round(memory / 1024 ** 3, 2)
    bot.send_message(call.message.chat.id, '<b><i>🖥 Информация о ПК.\n\n⚙️ Операционная система: </i></b>'+ (str(system))+ '<b><i>\n🎛 Процессор: </i></b>'+ (str(processor))+ '\n<b><i>📦 Объем ОП: </i></b>'+(str(memory_gb))+'ГБ\n<b><i>💻 Архитектура: </i></b>'+(str(architecture)), parse_mode='HTML',
                     reply_markup=back)



"""Функция ответа на команду старт"""
@bot.message_handler(commands=['start'])
def start_handler(message):
    bot.send_message(message.chat.id, '<b>🏠 Главное меню.</b>', reply_markup=main_keyboards, parse_mode='HTML')




"""Ответы на инлайн кнопки"""
@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "off":
        bot.send_message(call.message.chat.id, '<i><b>❗️ Вы точно хотите выключить пк?</b></i>', reply_markup=confirm, parse_mode='HTML')
        bot.delete_message(call.message.chat.id, call.message.message_id)
    elif call.data == 'yes':
        bot.send_message(call.message.chat.id, '⏳ Выключаю пк..')
        bot.delete_message(call.message.chat.id, call.message.message_id)
        bot.send_message(call.message.chat.id, '<i><b>❗ ️Персональный компьютер выключен. \nПосле этого сообщения бот не сможет вам ответить</b></i>', parse_mode='HTML')
        os.system('shutdown -s')
    elif call.data == 'screen':
        bot.delete_message(call.message.chat.id, call.message.message_id)
        path = tempfile.gettempdir() + 'screenshot.png'
        screenshot = ImageGrab.grab()
        screenshot.save(path, 'PNG')
        bot.send_photo(call.message.chat.id, open(path, 'rb'), caption='<b>Скриншот экрана.</b>', parse_mode='HTML', reply_markup=back)
    elif call.data == 'info':
        bot.delete_message(call.message.chat.id, call.message.message_id)
        check_ineternet_connection(call)
    elif call.data == 'back':
        bot.delete_message(call.message.chat.id, call.message.message_id)
        bot.send_message(call.message.chat.id, '<b>🏠 Главное меню.</b>', reply_markup=main_keyboards, parse_mode='HTML')
    elif call.data == 'again':
        bot.delete_message(call.message.chat.id, call.message.message_id)
        check_ineternet_connection(call)
    elif call.data == 'zelezo':
        computer(call)
    elif call.data == 'back_2':
        bot.delete_message(call.message.chat.id, call.message.message_id)
        bot.send_message(call.message.chat.id, '<b>🏠 Главное меню.</b>', reply_markup=main_keyboards, parse_mode='HTML')





bot.polling(none_stop=True)

