STATUS = ["Dm brelee2222 to invite me onto your server", "https://discord.gg/QzU45Tuvyz", "made by brelee2222", "go to brelee2222's server for bot updates", 'discord.gg/QzU45Tuvyz']
lettersa = ('a', 'A', '4', '@') 
lettersb = ('b', 'B', '3', '8')
lettersc = ('c', 'C', '(', '¢')
lettersd = ('d', 'D')
letterse = ('e', 'E') 
lettersf = ('f', 'F') 
lettersg = ('g', 'G', '9') 
lettersh = ('h', 'H')
lettersi = ('i', 'I', '1', '|', '!')
lettersj = ('j', 'J')
lettersk = ('k', 'K')
lettersl = ('l', 'L', '/')
lettersm = ('m', 'M')
lettersn = ('n', 'N') 
letterso = ('o', 'O', '0', '*', '()')
lettersp = ('p', 'P')
lettersq = ('q', 'Q') 
lettersr = ('r', 'R') 
letterss = ('s', 'S', '5', '$', '&', 'Ś')
letterst = ('t', 'T', '+')
lettersu = ('u', 'U', 'ü', 'ū')
lettersv = ('v', 'V') 
lettersw = ('w', 'W') 
lettersx = ('x', 'X') 
lettersy = ('y', 'Y', '7')
lettersz = ('z', 'Z', '2')
guildids = [772905819448672256]
pointers = [0]

badwords = ('fuck', 'shit','bitch','thot','niger', 'dick', 'faggot', 'cum', 'cunt', 'simp', 'penis', 'fock', 'bastard', 'shiet', 'fuhck', 'cock', 'balls', 'ballz', 'peniz', 'peenis', 'peeniz', 'pussy', 'pussee', 'crap', 'kunt', 'cunt', 'sex', 'fcuk', 'puusy', 'pusy', 'poosy', 'cuunt', 'bicht')



    


from collections import namedtuple

import discord.abc

import random
import asyncio
from keep_alive import keep_alive
import discord
import os
import rich_prescence
import time
import discord.ext
from discord.utils import get
from discord.ext import commands, tasks
from discord.ext.commands import has_permissions,  CheckFailure, check
class Profile(namedtuple('Profile', 'flags user mutual_guilds connected_accounts premium_since')):
    __slots__ = ()
    
class MyClient(discord.Client):
   
    
    
    
    async def on_ready(self):
        
        await client.change_presence(activity=discord.Game(name=random.choice(STATUS)))
        print('Connected!')
        print('Username: {0.name}\nID: {0.id}'.format(self.user))
        
    async def on_message(self, message):
        if message.content == 'tell me about this bot':
          
          embed=discord.Embed(title="BOT NAME", description='censor bot', color=0x00ff00)
          embed.add_field(name='creator', value="Brelee2222", inline=False)
          embed.add_field(name='servers', value=len(client.guilds), inline=False)
          embed.add_field(name='bot updates server', value=('https://discord.gg/QzU45Tuvyz'), inline=False)
          
          await message.channel.send(embed=embed)
          return
          

        
        if message.content == 'ping':
          msg = await message.channel.send("Timing My Ping System...")
          await asyncio.sleep(3)
          await msg.edit(content = f"My ping delay is **{round(client.latency * 1000)}ms**")
        if not message.guild.id in guildids:
          print(message.content, ':author: ', message.author)
        if message.content == 'servers' and message.author.id == 479792413884547072:
          
          try:
            print(pointers)
            await message.author.send(pointers)
          except:
            print('hello')
          
          embed=discord.Embed(title='servers', description='severs the bot is in', color=0x00ff00)

          for guild in client.guilds:
            
            embed.add_field(name=f"{guild.name}", value=f"{guild.member_count}", inline=False)
            try:
              user = await client.fetch_user(f"{guild.owner_id}")
              embed.add_field(name=user, value=f"{guild.owner_id}", inline=False)
              embed.add_field(name='id:'
              , value=f"{guild.id}", inline=False)

              
            
          
              
              
              
              
              
              
            except:
              print('hello')
          await message.author.send(embed=embed)
            
            
            
            
                    
        for i in lettersa:
          message.content = message.content.replace(i, 'a')
          
        for i in lettersb:
          message.content = message.content.replace(i, 'b')
          
        for i in lettersc:
          message.content = message.content.replace(i, 'c')
          
        for i in lettersd:
          message.content = message.content.replace(i, 'd')
          
        for i in letterse:
          message.content = message.content.replace(i, 'e')
          
        for i in lettersf:
          message.content = message.content.replace(i, 'f')
          
        for i in lettersg:
          message.content = message.content.replace(i, 'g')
          
        for i in lettersh:
          message.content = message.content.replace(i, 'h')
          
        for i in lettersi:
          message.content = message.content.replace(i, 'i')
          
        for i in lettersj:
          message.content = message.content.replace(i, 'j')
          
        for i in lettersk:
          message.content = message.content.replace(i, 'k')
          
        for i in lettersl:
          message.content = message.content.replace(i, 'l')
          
        for i in lettersm:
          message.content = message.content.replace(i, 'm')
          
        for i in lettersn:
          message.content = message.content.replace(i, 'n')
          
        for i in letterso:
          message.content = message.content.replace(i, 'o')
          
        for i in lettersp:
          message.content = message.content.replace(i, 'p')
          
        for i in lettersq:
          message.content = message.content.replace(i, 'q')
          
        for i in lettersr:
          message.content = message.content.replace(i, 'r')
          
        for i in letterss:
          message.content = message.content.replace(i, 's')
          
        for i in letterst:
          message.content = message.content.replace(i, 't')
          
        for i in lettersu:
          message.content = message.content.replace(i, 'u')
          
        for i in lettersw:
          message.content = message.content.replace(i, 'w')
          
        for i in lettersx:
          message.content = message.content.replace(i, 'x')
          
        for i in lettersy:
          message.content = message.content.replace(i, 'y')  
        for i in lettersz:
          
          message.content = message.content.replace(i, 'z')
        
        message.content = message.content.replace('.', '')
        if not message.guild.id in guildids:
          print(message.content)

        
        for words in badwords:

            
            

              if words in message.content and message.author.id != 806619458184806450: 
                  print('censored')
                  
                  pointers[0] +=1
                  pointers.append(message.author.name + '#' + message.author.discriminator)
                  pointers.append(message.content)
                  try:
                    msg = message
                    await msg.delete()
                    fmt = 'the message of {0.author} has been deleted due to inappropriate use of content'
                    await message.channel.send(fmt.format(message), delete_after=6.0)
                    await message.channel.send('https://cdn.discordapp.com/emojis/806577679829958737.png?v=1')
                    pointers.append('+')
                  except:
                    pointers.append('-')
keep_alive()  

client = MyClient()
client.run(os.getenv("TOKEN"))  