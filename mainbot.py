import os
import discord
import time
import datetime
import random
from discord.ext import commands

checkemoji = ":Check:670929822863720468"
uncheckemoji = ":Uncheck:670929839795994624"
token = "NjY3NTM3ODYyOTEyMzc2ODUz.Xi7XsA.X34T1DWpJFTIAY5zADhZrsGkPvG"
suggestid = 670920875146477578
wantroleid = 670920928519127051
voteid = 670925187796959242
reportid = 671007736401625089
logid = 671017813921628191
welcomeid = 670920495176220686



normalcommand = " \n\n\n>help - 你已經在用了，不多說\n>ticket - 有問題?管理員特別為您解答!\n>jointime - [MAIN FEATURE]確認加入時間，若超過特定時間會得到特殊身分組(本指令只能得到身分組)\n>role <名稱> <認得的顏色(使用>colorlist)> (加入1天以上) - 創建專屬的身分組" 
controlcommand = "\n***管理類***\n>member - 查看使用者分類\n>nick <使用者> <名稱(選填，空白表示重設)> - 更改暱稱(要改自己的用 /nick <名稱> 就好了)\n>ban <使用者> <原因(選填)>\n>mute <使用者> <原因> - 靜音(即將回來，已移除)\n>report <使用者> <原因> - 檢舉(所有人皆可) "
suggestcommand = "\n***民意調查***\n>poll <投票內容>- 投票系統(管理員限定)\n>suggest <建議> - 有好建議??為何不說呢?\n>wantrole <申請項目> <顏色> <原因> - 有好才華?想要更酷?好!立即申請!"
funcommand = "\n***玩樂類***\n>draw <號碼> [要抽的項目] - [管理員限定]抽獎，直接輸入 >draw獲得詳情"
infocommand = "\n***資訊類***\n>updatemembers - 更新儀表板\n>guildinfo - 顯示本群組的資料\n>userinfo <使用者> - 看看他的資料，比對自己。\n>whatsnew - 查看最新動態\n>update - 更新歷史\n>colorlist <顏色(選填)> - 加顏色是預覽，未加是列表"
helpcommands = f"Hello!指令列表在下面喔!!!{normalcommand} {controlcommand} {suggestcommand} {funcommand} {infocommand}"


def gettickettag(member):
    return f"{member.name}{member.discriminator}s-ticket"

def getcolor(color):
    if color == "藍綠色":
        return discord.Colour.teal()
    elif color == "深藍綠色":
        return discord.Colour.dark_teal()
    elif color == "綠色":
        return discord.Colour.green()
    elif color == "深綠色":
        return discord.Colour.dark_green()
    elif color == "藍色":
        return discord.Colour.blue()
    elif color == "深藍色":
        return discord.Colour.dark_blue()
    elif color == "紫色":
        return discord.Colour.purple()
    elif color == "深紫色":
        return discord.Colour.dark_purple()
    elif color == "粉紅色":
        return discord.Colour.magenta()
    elif color == "深粉紅色":
        return discord.Colour.dark_megenta()
    elif color == "黃色":
        return discord.Colour.gold()
    elif color == "深黃色":
        return discord.Colour.dark_gold()
    elif color == "橘色":
        return discord.Colour.orange()
    elif color == "深橘色":
        return discord.Colour.dark_orange()
    elif color == "紅色":
        return discord.Colour.red()
    elif color == "深紅色":
        return discord.Colour.dark_red()
    elif color == "灰色":
        return discord.Colour.lighter_grey()
    elif color == "深灰色":
        return discord.Colour.dark_grey()
    elif color == "Discord圖示色":
        return discord.Colour.blurple()
    elif color == "Discord主題色":
        return discord.Colour.greyple()
    elif color == "黑色":
        return 0x000000
    elif color == "白色":
        return 0xffffff
    else:
        return "unknown_color" 
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
async def member(ctx):
    membercount = 0
    botcount = 0
    onlinecount = 0
    idlecount = 0
    noncount = 0
    offlinecount = 0
    admincount = 0
    nonadmincount = 0
    for count in ctx.guild.members:
        if count.bot:
            botcount = botcount +1
        else:
            membercount = membercount +1
        if str(count.status) == "online":
            onlinecount +=1
        elif str(count.status) == "idle":
            idlecount +=1
        elif str(count.status) == "offline":
            offlinecount +=1
        else :
            noncount +=1
        if count.guild_permissions.kick_members==True:
            admincount +=1
        else:
            nonadmincount +=1
            
    embed = discord.Embed(
        title = "使用者們",
        description = "關於使用者...",
        colour = getcolor("黃色")
        )
    embed.add_field(name="種類判別",value= f"機器人:{botcount}\n真人:{membercount}")
    embed.add_field(name="狀態判別",value = f"上線 :{onlinecount}\n閒置 :{idlecount}\n不在線 :{offlinecount}\n靜音: {noncount}")
    embed.add_field(name="權限判別",value = f"管理員:{admincount}\n非管理員{nonadmincount}")
    await ctx.send(embed=embed)
    





