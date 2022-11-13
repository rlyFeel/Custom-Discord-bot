import nextcord
from nextcord.ext import commands


class Voice(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        print('Cogs is loaded - Voice')


    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        def check(x, y, z):
            return len(channel.members) == 0

        for guild in self.bot.guilds:
            if after.channel != None:
                if after.channel.id == 1036989467195613184:
                        channel = await guild.create_voice_channel(name=f'Канал {member.display_name}',
                                                                   category=nextcord.utils.get(guild.categories,
                                                                                               id=1036989082510835792))
                        await channel.set_permissions(member,
                                                      connect=True)
                        await member.move_to(channel)

                        await self.bot.wait_for('voice_state_update', check=check)
                        await channel.delete()

                elif after.channel.id == 1037010877913759795:
                        channel = await guild.create_voice_channel(name=f'Канал {member.display_name}',
                                                                   category=nextcord.utils.get(guild.categories,
                                                                                               id=1037009759825567865))
                        await channel.set_permissions(member,
                                                      connect=True)
                        await member.move_to(channel)

                        await self.bot.wait_for('voice_state_update', check=check)
                        await channel.delete()

                elif after.channel.id == 1037013128862511104:
                        channel = await guild.create_voice_channel(name=f'Канал {member.display_name}',
                                                                   category=nextcord.utils.get(guild.categories,
                                                                                               id=1037012148506873896))
                        await channel.set_permissions(member,
                                                      connect=True)
                        await member.move_to(channel)
                        await self.bot.wait_for('voice_state_update', check=check)

                        await channel.delete()

async def setup(bot):
    bot.add_cog(Voice(bot))