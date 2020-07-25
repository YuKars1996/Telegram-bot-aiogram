import requests
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram import Bot, types
from aiogram.utils import executor
from aiogram.dispatcher import Dispatcher
from aiogram.types import ParseMode
import pandas as pd
from config import TOKEN
import time

bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())
dp.middleware.setup(LoggingMiddleware())
number_of_pages = 1
photo_hello = 'https://r5.readrate.com/img/pictures/basic/663/663768/6637687/w585h345-crop-stretch-129fbc2a.jpg'
photo_python = 'https://media.proglib.io/wp-uploads/2018/09/ciwlCWa.png'
photo_php = 'https://5bucks.ru/wp-content/uploads/2016/12/bd2_6f5_636_330-1-original.jpg'
photo_java = 'https://techrocks.ru/wp-content/uploads/2018/08/code-java.jpg'
photo_c = 'https://media.proglib.io/wp-uploads/2018/03/maxresdefault.jpg'
photo_js = 'https://media.proglib.io/wp-uploads/2019/01/e25418821200a0f7c8f9f81b22d21691.jpg'


@dp.message_handler(commands=['materials'])
async def process_hello_command(message: types.Message):
    markup = types.InlineKeyboardMarkup()
    btn_articles = types.InlineKeyboardButton(text='текст на кнопке',
                                              url='ссылка'')
    btn_base = types.InlineKeyboardButton(text='текст на кнопке', url='ссылка'')
    btn_base_kar = types.InlineKeyboardButton(text='текст на кнопке', url='ссылка')
    markup.add(btn_articles)
    markup.add(btn_base_kar)
    markup.add(btn_base)
    await bot.send_photo(message.chat.id, photo_hello, "Надеюсь, ты найдешь здесь что-то полезное для себя.",
                         reply_markup=markup)
    await bot.delete_message(message.chat.id, message.message_id)
    time.sleep(10)
    await bot.delete_message(message.chat.id, message.message_id+1)


@dp.message_handler(content_types=["new_chat_members"]) #при добавлении участника в чат
async def new_chat_members(message: types.Message):
    await bot.send_message(message.chat.id, "ваш приветственный текст", reply_to_message_id=message.message_id,
                                      reply_markup=markup, parse_mode=ParseMode.MARKDOWN)
    time.sleep(15)
    await bot.delete_message(message.chat.id, message.message_id)
    await bot.delete_message(message.chat.id, message.message_id + 1)

@dp.message_handler(content_types=["left_chat_member"]) #при уходе участника из чата
async def left_chat_member(message):
    await bot.send_message(message.chat.id, "Кто-то ушел из чата... эээх..")
    time.sleep(10)
    await bot.delete_message(message.chat.id, message.message_id)
    await bot.delete_message(message.chat.id, message.message_id + 1)

@dp.message_handler(commands=['vacancies_python'])
async def vacancies_python (message: types.Message):
    job_title = ["'Python'"]
    for job in job_title:
        data = []
        vacancy_map = []
        di = []
        for i in range(number_of_pages):
            url = 'https://api.hh.ru/vacancies'
            par = {'text': job, 'area': '113', 'schedule': 'remote', 'per_page': '10', 'page': i}
            r = requests.get(url, params=par)
            e = r.json()
            data.append(e)
            vacancy_details = data[0]['items'][0].keys()
            df = pd.DataFrame(columns=list(vacancy_details))
            ind = 0
            for i in range(len(data)):
                for j in range(len(data[i]['items'])):
                    df.loc[ind] = data[i]['items'][j]
                    ind += 1
        vacancy_map.append(data)
        for t in vacancy_map:
            for k in t:
                for a in k['items']:
                    di.append(a['name'] +': ' + a['alternate_url'])
            caption = '10 последних вакансий удаленной работы на hh.ru:\n\n{}\n\n{}\n\n{}\n\n{}\n\n{}\n\n{}' \
                      '\n\n{}\n\n{}\n\n{}\n\n{}'.format(*di)
            await bot.send_photo(message.chat.id, photo_python, caption)
            await bot.delete_message(message.chat.id, message.message_id)

@dp.message_handler(commands=['vacancies_php'])
async def vacancies_php (message: types.Message):
    job_title = ["'PHP'"]
    for job in job_title:
        data = []
        vacancy_map = []
        di = []
        for i in range(number_of_pages):
            url = 'https://api.hh.ru/vacancies'
            par = {'text': job, 'area': '113', 'schedule': 'remote', 'per_page': '10', 'page': i}
            r = requests.get(url, params=par)
            e = r.json()
            data.append(e)
            vacancy_details = data[0]['items'][0].keys()
            df = pd.DataFrame(columns=list(vacancy_details))
            ind = 0
            for i in range(len(data)):
                for j in range(len(data[i]['items'])):
                    df.loc[ind] = data[i]['items'][j]
                    ind += 1
        vacancy_map.append(data)
        for t in vacancy_map:
            for k in t:
                for a in k['items']:
                    di.append(a['name'] +': ' + a['alternate_url'])
            caption = '10 последних вакансий удаленной работы на hh.ru:\n\n{}\n\n{}\n\n{}\n\n{}\n\n{}\n\n{}' \
                      '\n\n{}\n\n{}\n\n{}\n\n{}'.format(*di)
            await bot.send_photo(message.chat.id, photo_php, caption)
            await bot.delete_message(message.chat.id, message.message_id)

@dp.message_handler(commands=['vacancies_java'])
async def vacancies_java (message: types.Message):
    job_title = ["'Java'"]
    for job in job_title:
        data = []
        vacancy_map = []
        di = []
        for i in range(number_of_pages):
            url = 'https://api.hh.ru/vacancies'
            par = {'text': job, 'area': '113', 'schedule': 'remote', 'per_page': '10', 'page': i}
            r = requests.get(url, params=par)
            e = r.json()
            data.append(e)
            vacancy_details = data[0]['items'][0].keys()
            df = pd.DataFrame(columns=list(vacancy_details))
            ind = 0
            for i in range(len(data)):
                for j in range(len(data[i]['items'])):
                    df.loc[ind] = data[i]['items'][j]
                    ind += 1
        vacancy_map.append(data)
        for t in vacancy_map:
            for k in t:
                for a in k['items']:
                    di.append(a['name'] +': ' + a['alternate_url'])
            caption = '10 последних вакансий удаленной работы на hh.ru:\n\n{}\n\n{}\n\n{}\n\n{}\n\n{}\n\n{}' \
                      '\n\n{}\n\n{}\n\n{}\n\n{}'.format(*di)
            await bot.send_photo(message.chat.id, photo_java, caption)
            await bot.delete_message(message.chat.id, message.message_id)

@dp.message_handler(commands=['vacancies_c'])
async def vacancies_c (message: types.Message):
    job_title = ["'C#'"]
    for job in job_title:
        data = []
        vacancy_map = []
        di = []
        for i in range(number_of_pages):
            url = 'https://api.hh.ru/vacancies'
            par = {'text': job, 'area': '113', 'schedule': 'remote', 'per_page': '10', 'page': i}
            r = requests.get(url, params=par)
            e = r.json()
            data.append(e)
            vacancy_details = data[0]['items'][0].keys()
            df = pd.DataFrame(columns=list(vacancy_details))
            ind = 0
            for i in range(len(data)):
                for j in range(len(data[i]['items'])):
                    df.loc[ind] = data[i]['items'][j]
                    ind += 1
        vacancy_map.append(data)
        for t in vacancy_map:
            for k in t:
                for a in k['items']:
                    di.append(a['name'] +': ' + a['alternate_url'])
            caption = '10 последних вакансий удаленной работы на hh.ru:\n\n{}\n\n{}\n\n{}\n\n{}\n\n{}\n\n{}' \
                      '\n\n{}\n\n{}\n\n{}\n\n{}'.format(*di)
            await bot.send_photo(message.chat.id, photo_c, caption)
            await bot.delete_message(message.chat.id, message.message_id)

@dp.message_handler(commands=['vacancies_js'])
async def vacancies_js(message: types.Message):
    job_title = ["'JavaScript'"]
    for job in job_title:
        data = []
        vacancy_map = []
        di = []
        for i in range(number_of_pages):
            url = 'https://api.hh.ru/vacancies'
            par = {'text': job, 'area': '113', 'schedule': 'remote', 'per_page': '10', 'page': i}
            r = requests.get(url, params=par)
            e = r.json()
            data.append(e)
            vacancy_details = data[0]['items'][0].keys()
            df = pd.DataFrame(columns=list(vacancy_details))
            ind = 0
            for i in range(len(data)):
                for j in range(len(data[i]['items'])):
                    df.loc[ind] = data[i]['items'][j]
                    ind += 1
        vacancy_map.append(data)
        for t in vacancy_map:
            for k in t:
                for a in k['items']:
                    di.append(a['name'] +': ' + a['alternate_url'])
            caption = '10 последних вакансий удаленной работы на hh.ru:\n\n{}\n\n{}\n\n{}\n\n{}\n\n{}\n\n{}' \
                      '\n\n{}\n\n{}\n\n{}\n\n{}'.format(*di)
            await bot.send_photo(message.chat.id, photo_js, caption)
            await bot.delete_message(message.chat.id, message.message_id)

@dp.message_handler(commands=['help'])
async def helper(message: types.Message):
    await bot.send_message(message.chat.id,'Вот какие команды я знаю:\n\n'
                                           'materials - Полезные материалы\n'
                                            'vacancies_php - Вакансии удаленной работы PHP на hh.ru\n'
                                            'vacancies_python - Вакансии удаленной работы Python на hh.ru\n'
                                            'vacancies_js - Вакансии удаленной работы JavaScript на hh.ru\n'
                                            'vacancies_java - Вакансии удаленной работы Java на hh.ru\n'
                                            'vacancies_c- Вакансии удаленной работы C# на hh.ru')
    time.sleep(10)
    await bot.delete_message(message.chat.id, message.message_id)
    await bot.delete_message(message.chat.id, message.message_id + 1)

@dp.message_handler(text=['правила чата'])
async def chat_rules(message: types.Message):
    await bot.send_message(message.chat.id,'ваши правила чата')
    time.sleep(5)
    await bot.delete_message(message.chat.id, message.message_id)
    await bot.delete_message(message.chat.id, message.message_id + 1)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)