@bot.command()
async def colorlist(ctx,color = None):
        if color == None:
            await ctx.send("白色,黑色,藍綠色,深藍綠色,綠色,深綠色,藍色,深藍色,紫色,深紫色,粉紅色,深粉紅色,黃色,深黃色,橘色,深橘色,紅色,深紅色,灰色,深灰色,Discord圖示色,Discord主題色")
        else:
            if getcolor(color) != "unknown_color":
                embed = discord.Embed(
                    title = "顏色預覽",
                    description = f"這是 {color}",
                    colour = getcolor(color)
                    )
                await ctx.send(embed=embed)
            else:
                await ctx.send("請使用 >colorlist 來得知顏色列表")



@bot.command()
@commands.has_permissions(kick_members=True)
async def ban(ctx,member: discord.Member,reason = "") :
    embed = discord.Embed(
        title="封鎖紀錄",
        description = f"使用者已被封鎖",
        colour = discord.Colour.purple()
        )
    channel = bot.get_channel(logid)
    embed.add_field(name="封鎖人",value=ctx.author.mention)
    embed.add_field(name="被封鎖人", value=member.mention)
    if reason == "":
        pass
    else:
        embed.add_field(name="原因",value=reason)
    await channel.send(embed=embed)
    if reason != "":
        await member.send(f"您已從{ctx.guild.name}被{ctx.author.mention}封鎖!，原因為:{reason}")
    await ctx.guild.ban(member, reason=reason)
    await ctx.send("若要解除封鎖請自行到 伺服器設定 更改，謝謝您!")
    await guild.ban(member)



@bot.command()
async def updatemembers(ctx):
    voice = None
    category = discord.utils.get(ctx.guild.categories, name = "儀表板")
    try:
    	voice = discord.utils.get(ctx.guild.voice_channels, category_id=category.id)
    	await voice.delete()
    except:
        pass
    try:
    	voice = discord.utils.get(ctx.guild.voice_channels, category_id=category.id)
    	await voice.delete()
    except:
        pass
    try:
    	voice = discord.utils.get(ctx.guild.voice_channels, category_id=category.id)
    	await voice.delete()
    except:
        pass
    membercount = 0
    botcount = 0
    for count in ctx.guild.members:
        if count.bot:
            botcount = botcount +1
        else:
            membercount = membercount +1
    await ctx.guild.create_voice_channel(name=f"真實用戶:{membercount}",category=category)
    await ctx.guild.create_voice_channel(name=f"機器人:{botcount}",category=category)
    await ctx.send("已更新!")
    




@bot.command()
async def guildinfo(ctx):
    
    guild = ctx.guild
    features = ""
    emojinames = ""
    for emoji in guild.emojis:
        emojinames = f":{emoji.name}:\n{emojinames}"
    embed = discord.Embed(
        title = "群組資訊",
        colour = ctx.author.color
        )   
    embed.add_field(name="名稱",value=guild.name)
    embed.add_field(name="特殊貼圖",value=emojinames)
    embed.add_field(name="伺服器所在地區",value=guild.region)
    embed.add_field(name="掛機頻道",value=guild.afk_channel)
    embed.add_field(name="群組主人",value=bot.get_user(guild.owner_id).mention)
    
    await ctx.send(embed=embed)


@bot.command()
@commands.has_role("【Jointime】超級新手")
async def role(ctx,name,color):
    if getcolor(color) == "unknown_color":
        await ctx.send("請使用 >colorlist")
    else:
        embed = discord.Embed(
            title="創建身分組",
            description="已成功創建身分組",
            colour=getcolor(color)
            )
        await ctx.send(embed=embed)
        newrole = await ctx.guild.create_role(name=name,colour = getcolor(color))
        await ctx.author.add_roles(newrole)



    

