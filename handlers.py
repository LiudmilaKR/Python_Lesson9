from create import dp
from aiogram import types
from aiogram.dispatcher.filters import Text
from random import randint


@dp.message_handler(commands=['start'])
async def mes_start(message: types.Message):
    await message.reply(f'Привет, {message.from_user.first_name}!\nМы будем \
играть в конфеты!\nЕсли ты согласна - напиши /agree')


@dp.message_handler(commands=['agree'])
async def mes_help(message: types.Message):
    await message.reply('Отлично! Тогда - начнём...')
    await message.answer('Введи /set X, где X - общее число конфет.')


@dp.message_handler(commands=['set'])
async def mes_settings(message: types.Message):
    global total
    total = message.text.split()[1]
    await message.answer(f'Итак, общее количество конфет {total} штук!')
    await message.answer('Делай ход! Ты можешь взять не более 28 конфет!')


@dp.message_handler()
async def mes_count(message: types.Message):
    global total
    total = int(total)
    num_hum = int(message.text)
    if num_hum > 28:
        await message.answer('Ты можешь взять не более 28 конфет! Ход переходит к боту!')
    else:
        total -= num_hum
        await message.answer(f'На столе осталось {total} конфет!')
    if total > 28:
        await message.answer('Игра продолжается!\nТеперь мой ход!')
        num_bot = int(randint(1, 28))
        await message.answer(f'Я беру {str(num_bot)} конфет!')
        total -= num_bot
        await message.answer(f'На столе осталось {total} конфет!')
        if total > 28:
            await message.answer('Игра продолжается!\nТвой ход!')
        else:
            num_hum = total
            total = 0
            await message.answer('Ты победила!')
    else:
        num_bot = total
        total = 0
        await message.answer('Бот-победитель!')


@dp.message_handler()
async def mes_all(message: types.Message):
    await message.reply(f'{message.from_user.full_name}, смотри, что я поймал - {message.text}!')
    print(message)
