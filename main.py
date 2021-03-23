import discord
import os
from dotenv import load_dotenv
import requests
import json
import numbergame
import random

load_dotenv()

client = discord.Client()

sad_words = ['mean', 'depressed', 'unhappy', 'angry', 'miserable', 'depressing']

starter_encouragements = [
    'Cheer up!',
    'Hang in there.',
    'You are a great person!',
    'You can do it!'
]
# inspirational quote from zenquotes.com
def get_quote():
    response = requests.get('https://zenquotes.io/api/random')
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + ' -' + json_data[0]['a']
    return quote

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    # do not reply to a bot
    if message.author == client.user:
        return
    
    msg = message.content

    if message.content.startswith('!inspire'):
        quote = get_quote()
        await message.channel.send(quote)

    #if message.content.startswith('!hello'):
    #    await message.channel.send('Hello!')

    #if message.content.startswith('!numbergame'):
    #    randomNumberGenerator(args)

    if any(word in msg for word in sad_words):
        await message.channel.send(random.choice(starter_encouragements))











# login the bot
client.run(os.getenv('TOKEN'))