@bot.command()
async def help(ctx):
    authorname = ctx.author.name
    embed = discord.Embed(
        title="指令列表",
        description = helpcommands,
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
@commands.has_permissions(kick_members = True)
async def nick(ctx,member: discord.Member,*,name= None):
    await ctx.message.delete()
    await member.edit(nick=name)
    if name==None:
        await ctx.send(f"已重製{member.mention}的暱稱")
    else:
        await ctx.send(f"已設{member.mention}的暱稱為{name}")




@bot.command()
async def ticket(ctx):
    try:
        oldchannel = discord.utils.get(bot.get_all_channels(), name=gettickettag(ctx.author))
        await oldchannel.delete()
    except:
        pass
    ticket = await ctx.guild.create_text_channel(name=gettickettag(ctx.author))
    await ticket.set_permissions(ctx.author, send_messages = True,read_message_history = True,read_messages=True)
    await ticket.set_permissions(ctx.guild.default_role, read_message_history=False,read_messages = False)
    await ctx.message.delete()
    await ctx.send("專屬頻道已創立!")
    embed=discord.Embed(
        title="歡迎",
        description = "這裡是你的專屬頻道，稍等一下，並且先問問題。管理員不久後就會過來了!",
        color = ctx.author.colour
        )
    ticket = discord.utils.get(bot.get_all_channels(), name=gettickettag(ctx.author))
    await ticket.send(embed=embed)
    await ticket.send("@everyone")






@bot.command()
async def jointime(ctx):
    await ctx.send(f"{ctx.author.mention} 嗶嗶嗶...檢測中...")
    await ctx.message.delete()
    now=datetime.datetime.now()
    join = ctx.author.joined_at
    role = discord.utils.get(ctx.author.guild.roles, name="【Jointime】加入超過一秒...")
    await ctx.author.add_roles(role)
    jointext = "檢測到您加入未滿一小時，因此給你 [加入超過一秒...]"
    print((now-join).days)
    if (now-join).days >= 1:
        role = discord.utils.get(ctx.author.guild.roles, name="【Jointime】超級新手")
        await ctx.author.add_roles(role)
        jointext = "檢測到您加入過了一天，因此給你 [超級新手]"
        if (now-join).days >= 30:
            role = discord.utils.get(ctx.author.guild.roles, name="【Jointime】已加入一月")
            oldrole = discord.utils.get(ctx.author.guild.roles, name="【Jointime】超級新手")
            await ctx.author.add_roles(role)
            jointext = "檢測到您加入過了30天!!因此給你 [已加入一月]"
            if (now-join).days >= 365:
                role = discord.utils.get(ctx.author.guild.roles, name="【Jointime】一年老玩家")
                oldrole = discord.utils.get(ctx.author.guild.roles, name="【Jointime】已加入一月")
                jointext = "檢測到您加入過了一年!!!因此給你 [一年老玩家]!同時讓你在使用者列表裡額外分開!"
                if (now-join).days >= 730:
                    role = discord.utils.get(ctx.author.guild.roles, name="【Jointime】兩年超級老手")
                    oldrole = discord.utils.get(ctx.author.guild.roles, name="【Jointime】一年老玩家")
                    await ctx.author.add_roles(role)
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
@commands.has_permissions(kick_members=True)

async def draw(ctx, wantcount = None, *,info=None):
    await ctx.message.delete()
    if wantcount == None:
        await ctx.send("除了輸入 >draw，也要輸入一個使用者的代號(每次輸入指令皆會重新抽，並自動無條件消去)")
    else:
        if is_number(wantcount) == False:
            await ctx.send("請輸入一個數字")
        else:
            memberlist = []
            membercount = 0

            for count in ctx.guild.members:
                if count.bot == True:
                    pass
                else:
                    memberlist.append(count)
                    membercount += 1
            if int(wantcount) > membercount or int(wantcount) < 1:
                await ctx.send("您輸入的使用者不存在")
            else:
                member = random.choice(memberlist)
                embed = discord.Embed (
                    title = "幸運兒出爐!!",
                    description = f"幸運兒是 **{member.mention}**",
                    colour = member.color
                    )
                embed.add_field(name="抽獎人",value=f"{ctx.author.mention}\n")
                embed.add_field(name="選擇號碼",value=f"{wantcount}\n")
                if info == None:
                    pass
                else:
                    embed.add_field(name="獎勵",value=f"{info}\n")
                await ctx.send(embed=embed)
    
    



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
    if False:
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
    update003.add_field(name="新增指令",value="userinfo,jointime,移除Mute")
    update003.add_field(name="BUG修復",value="Update 指令版本都是 V.0.0.1")
    update003.add_field(name="優化", value="優化了權限系統，管理員再怎麼改名稱也適用了")
    update003.add_field(name="新增功能", value="\"歡迎加入\" 系統，以及主要功能 Jointime[MAIN FEATURE]")
    await ctx.author.send(content=None,embed=update003)



bot.run(token)

