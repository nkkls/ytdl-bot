from keepingalive import keepalive
import os

import discord
import yt_dlp

import random
import ffmpeg
import subprocess

bot = discord.Bot()
youtube = bot.create_group("youtube", "Do stuff youtube-related")


@bot.event
async def on_application_command_error(ctx: discord.ApplicationContext, error: discord.DiscordException):
  embed=discord.Embed(title="OOPS! YOU FUC  KED UP      .", description="we have recieved an error! We shall now display it to you", color=0xfc6363)
  embed.add_field(name="error;", value="ermm insert debug error here", inline=False)
  embed.add_field(name="trace;", value=f"```{str(error)}```", inline=False)
  embed.set_footer(text="made with rage, spite and love; by nth")
  await ctx.respond(embed=embed)
errCodes = {
  0: "`video is too long`"
}

def get_video_duration(file_path):
    command = ['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'default=noprint_wrappers=1:nokey=1', file_path]
    duration = subprocess.check_output(command, stderr=subprocess.STDOUT).decode()
    return float(duration)
  
@bot.event
async def on_ready():
    print(f"{bot.user} is ready and online!")

def checkLink(link):
    if 'youtube.com' in link:
      return True
    elif 'youtu.be' in link:
      return True
    else:
      return False

def longer_than_a_minute(info, *, incomplete):
          """Download only videos longer than a minute (or with unknown duration)"""
          duration = info.get('duration')
          if duration and duration > 3600:
              return 'videos too long, sorry'

@youtube.command(name = "video", description = "export youtube video")
async def video(
    ctx: discord.ApplicationContext,
    url: discord.Option(str),
    # type: discord.Option(str, choices=['mp3', 'aac','wav','m4a','ogg'])
    ):

      if checkLink(url) == False:
        await ctx.respond('not a valid youtube url, exploding 💥')
        return

      type = "mp4"
      id = random.randint(1,1000)
      ydl_opts = {
          'format': 'mp4/best',
          "outtmpl": f"{id}.mp4",
          'match_filter': longer_than_a_minute,
      }

      await ctx.respond('extracting...')

      with yt_dlp.YoutubeDL(ydl_opts) as ydl:
          err = ydl.download(url)
          # if err == None:
          #   await ctx.respond(f'recieved error code {err}, whoops!\n usually, it means that {errCodes.get(err, "`not listed in the book o errors`")}, exploding 💥')
          #   return
          await ctx.respond('extracting finished! uploading file', file=discord.File(f"{id}.{type}"))
          os.remove(f"{id}.{type}")
          # os.remove(f"{id}")

@youtube.command(name = "audio", description = "export youtube audio")
async def audio(
    ctx: discord.ApplicationContext,
    url: discord.Option(str),
    type: discord.Option(str, choices=['mp3', 'aac','wav','m4a','ogg'])):

      if checkLink(url) == False:
        await ctx.respond('not a valid youtube url, exploding 💥')
        return
      
      id = random.randint(1,1000)
      ydl_opts = {
          'format': 'm4a/bestaudio/best',
          'postprocessors': [{
              'key': 'FFmpegExtractAudio',
              'preferredcodec': type,
          }],
          "outtmpl": f"{id}",
          'match_filter': longer_than_a_minute,
      }

      message = await ctx.respond('extracting...')
      
      with yt_dlp.YoutubeDL(ydl_opts) as ydl:
          err = ydl.download(url)
          # if err == None:
          #   await ctx.respond(f'recieved error code {err}, whoops!\n usually, it means that {errCodes.get(err, "`not listed in the book o errors`")}, exploding 💥')
          #   return
        
          # video_duration = get_video_duration(f"{id}.{type}")
          # target_bitrate = int((19 * 8192) / video_duration)
          
          # subprocess.run(['ffmpeg', '-i', f"{id}.{type}",'-vcodec','libx264','-crf','24',f"{id}.{type}"])

          await ctx.respond('extracting finished! uploading file', file=discord.File(f"{id}.{type}"))
          os.remove(f"{id}.{type}")
          # os.remove(f"{id}")

keepalive()
bot.run(os.environ['token']) # run the bot with the token
