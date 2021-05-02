import constants as keys
from telegram.ext import *
import telebot
from telethon import TelegramClient
import tqdm
import os
import responses as R

bot = telebot.TeleBot(keys.API_KEY)
chat_id = bot.get_chat

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")

# @bot.message_handler(func=lambda message: True)
# def echo_all(message):
# 	bot.reply_to(message, message.text)

@bot.message_handler(commands=['location'])
def location(message):
    bot.send_location(chat_id, lat, lon)
# @bot.message_handler(func=lambda message: message.document.mime_type == 'text/plain', content_types=['document'])
# def handle_text_doc(message):
	
@bot.message_handler(commands=['quiz'])
def quiz(message):
    bot.reply_to(message, "Feature yet to come.")

bot.polling()
print("Bot started...")
