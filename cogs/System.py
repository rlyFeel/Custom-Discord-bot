import nextcord
import socket
import os

from cfg.system import *
from datetime import datetime
from nextcord.ext import commands



start_time = datetime.now()


class System(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        print('Cogs is loaded - System')

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def system(self, ctx):
        await ctx.send("Wait for analysis")
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        if sock.connect_ex((HOST, PORT)) == 0:
            emb = nextcord.Embed(title="** Server load **  ",
                                 description=f"🕛 Время ответа от сервера: =  {round(self.bot.latency * 1000)}ms\n "
                                             f"💻 Ответ сервера: ```root@admin:~# Server running| ✅```  \n"
                                             f"📗 Процессор: {cpu_per} % / 100% \n"
                                             f"📘 Память: {mem_info} % / 100% \n"
                                             f"📙 Время работы бота: {str(datetime.now() - start_time).split('.')[0]}",
                                 color=nextcord.Color.green())
            await ctx.send(embed=emb)

        else:
            emb = nextcord.Embed(title="📊 | ** Server load **",
                                 description=f"🕛 Время ответа от сервера: =  {round(self.bot.latency * 1000)}ms\n"
                                             f"💻 Ответ сервера: ```root@admin:~# Server is don't work| ❌```\n"
                                             f"📗 Процессор: {cpu_per} % / 100% \n"
                                             f"📘 Память: {mem_info} % / 100% \n"
                                             f"📙 Время работы бота: {str(datetime.now() - start_time).split('.')[0]}",
                                 color=nextcord.Color.red())
            await ctx.send(embed=emb)
        sock.close()

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def restart(self, ctx):
        os.system("pm2 restart 1")
        emb = nextcord.Embed(title="**Server - answer**", description="```Server restarted```", color=nextcord.Color.gold())
        await ctx.send(embed=emb)

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def start(self, ctx):
        os.system("pm2 start 1")
        emb = nextcord.Embed(title="**Server - answer**", description="```Server started```", color=nextcord.Color.gold())
        await ctx.send(embed=emb)

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def stop(self, ctx):
        os.system("pm2 stop 1")
        emb = nextcord.Embed(title="**Server - answer**", description="```Server stoped```", color=nextcord.Color.gold())
        await ctx.send(embed=emb)

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def reboot(self, ctx):
        emb = nextcord.Embed(title="**VDS - answer**", description="```VDS rebooted ```", color=nextcord.Color.gold())
        await ctx.send(embed=emb)
        os.system("sudo reboot")

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def ds_restart(self, ctx):
        emb = nextcord.Embed(title="**DS bot - answerv**", description="```Bot restarted```", color=nextcord.Color.gold())
        await ctx.send(embed=emb)
        os.system("pm2 restart 4")

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def ds_stop(self, ctx):
        emb = nextcord.Embed(title="**DS bot - answer**", description="```Bot stoped```", color=nextcord.Color.gold())
        await ctx.send(embed=emb)
        os.system("pm2 stop 4")














async def setup(bot):
    bot.add_cog(System(bot))
