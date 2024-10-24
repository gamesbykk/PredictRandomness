# bot.py
import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
x=discord.Intents.default()
x.message_content=True
client = discord.Client(intents=x)

@client.event
async def on_message(message):
    print(message.content)
    f = open("rand.txt", "a")
    try:
        f.write('\n'+str(int(message.content.lower()[:2])))
        f.close()
        f=open("rand.txt",'r')
        l=len(f.read().split('\n'))
        channel = client.get_channel(1298716515113373739)
        await channel.send('Database length '+str(l))
    except:
        pass


client.run(TOKEN)