import discord
import requests
from datetime import datetime
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Pong')
    if message.content.startswith('$quote'):
        get = requests.get(
            'https://quote-garden.herokuapp.com/api/v3/quotes/random')
        if get.status_code == 200:
            jsonStuff = get.json()
            data = jsonStuff['data']

            await message.channel.send(data[0]['quoteText'])

        else:
            await message.author.send(f"There was an error fetching the quote. The http code is {get.status_code}")
    if message.content.startswith('$error'):
        await message.author.send(f"There was an error fetching the quote.")

client.run(
    'token')
