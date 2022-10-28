from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.dispatcher.filters import Text
from aiogram import Bot, Dispatcher, types
from aiogram.utils.markdown import hlink
from aiogram.utils import executor
from pyrogram import Client
from texts import texts
from config import *
import requests
import asyncio
import json
import os

bot = Bot(token=TG_API_TOKEN)
dp = Dispatcher(bot)
client = Client("my_account", api_id=2040, api_hash='b18441a1ff607e10a989891a5462e627')

def get_lang(id):
	with open('langs.json') as f:
		lang = json.load(f)
	lang = lang.get(str(id))
	if lang is None:
		user_id = id
		with open('langs.json') as f:
			langs = json.load(f)
		lang = 'en'
		langs.update([(str(user_id),lang)])
		with open('langs.json', 'w') as f:
			f.write(json.dumps(langs))
	return lang


@dp.message_handler(commands='start')
async def start(message):
	user_id = message.from_user.id
	add_url_bot = InlineKeyboardButton(texts[get_lang(user_id)]['bt_invite_bot'], url='http://t.me/AntiVirusT_bot?startgroup=true')
	change_lang = InlineKeyboardButton(texts[get_lang(user_id)]['bt_change_lang'], callback_data='change_lang')
	profile = InlineKeyboardButton(texts[get_lang(user_id)]['bt_profile'], callback_data='profile')
	start_kb = InlineKeyboardMarkup().add(add_url_bot)
	start_kb.add(change_lang, profile)
	try:
		await message.message.edit_text(texts[get_lang(user_id)]['start_message'], reply_markup=start_kb)
	except:
		await bot.send_message(message.chat.id, texts[get_lang(user_id)]['start_message'], reply_markup=start_kb)


@dp.callback_query_handler(text='profile')
async def profile(call: types.CallbackQuery):
	await call.answer()
	back = InlineKeyboardButton(texts[get_lang(call.from_user.id)]['back'], callback_data='back')
	profile_kb = InlineKeyboardMarkup().add(back)
	with open('requests.json') as f:
		rq = json.load(f)
	if rq.get(str(call.from_user.id)) is None:
		count = 0
		names = []
	else:
		count = rq[str(call.from_user.id)]['count']
		names = rq[str(call.from_user.id)]['names']
	if names:
		files = ''
		for file in names:
			files+= f'{file}\n'
	else: files = texts[get_lang(call.from_user.id)]['none']
	await call.message.edit_text(texts[get_lang(call.from_user.id)]['profile'].format(requests=count,requests_files=files,id=call.from_user.id), reply_markup=profile_kb)



@dp.callback_query_handler(Text(startswith="back"))
async def back(call: types.CallbackQuery):
	await call.answer()
	await start(call)


@dp.callback_query_handler(text='change_lang')
async def change_lang(call: types.CallbackQuery):
	await call.answer()
	ru = InlineKeyboardButton('🇷🇺 Русский', callback_data='bt_lang_ru')
	ua = InlineKeyboardButton('🇺🇦 Український', callback_data='bt_lang_ua')
	us = InlineKeyboardButton('🇺🇸 English', callback_data='bt_lang_en')
	de = InlineKeyboardButton('🇩🇪 Deutsch', callback_data='bt_lang_de')
	languages = InlineKeyboardMarkup()
	languages.add(ru,ua)
	languages.add(us,de)
	await call.message.edit_text(texts[get_lang(call.from_user.id)]['text_change_lang'], reply_markup=languages)

@dp.callback_query_handler(Text(startswith="bt_lang_"))
async def change_lang_complete(call: types.CallbackQuery):
	user_id = call.from_user.id
	with open('langs.json') as f:
		lang = json.load(f)
	choice = call.data[len('bt_lang_'):]
	lang.update([(str(user_id),choice)])
	with open('langs.json', 'w') as f:
		f.write(json.dumps(lang))
	await call.answer()
	await start(call)



@dp.message_handler()
async def meshand(msg: types.Message):
	if msg.from_user.id == msg.chat.id:
		await bot.send_message(msg.from_user.id, texts[get_lang(msg.from_user.id)]['cant_find'])

@dp.message_handler(content_types=[types.ContentType.DOCUMENT])
async def filehand(msg: types.Message):
	file_size = (msg.document.file_size // 1024)//1024

	if file_size > 490:
		return await bot.send_message(msg.from_user.id, texts[get_lang(msg.from_user.id)]['size_limit'])
	message = texts[get_lang(msg.from_user.id)]['start_processing'].format(file_name=msg.document.file_name, file_size=file_size)
	mes = await bot.send_message(msg.chat.id, message)

	await client.download_media(msg.document, f"user_files/{msg.from_user.id}/{msg.document.file_name}")

	message += texts[get_lang(msg.from_user.id)]['upload_virus_total']
	await mes.edit_text(message)

	if file_size > 30:
		response = requests.get("https://www.virustotal.com/api/v3/files/upload_url", 
			headers={
				"Accept": "application/json",
				'x-apikey':f'{VSTOTAL_API_TOKEN}',
			})
		url =  response.json()['data']
	else: url = 'https://www.virustotal.com/api/v3/files'

	filepath = f"user_files/{msg.from_user.id}/{msg.document.file_name}"
	with open(filepath, "rb") as fh:
		mydata = fh.read()
		response = requests.post(url,                        
					headers={
						'Accept':'application/json',
						'x-apikey':f'{VSTOTAL_API_TOKEN}',
					},
					files={'file': mydata})
	os.remove(f"user_files/{msg.from_user.id}/{msg.document.file_name}")
	analit_id = response.json()['data']['id']

	message += texts[get_lang(msg.from_user.id)]['wait_virus_total']
	await mes.edit_text(message)

	comp = None; attempts = 0

	while comp!='completed' or attempts > 600:
		response = requests.get(f'https://www.virustotal.com/api/v3/analyses/{analit_id}', 
			headers = {
				"Accept": "application/json",
				"x-apikey": f'{VSTOTAL_API_TOKEN}',
			})
		attempts+=1
		comp = 'completed' if response.json()['data']['attributes']['status'] == 'completed' else None
		await asyncio.sleep(1)
	if attempts > 599:
		message += texts[get_lang(msg.from_user.id)]['timeout_virus_total']
		return await mes.edit_text(message)
	data = response.json()['data']['attributes']['stats']
	sha = response.json()['meta']['file_info']['sha256']
	cnt = 0
	detect = 0
	# print(response.json()['data']['attributes']['results'])
	for av, dt in response.json()['data']['attributes']['results'].items():
		cnt+=1
		if dt.get('result'):
			detect += 1


	with open('requests.json') as f:
		rq = json.load(f)
	if rq.get(str(msg.from_user.id)) is None:
		count = 0
		names = []
	else:
		count = rq[str(msg.from_user.id)]['count']
		names = rq[str(msg.from_user.id)]['names']

	count += 1
	names.append(msg.document.file_name)

	rq[str(msg.from_user.id)] = {'count':count, 'names':names}
	with open('requests.json', 'w') as f:
		f.write(json.dumps(rq))


	text = texts[get_lang(msg.from_user.id)]['url_to_virus_total'].format(sha=sha)
	message += texts[get_lang(msg.from_user.id)]['detect'].format(detect=detect, cnt=cnt, text=text)
	await mes.edit_text(message, parse_mode="HTML")
	
async def on_start(x):
	bot = await x.bot.me
	print('Bot joined to online!', bot.username)

client.start()
executor.start_polling(dp,on_startup=on_start, skip_updates = True)