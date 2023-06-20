import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='/')

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} ({bot.user.id})')

@bot.command()
@commands.has_permissions(administrator=True)
async def freeze(ctx):
    owner = ctx.guild.owner
    frozen_role = discord.utils.get(ctx.guild.roles, name='Frozen')

    for member in ctx.guild.members:
        if member != owner:
            await member.remove_roles(*member.roles)
            await member.add_roles(frozen_role)

    await ctx.send('Everyone has been frozen.')

bot.run('YOUR_BOT_TOKEN')

