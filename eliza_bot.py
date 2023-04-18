import os
import discord
from eliza import resposta_eliza
import re

intents = discord.Intents.default()
intents.all()
intents.members = True
intents.presences = True
intents.messages = True
intents.message_content = True

# Substitua YOUR_BOT_TOKEN pelo token do seu bot
TOKEN = os.environ["TOKEN"]


client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f"{client.user} está conectado ao servidor do Discord!")


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    # Checa se a mensagem é uma DM ou citação do bot
    if isinstance(message.channel, discord.DMChannel):
        mensagem_sem_citacao = re.sub(
            f"<@!?{client.user.id}>", "", message.content
        ).strip()
        resposta = resposta_eliza(mensagem_sem_citacao)
        await message.reply(resposta)

    elif (
        client.user in message.mentions or f"<@&1097861812730478665>" in message.content
    ):
        mensagem_sem_citacao = re.sub(
            f"<@!?{client.user.id}>", "", message.content
        ).strip()
        if ">" in mensagem_sem_citacao:
            mensagem_sem_citacao = mensagem_sem_citacao.split(">")[1].strip()
        resposta = resposta_eliza(mensagem_sem_citacao)

        await message.channel.send(f"{message.author.mention}, {resposta}")


client.run(TOKEN)
