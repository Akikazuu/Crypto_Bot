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

channelethos = discord.Object(id = "690254156228853805")
"""
channellmfr = discord.Object(id = "480336808073232394")
channelserya = discord.Object(id = "424979780899700749")
channelyaka = discord.Object(id = "453201375636094987")
channelmorph = discord.Object(id = "536651849311191041")
"""
def getDonate():
    donate = "```You can donate me in ETH,ETC ... (all erc20 token) to the next address : 0xaEe9672A5B8E735BDFfda9a96CD4321bcCc41b70```"
    need_help = "```First type ?help for get help.\nIf you have issue or have request you can text me on Discord at Akikazu#1604```"

    embed = discord.Embed(title = ":sparkles: Akikazu", description = "Thanks for use Crypto_Bot", color = 0x1C6C90)
    embed.add_field(name = ":money_mouth: Do you like this bot ? :money_mouth:", value = donate, inline = False)
    embed.add_field(name = ":information_source:  Do you need help ? :information_source: ", value = need_help, inline = False)
    embed.set_footer(text = "Developed by Akikazu, host by Antho")
    return embed

def getVersion():
    description_v1 = "```Start bot with 2 commands : ?top <X> and ?<coin>```"
    description_v11 = "```New feature : ?conv <ammount> <coin>, bug correction```"
    description_v12 = "```Big update : use the new coinmarketcap API, dynamic search of coin and logo on coinmarketcap.com, bug correction```"

    embed = discord.Embed(title = ":tools:  Crypto_Bot Changelog", description = "You can see all the update for the Bot", color = 0x5BD68D)
    embed.add_field(name = "Actual Version : v1.2", value = description_v12, inline = False)
    embed.add_field(name = "v1.1", value = description_v11, inline = False)
    embed.add_field(name = "v1.0", value = description_v1, inline = False)
    embed.set_footer(text = "Developed by Akikazu, host by Antho")
    embed.set_thumbnail(url = "https://www.nsrp.fr/img/changelogicon.png")

    return embed

def helpPLZ():
    description = "Type **?<coin>** to printout the info of this coin\n" + "Type **?conv <amount> <coin>** to printout the X coin conversion to € / $\n" + "Type **?top <amount>** to printout the top X coin\n" + "Type **?version** to printout the changelog for the bot\n" + "Type **?donate** to make donation\n" + "(List of coin in coinmarketcap.com only)"
    
    embed = discord.Embed(title = ":information_source: Bot helper", description = "", color = 0x3f89c1)
    embed.add_field(name = "Commands :", value = description, inline = False)
    embed.add_field(name = "Version :", value = "`v1.2`", inline = False)
    embed.set_footer(text = "Developed by Akikazu, host by Antho")
    return embed

def error(coin):
        embed = discord.Embed(title = ":no_entry_sign: Error", description = ":warning: Coin : " + coin.upper() + " not found in coinmarketcap API", color = 0xBC1D35)
        embed.set_footer(text = "Contact Akikazu if the currency exists in coinmarketcap.com")
        return embed

def getCoin(coin):
    ticker = coinmarketcap.getTickerData(coin)
    if ticker is None:
        return error(coin)
    else:
        return coinmarketcap.getDataV2(ticker, coin)

def getConv(number, coin):
    ticker = coinmarketcap.getTickerData(coin)
    if ticker is None:
        return error(coin)
    else:
        return coinmarketcap.getConv(ticker, number, coin)

@bot.event
async def on_ready():
    print("Bot is online")
    print(datetime.today())

@bot.event
async def Top10():
    await bot.wait_until_ready()
    while not bot.is_closed:
        embed = coinmarketcap.getTop(10)
        await bot.send_message(channelethos, embed = embed)
        """
        await bot.send_message(channellmfr, embed = embed)
        await bot.send_message(channelserya, embed = embed)
        await bot.send_message(channelyaka, embed = embed)
        await bot.send_message(channelmorph, embed = embed)
        """
        await asyncio.sleep(3600)

@bot.event
async def Purge():
    await bot.wait_until_ready()
    while not bot.is_closed:
        yesterday = datetime.today() - timedelta(days = 1)
        await bot.purge_from(channelethos, before = yesterday)
        #await bot.send_message(channelyaka, embed = yesterday)
        #await bot.purge_from(channellmf, before = yesterday)

        print("PURGE NOW !")
        await asyncio.sleep(3600)

@bot.event
async def on_message(message):
    msg = message.content.lower()
    words = msg.split()
    target = discord.Object(id = message.channel.id)

    if target.id == channelethos.id:#or target.id == channellmfr.id or target.id == channelserya.id or target.id == channelyaka.id or target.id == channelmorph.id:
        if msg.startswith("?"):

            cmd = words[0][1:]

            if len(words) == 1:
                if cmd == "help":
                    rep = helpPLZ()

                elif cmd == "version":
                    rep = getVersion()
            
                elif cmd == "donate":
                    rep = getDonate()

                else:
                    rep = getCoin(str(cmd))
                    
            if len(words) == 2:
                number = words[1]
                if cmd == "top":
                    rep = coinmarketcap.getTop(number)

            if len(words) == 3:
                number = words[1]
                coin = words[2]
                if cmd == "conv":
                    rep = getConv(number,coin)
            
            if rep:
                await bot.send_message(target, embed = rep)
            
bot.loop.create_task(Top10())
bot.loop.create_task(Purge())
bot.run("NDMyMjA2MDc1MDEwMzUxMTA0.Daqr7A.4uR5KqXcVKCxVOiq9O5IOU5B0ZU")
