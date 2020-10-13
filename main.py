import os
from bot_functions import server_management
from discord.ext import commands
from discord.ext.commands import has_permissions

bot_token = os.getenv("BOT_TOKEN")

bot = commands.Bot(command_prefix="!")


@bot.command()
@has_permissions(administrator=True)
async def muteall(ctx):
    mute_list = server_management.mute_members(ctx)
    for mute_member in mute_list:
        await mute_member


@bot.command()
@has_permissions(administrator=True)
async def unmuteall(ctx):
    mute_list = server_management.unmute_members(ctx)
    for mute_member in mute_list:
        await mute_member


@bot.command()
async def pollo(ctx):
    la_habitacion_del_pollo = 764124563667681330
    dst_channel = bot.get_channel(la_habitacion_del_pollo)
    await ctx.message.delete()
    await server_management.move_author_to_channel(ctx, dst_channel)


@bot.command()
async def join(ctx):
    channel = ctx.author.voice.channel
    await ctx.message.delete()
    await channel.connect()


@bot.command()
async def leave(ctx):
    await ctx.voice_client.disconnect()

bot.run(bot_token)
