from aiogram import Bot, Dispatcher

with open('token.txt', 'r') as key:
    token = key.read()

bot = Bot(token)
dp = Dispatcher(bot)