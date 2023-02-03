from loader import dp
from aiogram.types import Message
import game



@dp.message_handler(commands=['candis'])
async def mes_candis(message: Message):

    for duel in game.total:
        if message.from_user.id == duel[0]:
            if len(message.text.split()) == 2 and message.text.split()[1].isdigit():
                # print('принял')
                candis = int(message.text.split()[1])
                game.total.remove(duel)
                print(duel)
                my_game = [message.from_user.id, message.from_user.first_name, candis]
                game.total.append(my_game)
                await message.answer(f'конфет стало {candis}')
            else:
                await message.answer('Указать колличество конфет нужно цифрами после пробела')
