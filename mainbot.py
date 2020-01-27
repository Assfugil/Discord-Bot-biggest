# bot.py
import os
import json
import discord
import time
import datetime
from discord.ext import commands


checkemoji = ":Check:670929822863720468"
uncheckemoji = ":Uncheck:670929839795994624"
token = "NjY3NTM3ODYyOTEyMzc2ODUz.Xi2QNg.hcjl0SNVaQUX5hsTg9jVMAUGwaG"
suggestid = 670920875146477578
wantroleid = 670920928519127051
voteid = 670925187796959242
reportid = 671007736401625089
logid = 671017813921628191
welcomeid = 671280893213802507
admin = "管理員"

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
    await bot.change_presence(activity=discord.Game(name='快快快快快用>help'))
    print(f'本機器人已與Discord連線，使用者名稱為{bot.user} !'f'Created by FANA Owner')


@bot.event
async def on_member_join(member):
    embed = discord.Embed(
        title = "歡迎加入我們",
        description = f"讓我們一起歡迎{member.mention}加入我們!使用>help吧!",
        colour = discord.Colour.blue()
        )
    channel = bot.get_channel(welcomeid)
    await channel.send(embed=embed)
    

@bot.event
async def on_member_remove(member):
    embed = discord.Embed(
        title="慢走!",
        description = f"慢走，{member.mention}。感謝您的一路陪伴!有機會再回來!",
        colour = discord.Colour.orange()
        )
    channel = bot.get_channel(welcomeid)
    await channel.send(embed=embed)

@bot.command()
async def help(ctx):
    embed = discord.Embed(
        title="指令列表",
        description = f"Hello! {ctx.author.mention}，指令列表在下面喔!!! \n\n\n>help - 你已經在用了，不多說\n>jointime - [MAIN FEATURE]確認加入時間，若超過一年會得到特殊身分組(本指令只能得到身分組)\n***管理類***\n>mute <使用者> <原因> - 靜音(處罰，管理員限定)\n>report <使用者> <原因> - 檢舉(所有人皆可)\n***民意調查***\n>poll <投票內容>- 投票系統(管理員限定)\n>suggest <建議> - 有好建議??為何不說呢?\n>wantrole <申請項目> <顏色> <原因> - 有好才華?想要更酷?好!立即申請!\n***資訊類***\n>userinfo <使用者> - 看看他的資料，比對自己。\n>whatsnew - 查看最新動態\n>update - 更新歷史",
        colour = discord.Colour.green()
        )
    await ctx.send(content=None,embed=embed)

@bot.command()
async def userinfo(ctx,member :discord.Member):
    if member.bot == False:
        embed = discord.Embed(
            title=f"{member.name}#{member.discriminator}的小檔案",
            description = f"沒有信用卡號碼謝謝._.\n\n=-=-=**使用者資料**=-=-=\n\n使用者名稱 : {member.name}\n使用者的TAG : {member.discriminator}\n使用者ID : {member.id}\n顯示名稱 : {member.display_name}\n帳號創建時間 : {member.created_at}\n\n=-=-=於本群組資料=-=-=\n\n暱稱:{member.nick}\n於{member.joined_at}加入本群組",
            colour = member.color
            )
    else:
        embed = discord.Embed(
            title=f"{member.name}#{member.discriminator} [機器人]的小檔案",
            description = f"沒有信用卡號碼謝謝._.\n\n=-=-=**使用者資料**=-=-=\n\n使用者名稱 : {member.name}\n使用者的TAG : {member.discriminator}\n使用者ID : {member.id}\n顯示名稱 : {member.display_name}\n帳號創建時間 : {member.created_at}\n\n=-=-=於本群組資料=-=-=\n\n暱稱:{member.nick}\n於{member.joined_at}加入本群組",
            colour = discord.Colour.blurple()
            )
    await ctx.send(embed=embed)

