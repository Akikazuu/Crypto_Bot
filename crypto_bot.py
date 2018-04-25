#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import datetime
from datetime import datetime, timedelta
import coinmarketcap

Client = discord.Client()
bot = commands.Bot(command_prefix = "?")
channel = discord.Object(id = "432260844110479360")
#432260844110479360 #linux
#432206626649407488 #test
def HelpPLZ():
    embed = discord.Embed(title = "Bot helper", description = "Type '?'coin to printout the info of this coin (list of coin in coinmarketcap.com only)", color = 0xFF9900)
    embed.set_footer(text = "Developed by Akikazu")
    return embed

def getCoin(coin):
    ticker = coinmarketcap.getTickerData(coin)

    if ticker is None:
        embed = discord.Embed(title = "Error", description = "Coin : " + coin.upper() + " not found in coinmarketcap API", color = 0xFF9900)
        embed.set_footer(text = "Contact Akikazu if the currency exists in coinmarketcap.com")
        return embed
    else:
        return coinmarketcap.getData(ticker, coin)

@bot.event
async def on_ready():
    print("Bot is online")
    print(datetime.today())

@bot.event
async def Top10():
    await bot.wait_until_ready()
    while not bot.is_closed:
        embed = coinmarketcap.getTop(10)
        await bot.send_message(channel, embed = embed)
        await asyncio.sleep(3600)

@bot.event
async def Purge():
    await bot.wait_until_ready()
    while not bot.is_closed:
        yesterday = datetime.today() - timedelta(days = 1)
        await bot.purge_from(channel, before = yesterday)
        print("PURGE NOW !")
        await asyncio.sleep(3600)

@bot.event
async def on_message(message):
    msg = message.content.lower()
    words = msg.split()
    if message.channel.id == channel.id:
        if msg.startswith("?"):
            cmd = words[0][1:]
            try:
                number = words[1]
                if cmd == "top":
                    rep = coinmarketcap.getTop(number)
            except :
                if cmd == "p":
                    await bot.purge_from(channel, before = datetime.now())
                if cmd == "help":
                    rep = HelpPLZ()
                else:
                    rep = getCoin(str(cmd))

            if rep:
                await bot.send_message(channel, embed = rep)

bot.loop.create_task(Top10())
bot.loop.create_task(Purge())
bot.run("NDMyMjA2MDc1MDEwMzUxMTA0.Daqr7A.4uR5KqXcVKCxVOiq9O5IOU5B0ZU")
