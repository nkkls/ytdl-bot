from lifesupport import keepalive
import os

import discord
import exporting

exporter = exporting.Exporter()
import random
import ffmpeg

bot = discord.Bot()
youtube = bot.create_group("youtube", "Do stuff youtube-related")

@bot.event
async def on_application_command_error(ctx: discord.ApplicationContext, error: discord.DiscordException):
  embed=discord.Embed(title="OOPS! YOU FUC  KED UP      .", description="we have recieved an error! We shall now display it to you", color=0xff3366)
  embed.add_field(name="error;", value="tbd", inline=False)
  embed.add_field(name="trace;", value=f"```{str(error)}```", inline=False)
  embed.set_footer(text="made with rage, spite and love; by nth")
  await ctx.respond(embed=embed)
  
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

@bot.slash_command(name = "test", description = "uploads meow.txt")
async def test(ctx):
   await ctx.send(f"returned ```{str(exporter.export('video', 'https://www.youtube.com/watch?v=dQw4w9WgXcQ', 'mp4', True))}```")

# @youtube.command(name = "video", description = "export youtube video")
# async def video(
#     ctx: discord.ApplicationContext,
#     url: discord.Option(str),
#     # type: discord.Option(str, choices=['mp3', 'aac','wav','m4a','ogg'])
#     ):

#       if checkLink(url) == False:
#         await ctx.respond('not a valid youtube url, exploding 💥')
#         return

#       type = "mp4"
#       id = random.randint(1,1000)
#       ydl_opts = {
#           'format': 'mp4/best',
#           "outtmpl": .mp4",
#       }

#       await ctx.respond('extracting...')

#       with yt_dlp.YoutubeDL(ydl_opts) as ydl:
#           err = ydl.download(url)
#           # if err == None:
#           #   await ctx.respond(f'recieved error code {err}, whoops!\n usually, it means that {errCodes.get(err, "`not listed in the book o errors`")}, exploding 💥')
#           #   return
#           await ctx.respond('extracting finished! uploading file', file=discord.File(f"{id}.{type}"))
#           os.remove(f"{id}.{type}")
#           # os.remove(f"{id}")

# @youtube.command(name = "audio", description = "export youtube audio")
# async def audio(
#     ctx: discord.ApplicationContext,
#     url: discord.Option(str),
#     type: discord.Option(str, choices=['mp3', 'aac','wav','m4a','ogg'])):

#       if checkLink(url) == False:
#         await ctx.respond('not a valid youtube url, exploding 💥')
#         return
      
#       id = random.randint(1,1000)
#       ydl_opts = {
#           'format': 'm4a/bestaudio/best',
#           'postprocessors': [{
#               'key': 'FFmpegExtractAudio',
#               'preferredcodec': type,
#           }],
#           "outtmpl": f"{id}",
#           'match_filter': longer_than_a_minute,
#       }

#       message = await ctx.respond('extracting...')
      
#       with yt_dlp.YoutubeDL(ydl_opts) as ydl:
#           err = ydl.download(url)

#           await ctx.respond('extracting finished! uploading file', file=discord.File(f"{id}.{type}"))
#           os.remove(f"{id}.{type}")

keepalive()
bot.run(os.environ['token']) # run the bot with the token
