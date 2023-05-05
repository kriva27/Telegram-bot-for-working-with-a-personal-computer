import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton


main_keyboards = InlineKeyboardMarkup()
main_keyboards.row_width = 2
main_keyboards.add(InlineKeyboardButton("🖼 Скрин", callback_data="screen"))
main_keyboards.add(InlineKeyboardButton("🕹 Выключить", callback_data="off"))
main_keyboards.add(InlineKeyboardButton("♻️ Интернет", callback_data="info"))
main_keyboards.add(InlineKeyboardButton("🖥 Железо", callback_data="zelezo"))
confirm = InlineKeyboardMarkup(row_width=2)
confirm.add(InlineKeyboardButton("✅ Подтвердить", callback_data='yes'))
confirm.add(InlineKeyboardButton("❌ Отменить", callback_data='back'))


close_message = InlineKeyboardMarkup(row_width=2)
close_message.add(InlineKeyboardButton("🌀 Проверить ", callback_data='again'))
close_message.add(InlineKeyboardButton("❌ Отменить", callback_data='back'))

back = InlineKeyboardMarkup()
back.add(InlineKeyboardButton("🔙 Назад", callback_data='back_2'))
