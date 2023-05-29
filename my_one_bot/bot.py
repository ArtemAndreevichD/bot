import logging
import os

from aiogram import Bot, Dispatcher, executor, types

# from config import TOKEN
TOKEN = os.getenv('TOKEN')

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

transliteration_dict = {'А': 'A',
                        'Б': 'B',
                        'В': 'V',
                        'Г': 'G',
                        'Д': 'D',
                        'Е': 'E',
                        'Ё': 'E',
                        'Ж': 'ZH',
                        'З': 'Z',
                        'И': 'I',
                        'Й': 'I',
                        'К': 'K',
                        'Л': 'L',
                        'М': 'M',
                        'Н': 'N',
                        'О': 'O',
                        'П': 'P',
                        'Р': 'R',
                        'С': 'S',
                        'Т': 'T',
                        'У': 'U',
                        'Ф': 'F',
                        'Х': 'KH',
                        'Ц': 'TS',
                        'Ч': 'CH',
                        'Ш': 'SH',
                        'Щ': 'SHCH',
                        'Ы': 'Y',
                        'Ъ': 'IE',
                        'Э': 'E',
                        'Ю': 'IU',
                        'Я': 'IA',
                        '-': '-',
                        ' ': ' '}


@dp.message_handler(commands=['start'])
async def send_welkome(message: types.Message):
    user_name = message.from_user.full_name
    uset_id = message.from_user.id
    text = f"Hello, {user_name}! What name do you want to transliterate?"
    logging.info(f"{user_name=} {uset_id=} send message {message.text}")
    await message.reply(text)

@dp.message_handler()
async def send_transliteration(message: types.Message):
    user_name = message.from_user.full_name
    uset_id = message.from_user.id
    text = message.text
    text = text.upper()
    transliteration = []
    for i in text:
        if i in transliteration_dict:
            transliteration.append(transliteration_dict[i])
        elif i == ' ':
            transliteration.append(i)
    transliterated = ''.join(transliteration)
    logging.info(f"{user_name=} {uset_id=} message:{message.text}")
    await bot.send_message(uset_id, transliterated)
    await bot.send_message(uset_id, 'What name do you want to transliterate?') 
    logging.info(f'bot responded:{transliterated}')


if __name__ == "__main__":
    executor.start_polling(dp)

    

