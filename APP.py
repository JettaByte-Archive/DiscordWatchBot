import os
import asyncio
import requests
import discord
from discord import Webhook, RequestsWebhookAdapter
from discord.ext.commands import bot

webhooks = input("Please enter the webhook address | ")
tokens = input("Please enter your bot token | ")

client = discord.Client()


@client.event
async def on_ready():
    print('Start the watch process')


@client.event
async def on_message(message):
    webhook = Webhook.from_url(
        webhooks,
        adapter=RequestsWebhookAdapter())
    webhook.send("You have confirmed that a new message has been sent.")
    webhook.send(message)
    webhook.send(message.content)
    print('You have confirmed that a new message has been sent.')
    print(message)
    print(message.content)


client.run(tokens)
