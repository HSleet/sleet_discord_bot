
def mute_members(context):
    channel_requested = context.author.voice.channel
    all_channel_members = context.channel.members
    for i in range(len(all_channel_members)):
        if not all_channel_members[i].bot:
            if all_channel_members[i].voice is not None:
                if all_channel_members[i].voice.channel == channel_requested:
                    yield all_channel_members[i].edit(mute=True)


def unmute_members(context):
    channel_requested = context.author.voice.channel
    all_channel_members = context.channel.members
    for i in range(len(all_channel_members)):
        if not all_channel_members[i].bot:
            if all_channel_members[i].voice is not None:
                if all_channel_members[i].voice.channel == channel_requested:
                    yield all_channel_members[i].edit(mute=False)

async def pollo(ctx):
 user_request = ctx.author
 dst_channel = "la habitacion del pollo"
 
 lst = member.move_to(dst_channel)
 await asyncio.gather(*lst)
