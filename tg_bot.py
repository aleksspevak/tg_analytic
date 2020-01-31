#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import telebot
from telebot import types
import tg_analytic

token = ""
bot = telebot.TeleBot(token)

user_markup = types.ReplyKeyboardMarkup(True)
user_markup.row('команда а', 'команда б')
user_markup.row('команда в')


@bot.message_handler(commands=['start'])
def handle_text(message):
    tg_analytic.statistics(message.chat.id, message.text)
    bot.send_message(message.chat.id, " Исполнена команда старт ", reply_markup=user_markup)

@bot.message_handler(commands=['command'])
def handle_text(message):
    tg_analytic.statistics(message.chat.id, message.text)
    bot.send_message(message.chat.id, 'Использована команда')

@bot.message_handler(content_types=['text'])
def handle_text(message):
    tg_analytic.statistics(message.chat.id,message.text)
    if message.text == 'команда а':
        text = 'Использована команда а'
        bot.send_message(message.chat.id,text,reply_markup=user_markup)

    if message.text == 'команда б':
        s1 = 'Использована команда б'
        tg_analytic.statistics(message.chat.id, message.text)
        bot.send_message(message.chat.id,s1,reply_markup=user_markup)
    if message.text == 'команда в':
        s1 = 'Использована команда в'
        tg_analytic.statistics(message.chat.id, message.text)
        bot.send_message(message.chat.id,s1,reply_markup=user_markup)
    if message.text[:10] == 'статистика' or message.text[:10] == 'Cтатистика':
        st = message.text.split(' ')
        if 'txt' in st or 'тхт' in st:
            tg_analytic.analysis(st,message.chat.id)
            with open('%s.txt' %message.chat.id ,'r',encoding='UTF-8') as file:
                bot.send_document(message.chat.id,file)
            tg_analytic.remove(message.chat.id)
        else:
            messages = tg_analytic.analysis(st,message.chat.id)
            bot.send_message(message.chat.id, messages)

bot.polling(none_stop=True, interval=1)
