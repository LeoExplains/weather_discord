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

        if message.content.startswith('!today'):
          
          await message.reply('Enter a location:')
          input = await self.wait_for('message')
          result = get_lat_lon(input.content)
          await message.channel.send("Please wait while I look up locations matching that")
          for i, j in enumerate(result):
            option = f"{i + 1}: {j}"
            await message.channel.send(option)

          await message.channel.send("Select a location number:")  
          input = await self.wait_for('message')
          # would like to consolidate this below into a cleaner construct
          
          if int(input.content) == 1:
            await message.channel.send(result[0])
            user_location = result[0]
          elif int(input.content) == 2:
            await message.channel.send(result[1])
            user_location = result[1]
          elif int(input.content) == 3:
            await message.channel.send(result[1])
            user_location = result[2]
          elif int(input.content) == 4:
            await message.channel.send(result[1])
            user_location = result[3]
          elif int(input.content) == 5:
            await message.channel.send(result[1])
            user_location = result[4]
          elif int(input.content) == 6:
            await message.channel.send(result[1])
            user_location = result[5]
          elif int(input.content) == 7:
            await message.channel.send(result[1])
            user_location = result[6]
          elif int(input.content) == 8:
            await message.channel.send(result[1])
            user_location = result[7]
          elif int(input.content) == 9:
            await message.channel.send(result[1])
            user_location = result[8]
          elif int(input.content) == 10:
            await message.channel.send(result[1])
            user_location = result[9]
          else: 
            await message.channel.send(type(input.content))
            await message.channel.send(input.content)
              
            
          # still need to display all location options and confirm with user.
          set_user_location(user_location)
          await message.channel.send(short_chat(today))

        if message.content.startswith('!tomorrow'):
          await message.reply('Enter a location:')
          try:
            input = await self.wait_for('message')
            symbols = "!@#$%^&*()_-+={}[]"
            if input.content in symbols:
              await message.channel.send ("Sorry there was a symbol in your request, please try again. ")
            else:
              result = get_lat_lon(input.content)
              await message.channel.send("Please wait while I look up locations matching that")
              for i, j in enumerate(result):
                option = f"{i + 1}: {j}"
                await message.channel.send(option)
  
              await message.channel.send("Select a location number:")  
              input = await self.wait_for('message')
          except:
            print("Sorry there was an issue with that location, please try again")
          # would like to consolidate this below into a cleaner construct

          try:
            if int(input.content) == 1:
              await message.channel.send(result[0])
              user_location = result[0]
            elif int(input.content) == 2:
              await message.channel.send(result[1])
              user_location = result[1]
            elif int(input.content) == 3:
              await message.channel.send(result[1])
              user_location = result[2]
            elif int(input.content) == 4:
              await message.channel.send(result[1])
              user_location = result[3]
            elif int(input.content) == 5:
              await message.channel.send(result[1])
              user_location = result[4]
            elif int(input.content) == 6:
              await message.channel.send(result[1])
              user_location = result[5]
            elif int(input.content) == 7:
              await message.channel.send(result[1])
              user_location = result[6]
            elif int(input.content) == 8:
              await message.channel.send(result[1])
              user_location = result[7]
            elif int(input.content) == 9:
              await message.channel.send(result[1])
              user_location = result[8]
            elif int(input.content) == 10:
              await message.channel.send(result[1])
              user_location = result[9]
            else: 
              await message.channel.send(type(input.content))
              await message.channel.send(input.content)
          except:
            print ('There was an issue with selecting a location, please try again')
            return -1
            
          # still need to display all location options and confirm with user.
          try:
            if set_user_location(user_location) == -1:
              print ('There was an issue getting the location, please try again')
            else: 
              set_user_location(user_location)
              await message.channel.send(short_chat(tomorrow))
          except:
            print("Sorry there was an issue with setting location, please try again")
            return -1
          


intents = discord.Intents(messages=True)


client = MyClient(intents=intents)
token = os.environ.get("DISCORD_BOT_SECRET")
client.run(token)