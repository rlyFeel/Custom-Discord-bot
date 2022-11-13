import nextcord

from nextcord.ext import commands
from cfg.dtb import *
from cfg.cfg import *


class Whid(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        print('Cogs is loaded - Whid')

    @commands.Cog.listener()
    async def on_message(self, message):

        if message.channel.id != :
            return
        if message.author.id == self.bot.user.id:
            return
        if not nextcord.utils.get(message.guild.roles, id=) in message.author.roles:
            return
        if len(message.content) != 32:
            await message.delete()
            emb = nextcord.Embed(title="Отправьте хвид в правильном формате",
                                color=nextcord.Color.dark_blue())
            await message.author.send(embed=emb)
            return
        match await add_hwid(message.author.id, message.content, message.author.name):
            case 0:
                emb = nextcord.Embed(title="Ваш хвид был добавлен!",
                                    description=f'**{message.content}**\n Вот ваш чит.\n',
                                    color=nextcord.Color.gold())
                await message.author.send(embed=emb)
            case 1:
                emb = nextcord.Embed(title="Ваш хвид был обновлен!",
                                    description=f'**{message.content}**\n Вот ваш чит.\n',
                                    color=nextcord.Color.gold())
                await message.author.send(embed=emb)
        await message.delete()
        await message.author.add_roles(nextcord.utils.get(message.guild.roles, id=))
        await message.author.remove_roles(nextcord.utils.get(message.guild.roles, id=))


async def setup(bot):
    bot.add_cog(Whid(bot))