import datetime
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

# Создание клиента
client = TelegramClient('session_name', api_id, api_hash)


async def send_message_TRX():
    receiver = receiver_trx
    # Использование номера телефона
    entity = await client.get_entity(receiver[0])
    await client.send_message(entity, receiver[1])

    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("[{}] Сообщение TRX отправлено".format(current_time))

async def send_message_BTC():
    receiver = receiver_btc
    # Использование номера телефона
    entity = await client.get_entity(receiver[0])
    await client.send_message(entity, receiver[1])

    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("[{}] Сообщение BTC отправлено".format(current_time))

async def send_message_BNB():
    receiver = receiver_bnb
    # Использование номера телефона
    entity = await client.get_entity(receiver[0])
    await client.send_message(entity, receiver[1])

    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("[{}] Сообщение BNB отправлено".format(current_time))


async def main():

    cprint(figlet_format('Nico \n Farm', font='starwars'),
           'green', 'on_red', attrs=['bold'])

    await client.start(phone_number)
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
