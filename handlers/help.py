from loader import dp
from aiogram.types import Message


@dp.message_handler(commands=['help'])
async def mes_help(message: Message):
    await message.answer(f'Правила игры:\n Игра продолжается пока не закончатся конфеты, '
                         f'кто заберёт последние выигрывает.\n'
                         f'брать можно от 1 до 28 по умолчаню начинаем со 150\n '
                         f'/candis - через пробел число для смены изночального колличества\n'
                         f'/start - запуск игры ')
