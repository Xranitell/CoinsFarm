import datetime
import random
import time
from datetime import datetime
from telethon import TelegramClient
from apscheduler.schedulers.asyncio import AsyncIOScheduler
import asyncio
from data.config import *
import sys
from colorama import init
init(strip=not sys.stdout.isatty()) # strip colors if stdout is redirected
from termcolor import cprint
from pyfiglet import figlet_format

api_id = ''
api_hash =''
phone =''
sessionname =''

# Создание клиента
print('------------------------------------')
string = input("Enter connecting string\n")
list = string.split(':')
sessionname = list[0]
api_id = list[1]
api_hash = list[2]
phone = list[3]
cl_password = list[4]
print('------------------------------------')


client = TelegramClient(sessionname, api_id, api_hash)

async def send_message_TRX():
    receiver = receiver_trx
    # Использование номера телефона
    entity = await client.get_entity(receiver[0])
    await client.send_message(entity, receiver[1])

    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    cprint("[{}] Сообщение TRX отправлено".format(current_time), 'yellow')

async def send_message_BTC():
    receiver = receiver_btc
    # Использование номера телефона
    entity = await client.get_entity(receiver[0])
    await client.send_message(entity, receiver[1])

    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    cprint("[{}] Сообщение BTC отправлено".format(current_time), 'yellow')

async def send_message_BNB():
    receiver = receiver_bnb
    # Использование номера телефона
    entity = await client.get_entity(receiver[0])
    await client.send_message(entity, receiver[1])

    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    cprint("[{}] Сообщение BNB отправлено".format(current_time), 'yellow')


async def main():
    #input api
    print(client.session)

    cprint(figlet_format('Nico \n Farm', font='starwars'),
           'yellow', 'on_black', attrs=['bold'])

    await client.start(phone, cl_password)
    cprint('Авторизация успешна', 'green')

    scheduler = AsyncIOScheduler()

    scheduler.add_job(send_message_TRX, 'interval', seconds= receiver_trx[2])
    scheduler.add_job(send_message_BNB, 'interval', seconds=receiver_bnb[2])
    scheduler.add_job(send_message_BTC, 'interval', seconds=receiver_btc[2])

    try:
        print("Клиент запущен и будет отправлять сообщения c заданным интервалом")

        scheduler.start()
        await send_message_TRX()
        await send_message_BTC()
        await send_message_BNB()
        # Нужно держать программу запущенной
        await client.run_until_disconnected()
    except (KeyboardInterrupt, SystemExit):
        pass


if __name__ == '__main__':
    asyncio.run(main())