@bot.command()
async def jointime(ctx):
    await ctx.send(f"{ctx.author.mention} 嗶嗶嗶...檢測中...~~38度~~")
    await ctx.message.delete()
    now=datetime.datetime.now()
    join = ctx.author.joined_at
    role = discord.utils.get(ctx.author.guild.roles, name="【Jointime】加入超過一秒...")
    await ctx.author.add_roles(role)
    jointext = "檢測到您加入未滿一小時，因此給你 [加入超過一秒...]"
    print((now-join).days)
    if (now-join).days >= 1:
        role = discord.utils.get(ctx.author.guild.roles, name="【Jointime】超級新手")
        oldrole = discord.utils.get(ctx.author.guild.roles, name="【Jointime】加入超過一秒...")
        await ctx.author.add_roles(role)
        await ctx.author.remove_roles(oldrole)
        jointext = "檢測到您加入過了一天，因此給你 [超級新手]"
        if (now-join).days >= 30:
            role = discord.utils.get(ctx.author.guild.roles, name="【Jointime】已加入一月")
            oldrole = discord.utils.get(ctx.author.guild.roles, name="【Jointime】超級新手")
            await ctx.author.add_roles(role)
            await ctx.author.remove_roles(oldrole)
            jointext = "檢測到您加入過了30天!!因此給你 [已加入一月]"
            if (now-join).days >= 365:
                role = discord.utils.get(ctx.author.guild.roles, name="【Jointime】一年老玩家")
                oldrole = discord.utils.get(ctx.author.guild.roles, name="【Jointime】已加入一月")
                await ctx.author.add_roles(role)
                await ctx.author.remove_roles(oldrole)
                jointext = "檢測到您加入過了一年!!!因此給你 [一年老玩家]!同時讓你在使用者列表裡額外分開!"
                if (now-join).days >= 730:
                    role = discord.utils.get(ctx.author.guild.roles, name="【Jointime】兩年超級老手")
                    oldrole = discord.utils.get(ctx.author.guild.roles, name="【Jointime】一年老玩家")
                    await ctx.author.add_roles(role)
                    await ctx.author.remove_roles(oldrole)
                    jointext = "檢測到您加入過了兩年!!!因此給你 [兩年超級老手]!同時讓你在使用者列表裡額外分開並且可以免費使用本機器人的一些超級功能!"
    await ctx.send(f"{ctx.author.mention}，{jointext}")
    
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
    await ctx.send(f"已申請身分組\"{role}\"，他要{color}，推薦原因是delete : {reason}!!")
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
        title = "群組進出系統&資料類型&加入時間獎勵大更新",
        description = "1.群組進出系統 - 到歡迎的頻道將會有新的機器人歡迎您!!!\n2.資料類型大更新 - 可以用原以為很廢卻很方便的 >userinfo 了!!! \n3.獨家功能:加如時間獎勵大更新 [MAIN FEATURE] - 當加入伺服器一段時間後，將可以分別得到一個月以上,一年以上及傳奇的兩年以上身分組!(使用 >jointime)",
        colour = discord.Colour.red()
        )
    await ctx.send(content=f"嗶嗶嗶，查到最新消息{ctx.author.mention}!",embed=embed)

@bot.command(pass_context = True)
@commands.has_permissions(kick_members=True)
async def poll(ctx,*,info):
            await ctx.message.delete()
            channel = bot.get_channel(voteid)
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
    embedmsg = await channel.send(content=None,embed=embed)
    await embedmsg.add_reaction(checkemoji)
@bot.command()
@commands.has_permissions(kick_members=True)
async def mute(ctx, member: discord.Member, *,reason):
    
        channel = bot.get_channel(logid)
        await ctx.message.delete()
        role = discord.utils.get(member.guild.roles, name="Mute")
        await member.add_roles(role)
        embed = discord.Embed(
            title = "禁言",
            colour = discord.Colour.purple(),
            description = f"原因 : {reason}"
            )
        embed.add_field(name="禁言使用者", value=member.mention)
        await channel.send(content = None,embed=embed)

@bot.command()
async def update(ctx):
    await ctx.send("訊息太長了!因此將訊息傳送至你那!")
    update001 = discord.Embed(
        title="FANA 機器人更新 V.0.0.1",
        description = "創立!!!",
        colour = discord.Colour.gold()
        )
    update001.add_field(name="新增指令",value="whatsnew,help,wantrole,suggest")
    await ctx.author.send(content=None,embed=update001)
    update002 = discord.Embed(
        title="FANA 機器人更新 V.0.0.2",
        description = "投票系統大更新!!",
        colour = discord.Colour.gold()
        )
    update002.add_field(name="新增指令",value="poll 投票系統")
    await ctx.author.send(content=None,embed=update002)
    update003 = discord.Embed(
        title="FANA 機器人更新 V.0.0.3",
        description = "逞罰小更新!",
        colour = discord.Colour.gold()
        )
    update003.add_field(name="新增指令",value="update,mute,report")
    update003.add_field(name="指令修改",value="Help指令優化")
    await ctx.author.send(content=None,embed=update003)
    update003 = discord.Embed(
        title="FANA 機器人更新 V.0.0.4",
        description = "逞罰小更新!",
        colour = discord.Colour.gold()
        )
    update003.add_field(name="新增指令",value="userinfo,jointime")
    update003.add_field(name="BUG修復",value="Update 指令版本都是 V.0.0.1")
    update003.add_field(name="優化", value="優化了權限系統，管理員再怎麼改名稱也適用了")
    update003.add_field(name="新增功能", value="\"歡迎加入\" 系統，以及主要功能 Jointime[MAIN FEATURE]")
    await ctx.author.send(content=None,embed=update003)



bot.run(token)

