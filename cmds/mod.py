import discord
from discord.ext import commands
from core.classes import Cog_Extension, Global_Func
import json

with open('setting.json', 'r', encoding='utf8') as jfile:
   jdata = json.load(jfile)

class Mod(Cog_Extension):
  @commands.command()
  @commands.has_permissions(ban_members = True)
  async def ban(ctx, member : discord.Member, *, reason = None):
      await member.ban(reason = reason)

  @commands.command()
  @commands.has_permissions(kick_members=True)
  async def kick(ctx, member: discord.Member, *, reason=None):
    if reason==None:
      reason="No Reason Provided"
    await ctx.guild.kick(member)
    await ctx.send(f'User {member.mention} has been kicked for {reason}')

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def unban(ctx, *, member):
      banned_users = await ctx.guild.bans()
      member_name, member_discriminator = member.split("#")

      for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'Unbanned {user.mention}')
            return

    @commands.command(aliases=['cc'])
    @commands.has_permissions(administrator=True)
    async def purge(self, ctx, num: int, reason=None):
        '''清理指定數量訊息'''
        await ctx.channel.purge(limit=num + 1)
        
        levels = {
            "a": "非對應頻道內容",
            "b": "不雅用詞"
        }

        if reason is not None:
            if reason in levels.keys():
                await ctx.send(Global_Func.code(lang='fix', msg=f'已清理 {num} 則訊息.\nReason: {levels[reason]}'))
        else:
            await ctx.send(content=Global_Func.code(lang='fix', msg=f'已清理 {num} 則訊息.\nReason: {reason}'), delete_after=5.0)


def setup(bot):
   bot.add_cog(Mod(bot))