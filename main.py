from lifesupport import keepalive
import os

import discord
import exporting

exporter = exporting.Exporter()
import random
import ffmpeg

bot = discord.Bot()

@bot.event
async def on_application_command_error(ctx: discord.ApplicationContext,
                                       error: discord.DiscordException):
  embed = discord.Embed(
    title=":boom::boom::boom:OOPS! YOU FUC  KED UP      .",
    description="we have recieved an error! We shall now display it to you",
    color=0xff3366)
  embed.add_field(name="error;", value="tbd", inline=False)
  embed.add_field(name="trace;", value=f"```{str(error)}```", inline=False)
  embed.add_field(
    name="problem? :trolface",
    value="open up a [issue](https://github.com/nthprsnl/ytdl-bot/issues)",
    inline=False)
  embed.set_footer(text="made with rage, spite and love; by nth")
  await ctx.respond(embed=embed)
  raise error


@bot.event
async def on_ready():
  print(f"{bot.user} is ready and online!")


def checkLink(link, type):
  if 'youtube.com' in link:
    return True
  elif 'youtu.be' in link:
    return True
  else:
    return False


@bot.slash_command(name="video", description="free for all")
async def export_video(ctx: discord.ApplicationContext, 
                 url: discord.Option(str), 
                 type: discord.Option(str, choices=['mp4', 'mkv']), 
                 upload: discord.Option(str, choices=["true", "false"])):
  await ctx.respond(':bangbang: exporting!')
  res = exporter.export('video', url,type)
  if upload == "true" or exporter.get_filesize(res[3]) > 20.0:
    link = exporter.upload(res[3])
    await ctx.respond('and uploading :boom:')
    embed = discord.Embed(
      title="we have recieved your",
      description="meow meow meow",
      color=0xff3366)
    embed.add_field(name="url", value=url, inline=False)
    embed.add_field(name="upload url", value=f"```{link}``` YOU HAVE ONE HOUR TO DOWNLOAD.", inline=False)
    embed.add_field(
      name="problem? :trolface",
      value="open up a [issue](https://github.com/nthprsnl/ytdl-bot/issues)",
      inline=False)
    embed.set_footer(text="made with rage, spite and love; by nth")
    await ctx.respond(embed=embed)
  else:
    link = None
    embed = discord.Embed(
      title="we have recieved your",
      description="meow meow meow",
      color=0xff3366)
    embed.add_field(name="url", value=url, inline=False)
    # embed.add_field(name="trace;", value=f"```{str(error)}```", inline=False)
    embed.add_field(
      name="problem? :trolface",
      value="open up a [issue](https://github.com/nthprsnl/ytdl-bot/issues)",
      inline=False)
    embed.set_footer(text="made with rage, spite and love; by nth")
    await ctx.respond(embed=embed, file=discord.File(res[3]))

@bot.slash_command(name="audio", description="free for all")
async def export_audio(ctx: discord.ApplicationContext, 
                 url: discord.Option(str), 
                 type: discord.Option(str, choices=['mp3', 'wav']), 
                 upload: discord.Option(str, choices=["true", "false"])):
  await ctx.respond(':bangbang: exporting!')
  res = exporter.export('audio', url,type)
  print(res)
  if upload == "true" or exporter.get_filesize(res[3]) > 20.0:
    # link = exporter.upload(res[3])
    await ctx.respond('and uploading :boom:')
    embed = discord.Embed(
      title="we have recieved your",
      description="meow meow meow",
      color=0xff3366)
    embed.add_field(name="url", value=url, inline=False)
    embed.add_field(name="upload url", value=f"```{link}``` YOU HAVE ONE HOUR TO DOWNLOAD.", inline=False)
    embed.add_field(
      name="problem? :trolface",
      value="open up a [issue](https://github.com/nthprsnl/ytdl-bot/issues)",
      inline=False)
    embed.set_footer(text="made with rage, spite and love; by nth")
    await ctx.respond(embed=embed)
  else:
    link = None
    embed = discord.Embed(
      title="we have recieved your",
      description="meow meow meow",
      color=0xff3366)
    embed.add_field(name="url", value=url, inline=False)
    # embed.add_field(name="trace;", value=f"```{str(error)}```", inline=False)
    embed.add_field(
      name="problem? :trolface",
      value="open up a [issue](https://github.com/nthprsnl/ytdl-bot/issues)",
      inline=False)
    embed.set_footer(text="made with rage, spite and love; by nth")
    await ctx.respond(embed=embed, file=discord.File(res[3]))
    
keepalive()
bot.run(os.environ['token'])  # run the bot with the token
