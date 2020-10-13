
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


def move_author_to_channel(ctx, channel):
    author = ctx.author
    return author.move_to(channel)
