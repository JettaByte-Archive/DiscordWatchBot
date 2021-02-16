import os
import asyncio
import requests
import discord
from discord import Webhook, RequestsWebhookAdapter
from discord.ext.commands import bot

webhooks = input("웹후크 주소를 입력해주세요")
tokens = input("봇 토큰을 입력해주세요")

client = discord.Client()


@client.event
async def on_ready():
    print('감시 시작')
    print('다음 봇에서 감시중 입니다.')
    print(client.user.name)
    print(client.user.id)
    print('--------------')


@client.event
async def on_message(message):
    webhook = Webhook.from_url(
        webhooks,
        adapter=RequestsWebhookAdapter())
    webhook.send("감시 대상에서 새로운 메세지가 발송됨.")
    webhook.send("해당 메세지 내용:")
    webhook.send(message)
    webhook.send(message.content)
    print('감시 대상에서 새로운 메세지가 발송됨.')
    print(message)
    print(message.content)


client.run(tokens)