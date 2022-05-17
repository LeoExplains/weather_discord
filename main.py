from chat import *
from check import *

import asyncio
import os
#Discord weather bot

import discord

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')
        print('------')
        
    async def on_message(self, message):
        # we do not want the bot to reply to itself
        if message.author.id == self.user.id:
            return
    
        if message.content.startswith('!weather'):
          await message.channel.send(intro())

        if message.content.startswith('!location'):
          await message.reply('Set a location:')
          input = await self.wait_for('message')
          result = get_lat_lon(input.content)
          await message.channel.send("select a location number")
          for i, j in enumerate(result):
            option = f"{i + 1}: {j}"
            #await message.channel.send("Is this the location? (y/n)")
            await message.channel.send(option)
            
          input = await self.wait_for('message')
          if int(input.content) == 1:
              await message.channel.send(result[0])
          else: 
            await message.channel.send(type(input.content))
            await message.channel.send(input.content)
              
            def is_choice(m):
              return m.author == message.author and m.content.isdigit()

            # try:
            #       input = await self.wait_for('message', check=is_choice, timeout=15.0)
            # except asyncio.TimeoutError: # fix this to be defined
            #       return await message.channel.send(f'Sorry, you took too long, defaulting to Melbourne Vic AU.')
            
            
            # still need to display all location options and confirm with user.
          # await message.channel.send(set_user_location(get_lat_lon(input.content)))
          # await message.channel.send(short_chat(today))


intents = discord.Intents(messages=True)


client = MyClient(intents=intents)
token = os.environ.get("DISCORD_BOT_SECRET")
client.run(token)

# ####################
# print(get_lat_lon("melbourne"))
# result = get_lat_lon("melbourne")
# def on_message():
#   for i, j in enumerate(result):
#     print(i + 1, j)
#     choice = input("is this the location? (y/n) ")
#     if choice == 'y':
#       return j

# if message.content == 'ping':
#             await message.channel.send('pong')

# print(on_message())
#     choice = input(f"""is this the right location? (y/n): """)
#     if choice.lower() == "y":
#       return(coord)
#     else:
#       continue
#   return(-1)