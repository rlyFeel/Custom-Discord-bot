import nextcord
from nextcord.ext.commands import Bot
import os
from cfg.cfg import *


activity = nextcord.Streaming(name="With 💙 for you ",url="https://www.youtube.com/watch?v=dQw4w9WgXcQ")

intents = nextcord.Intents.all()
bot = Bot(command_prefix="/", intents=intents, activity=activity, status=nextcord.Status.do_not_disturb)
bot.remove_command("help")



@bot.event
async def on_ready():
    channel = bot.get_channel(1037699996428009542)
    emb = nextcord.Embed(title='📚 Start', description='``` Ready to job!```')
    await channel.send(embed=emb)

    async def load_cogg(name):
        if (name == "database"): return
        bot.load_extension(f"cogs.{name}")

    async def reload_cogg(name):
        bot.unload_extension(f"cogs.{name}")
        bot.load_extension(f"cogs.{name}")

    print('------')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            try:
                await load_cogg(filename[:-3])
            except Exception as ex:
                print(f"{filename[:-3]} crashed. I'm automaticly fixing it")
                await reload_cogg(filename[:-3])


@bot.event
async def on_member_join(member):
    role = nextcord.utils.get(member.guild.roles, id=984170071180070932)
    await member.add_roles(role)



bot.run(DISCORD_TOKEN)