texts = {
	'ru':{
	#Старт меню
		'start_message':
			'''
👋🏻 Привет
• Вы можете отправить файл боту или переслать его с другого канала, и он проверит файл на VirusTotal с помощью более 70 различных антивирусов.

• Для получения результатов сканирования, отправьте мне любой файл размером до 490 МБ, и вы получите подробный его анализ.

• С помощью бота вы можете осуществлять анализ подозрительных файлов на предмет выявления вредоносных программ.

• Вы также можете добавить меня в свои чаты, и я смогу анализировать файлы, которые отправляют участники.
• По поводу рекламы и предложений обращайтесь: @lolkof
			''',
		'bt_invite_bot':'🧷 Добавить бота в свой чат',
		'bt_change_lang':'🇷🇺 Язык',
		'bt_profile':'📚 Профиль',
	#Меню изменения языка
		'text_change_lang':'📚 Выберите ваш язык:',
		'cant_find':'💁🏼‍♂ Извините, но в этом сообщение мы не обнаружили файлы 🗂',
		'size_limit':'❌ Мы нашли файл в этом сообщении, но он превышает лимит по весу в 490МБ',
		'start_processing':'''
✅Начинаю обработку файла {file_name}
Вес файла {file_size}МБ
🔃Загрузка на сервер бота...''',
		'upload_virus_total':'\n🔃Загрузка на сервер VirusTotal...',
		'wait_virus_total':'\n⏳Ожидание проверки со стороны VirusTotal...',
		'timeout_virus_total':'\nПревышено время ожидания',
		'url_to_virus_total':'<a href="https://www.virustotal.com/gui/file/{sha}">Ссылка на VirusTotal</a>',
		'detect':'\n🕷Вирусов: {detect}/{cnt}\n{text}',
		#профиль
		'back':'🔙 Назад',
		'profile':'''
🔑 Идентификатор: {id}

Запросов: {requests}
Запросы:
{requests_files}
''',
		'none':'🕵️Не найдено'
	},
	'ua':{
	#Старт меню
		'start_message':
			'''
👋🏻 Привіт
• Ви можете відправити файл боту або переслати його з іншого каналу, і він перевірить файл на наявність вірусів, використовуючи більше 70 різних антивірусів.

• Щоб отримати результати сканування, надішліть мені будь-який файл розміром до 490 МБ, і ви отримаєте його детальний аналіз.

• За допомогою бота ви можете аналізувати підозрілі файли на предмет виявлення шкідливих програм.

• Ви також можете додати мене до своїх чатів, і я зможу аналізувати файли, які надсилають учасники.
• З приводу реклами та пропозицій звертайтесь: @lolkof
			''',
		'bt_invite_bot':'🧷 запросіть бота в свій чат',
		'bt_change_lang':'🇺🇦 мова',
		'bt_profile':'📚 Профіль',
	#Меню изменения языка
		'text_change_lang':'📚 виберіть свою мову:',
		'cant_find':"🕵️ Вибачте, але ми не знайшли жодних файлів у цьому повідомленні 🗂",
		'size_limit':'❌ Ми знайшли файл у цьому повідомленні, але він перевищує обмеження ваги в 490 МБ',
		'start_processing':'''
✅ Запуск обробки файлу {file_name}
Вага файлу {file_size}МБ
🔃 Завантаження на сервер бота...''',
		'upload_virus_total':'\n🔃Завантаження на сервер VirusTotal...',
		'wait_virus_total':'\n⏳Очікування перевірки за допомогою VirusTotal...',
		'timeout_virus_total':'\nПеревищено час очікування',
		'url_to_virus_total':'<a href="https://www.virustotal.com/gui/file/{sha}">URL-адреса для VirusTotal</a>',
		'detect':'\n🕷вірусів: {detect}/{cnt}\n{text}',
		'back':'🔙 назад',
		'profile':'''
🔑 id: {id}

Кількість запитів: {requests}
запит:
{requests_files}
''',
		'none':'🕵️Не знайдено'
	},
	'en':{
	#Старт меню
		'start_message':
			'''
👋🏻 Hi
• You can send the file to the bot or forward it from another channel, and it will check the file for VirusTotal using more than 70 different antiviruses.

• To get the scan results, send me any file up to 490 MB in size, and you will receive a detailed analysis of it.

• With the help of a bot, you can analyze suspicious files for malware detection.

• You can also add me to your chats, and I will be able to analyze the files that the participants send.
• For advertisements and offers contact: @lolkof
			''',
		'bt_invite_bot':'🧷 invite bot in your chat',
		'bt_change_lang':'🇺🇸 language',
		'bt_profile':'📚 Profile',
	#Меню изменения языка
		'text_change_lang':'📚 choose your language:',
		'cant_find':"🕵️ Sorry, but we didn't find any files in this message 🗂",
		'size_limit':'❌ We found the file in this message, but it exceeds the weight limit of 490MB',
		'start_processing':'''
✅Starting processing the file {file_name}
File weight {file_size}MB
🔃Uploading to the bot server...''',
		'upload_virus_total':'\n🔃Uploading to the VirusTotal server...',
		'wait_virus_total':'\n⏳Waiting for verification by VirusTotal...',
		'timeout_virus_total':'\nWaiting time exceeded',
		'url_to_virus_total':'<a href="https://www.virustotal.com/gui/file/{sha}">URL to VirusTotal</a>',
		'detect':'\n🕷Viruses: {detect}/{cnt}\n{text}',
		'back':'🔙 back',
		'profile':'''
🔑 id: {id}

Requests count: {requests}
requests:
{requests_files}
''',
		'none':'🕵️Not found'
	},
	'de':{
	#Старт меню
		'start_message':
			'''
👋🏻 Hi
• Sie können die Datei an den Bot senden oder von einem anderen Kanal weiterleiten, und er überprüft die Datei mit mehr als 70 verschiedenen Antivirenprogrammen auf VirusTotal.

• Um die Scanergebnisse zu erhalten, senden Sie mir eine Datei mit einer Größe von bis zu 490 MB, und Sie erhalten eine detaillierte Analyse davon.

• Mit Hilfe eines Bots können Sie verdächtige Dateien auf Malware-Erkennung analysieren.

• Sie können mich auch zu Ihren Chats hinzufügen, und ich kann die Dateien analysieren, die die Teilnehmer senden.
• Kontakt für Anzeigen und Angebote: @lolkof
			''',
		'bt_invite_bot':'🧷 laden Sie Bot in Ihren Chat ein',
		'bt_change_lang':'🇩🇪 sprachlich',
		'bt_profile':'📚 Profil',
	#Меню изменения языка
		'text_change_lang':'📚 wählen Sie Ihre Sprache:',
		'cant_find':"🕵️ Entschuldigung, aber wir haben in dieser Nachricht keine Dateien gefunden 🗂",
		'size_limit':'❌ Wir haben die Datei in dieser Nachricht gefunden, aber sie überschreitet das Gewichtslimit von 490 MB',
		'start_processing':'''
✅ Starten der Verarbeitung der Datei {file_name}
Dateigewicht {file_size} MB
🔃 Hochladen auf den Bot-Server...''',
		'upload_virus_total':'\n🔃Hochladen auf den VirusTotal-Server...',
		'wait_virus_total':'\n⏳Warten auf Überprüfung durch VirusTotal...',
		'timeout_virus_total':'\nWartezeit überschritten',
		'url_to_virus_total':'<a href="https://www.virustotal.com/gui/file/{sha}">URL zu VirusTotal</a>',
		'detect':'\n🕷Computerviren: {detect}/{cnt}\n{text}',
		'back':'🔙 zurück',
		'profile':'''
🔑 id: {id}

Anzahl der Anfragen: {requests}
Antr:
{requests_files}
''',
		'none':'🕵️Nicht gefunden'
	},
}