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

        if message.content.startswith('!s today'):
            await message.channel.send(intro(), mention_author=True)
            await message.reply('Set a location:', mention_author=True)
            def is_correct(m):
                return m.author == message.author
            try:
                input = await self.wait_for('message', check=is_correct, timeout=15.0)
            except asyncio.TimeoutError:
                return await message.channel.send(f'Sorry, you took too long, defaulting to Melbourne Vic AU.')
            # still need to display all location options and confirm with user.
            await message.channel.send(set_user_location(get_lat_lon(input.content)))
            await message.channel.send(short_chat(today))

        if message.content.startswith('!s tomorrow'):
            await message.channel.send(intro(), mention_author=True)
            await message.reply('Set a location:', mention_author=True)
            def is_correct(m):
                return m.author == message.author
            try:
                input = await self.wait_for('message', check=is_correct, timeout=15.0)
            except asyncio.TimeoutError:
                return await message.channel.send(f'Sorry, you took too long, defaulting to Melbourne Vic AU.')
            # still need to display all location options and confirm with user.
            set_user_location(get_lat_lon(input.content))
            await message.channel.send(short_chat(today))


intents = discord.Intents(messages=True)


client = MyClient(intents=intents)
token = os.environ.get("DISCORD_BOT_SECRET")
client.run(token)
