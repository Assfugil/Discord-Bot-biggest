# bot.py
import os
import json
import discord
import time
from discord.ext import commands


checkemoji = ":Check:670929822863720468"
uncheckemoji = ":Uncheck:670929839795994624"
token = "NjY3NTM3ODYyOTEyMzc2ODUz.Xi2QNg.hcjl0SNVaQUX5hsTg9jVMAUGwaI"
whatsnew = "這次更新可以完全替代掉3個投票機器人了 <YAY> 。哈哈等著被踢吧投票機器人們!"
suggestid = 670920875146477578
wantroleid = 670920928519127051
voteid = 670925187796959242
reportid = 671007736401625089
logid = 671017813921628191


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False
bot = commands.Bot(command_prefix='>')
bot.remove_command("help")
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name='星月萬歲!'))
    print(f'本機器人已與Discord連線，使用者名稱為{bot.user} !'f'Created by FANA Owner')




@bot.command()
async def help(ctx):
    embed = discord.Embed(
        title="指令列表",
        description = f"Hello! {ctx.author.mention}，指令列表在下面喔!!! \n`>help - 你已經在用了，不多說 :thinking:\n>report <使用者> <原因>\n>warn <使用者> <原因>\n>poll <投票內容>- 投票系統\n>whatsnew - 查看最新動態\n>suggest <建議> - 有好建議??為何不說呢?\n>wantrole <申請項目> <顏色> <原因> - 有好才華?想要更酷?好!立即申請!`",
        colour = discord.Colour.green()
        )
    await ctx.send(content=None,embed=embed)
    
@bot.command()
async def suggest(ctx,* ,arg2):
    channel = bot.get_channel(suggestid)
    await ctx.message.delete()
    await ctx.send(f"已傳送給星月建議: {arg2}")
    embed = discord.Embed(
        title="建議",
        description = f"{arg2}",
        colour = discord.Colour.blue()
                          )
    embed.add_field(name="傳送者", value=f"{ctx.author.mention}")
    await channel.send(content=None, embed=embed)

@bot.command()
async def wantrole(ctx, role,color, *, reason):
    channel = bot.get_channel(wantroleid)
    await ctx.message.delete()
    await ctx.send(f"已申請身分組\"{role}\"，他要{color}，推薦原因是 : {reason}!!")
    embed= discord.Embed(
        title = "身分組申請",
        colour = discord.Colour.gold(),
        description = f"原因: `{reason}`"
        )
    embed.add_field(name="使用者", value=f"{ctx.author.mention}")
    embed.add_field(name="身分組", value=f"{role}")
    embed.add_field(name="顏色", value=f"{color}")
    await channel.send(content=None,embed=embed)

@bot.command()
async def whatsnew(ctx):
    await ctx.message.delete()
    embed= discord.Embed(
        title = "最新消息",
        description = whatsnew,
        colour = discord.Colour.red()
        )
    await ctx.send(content=f"嗶嗶嗶，查到最新消息{ctx.author.mention}!",embed=embed)

@bot.command(pass_context = True)
@commands.has_role("管理員")
async def poll(ctx,*,info):
            await ctx.message.delete()
            channel = bot.get_channel(voterid)
            embed = discord.Embed(
                title = " :bar_chart: 請投票!",
                description = f"{info}",
                colour = discord.Colour.gold()
                )
            votemsg = await channel.send(content = None,embed=embed)
            await votemsg.add_reaction(checkemoji)
            await votemsg.add_reaction(uncheckemoji)


@bot.command()
async def report(ctx, member: discord.Member, *,reason):
    await ctx.message.delete()
    channel = bot.get_channel(reportid)
    embed = discord.Embed(
        title = "檢舉",
        description = f"原因 : {reason}",
        colour = discord.Colour.red()
        )
    embed.add_field(name="檢舉人", value=ctx.author.mention)
    embed.add_field(name="被檢舉人", value=member.mention)
    embedmsg = await channel.send(content="按下勾勾便可刪除本檢舉",embed=embed)
    await embedmsg.add_reaction(checkemoji)
@bot.command()
async def mute(ctx, member: discord.Member, *,reason):
    await ctx.message.delete()
    role = discord.utils.get(member.guild.roles, name="Mute")
    await member.add_roles(role)
    embed = discord.Embed(
        title = "禁言",
        colour = discord.Colour.purple()
        )
    embed.add_field(name="禁言使用者", value=)

@bot.event
async def on_reaction_add(reaction, user):
    if (user.bot == False):
        if reaction.message.channel == bot.get_channel(reportid):
            if reaction.emoji.name == "Check":
                await reaction.message.delete()
    

bot.run(token)

