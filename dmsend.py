
# 봉순#4888 : MASS DM BOT SOURCE
# 오픈소스 이용하여 제작되었습니다


import discord
import asyncio
import datetime

client = discord.Client()

@client.event
async def on_ready():
    print("봇이 정상적으로 실행되었습니다.")
    game = discord.Game('쒸이발 병쉰 은수')
    await client.change_presence(status=discord.Status.online, activity=game)

#/dm {할말}로 전체DM 전송
@client.event
async def on_message(message):
    if message.content.startswith('/dm'):
        for i in message.guild.members:
            if i.bot == True:
                pass
            else:
                try:
                    msg = message.content[4:]
                    if message.author.id == 551142149777915914:
                        embed = discord.Embed(colour=0x1DDB16, timestamp=message.created_at, title="ℭ𝔞𝔯𝔱𝔢𝔩")
                        embed.add_field(name="읽어 쉬발", value=msg, inline=True)
                        embed.set_footer(text=f"discord.gg/3nSY2n6")
                        await i.send(embed=embed)
                except:
                    pass


client.run('NzE3MTQzMTE3ODA3MjIyNzk0.XtWBqg.kMuO8AQYKYQwsj6hpj-VZ6BjZo4')
