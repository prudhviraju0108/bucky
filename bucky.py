#!/usr/bin/python

import sys
import time
import telepot
from telepot.loop import MessageLoop

TOKEN = '774488044:AAG1jKOg9KI2mrk0HblZP9sZVL90uoKHDVU'

bot = telepot.Bot(TOKEN)
who = bot.getMe()
bot_name = who['first_name']

def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(content_type, chat_type, chat_id)
    print msg

    if content_type == 'text':
	if msg['text'] == 'Hi Bucky':
		bot.sendMessage(chat_id,'Hi kp')
	if msg['text'] == 'who are you?':
		bot.sendMessage(chat_id,'Hey bud this is ' + bot_name)
#TOKEN = sys.argv[1]  # get token from command-line

bot = telepot.Bot(TOKEN)
MessageLoop(bot, handle).run_as_thread()
print ('Listening ...')

# Keep the program running.
while 1:
    time.sleep(10)
