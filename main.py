from chat import *
from check import *


import os
#Discord Interview Bot

""" A bot to have a simulated interview with me"""

import discord

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')
        print('------')

    async def on_message(self, message):
        # we do not want the bot to reply to itself
        if message.author.id == self.user.id:
            return

        if message.content.startswith('!today'):
            await message.channel.send(intro(), mention_author=True)
            await message.reply('Todays weather is:', mention_author=True)
            await message.reply(set_user_location(get_lat_lon("melbourne")))
            await message.reply(short_chat(today))


intents = discord.Intents(messages=True)


client = MyClient(intents=intents)
token = os.environ.get("DISCORD_BOT_SECRET")
client.run(token)
