import nextcord

from nextcord.ext import commands
from datetime import datetime


class Change_nicks(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        print('Cogs id loaded - Change_nicks')

    start_time = datetime.now()

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def changenickforall(self, ctx):
        nick = ctx.message.content.split(' ', 1)[1]
        await ctx.send("Устанавливаю всем никнеймы " + nick)
        for member in ctx.guild.members:
            try:
                if (member.nick != nick):
                    await member.edit(nick=nick)
            except Exception as ex:
                print(ex)
        await ctx.send("Готово!")

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def clearnicknames(self, ctx):
        await ctx.send("Очищаю всем никнеймы")
        for member in ctx.guild.members:
            try:
                if (member.nick != None):
                    await member.edit(nick=None)
            except Exception as ex:
                print(ex)
        await ctx.send("Готово!")


async def setup(bot):
    bot.add_cog(Change_nicks(bot))

