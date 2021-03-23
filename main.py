import discord
import os
from dotenv import load_dotenv
import requests
import json
import numbergame
import random
import asyncio

load_dotenv()

class MyClient(discord.Client):
    async def on_ready(self):
        print('We have logged in as {0.user}'.format(client))

    async def on_message(self, message):
        # console log
        print('Message from {0.author}: {0.content}'.format(message))

        # do not reply to a bot
        if message.author == client.user:
            return

        # random number game
        if message.content.startswith('!numbergame'):
            await message.channel.send('Guess a number between 1 and 1000')

            def is_correct(m):
                return m.author == message.author and m.content.isdigit()

            answer = random.randint(1, 1000)

            try:
                guess = await self.wait_for('message', check=is_correct, timeout=5.0)
            except asyncio.TimeoutError:
                return await message.channel.send('Sorry, you took too long to respond. The correct answer was {}'.format(answer))

            if int(guess.content) == answer:
                await message.channel.send('You are right!')
            else:
                await message.channel.send('You were wrong. The correct answer was {}'.format(answer))

        # inspiration quote generator
        sad_words = ['mean', 'depressed', 'unhappy', 'angry', 'miserable', 'depressing']

        def get_quote():
            response = requests.get('https://zenquotes.io/api/random')
            json_data = json.loads(response.text)
            quote = json_data[0]['q'] + ' -' + json_data[0]['a']
            return quote

        if message.content.startswith('!inspire'):
            quote = get_quote()
            await message.channel.send(quote)
        
# create client object
client = MyClient()
# bot login
client.run(os.getenv('TOKEN'))

