import discord

ACTIVITY_TYPE_MAP = {
    'playing': discord.ActivityType.playing,
    'watching': discord.ActivityType.watching,
    'streaming': discord.ActivityType.streaming,
    'competing': discord.ActivityType.competing,
    'listening': discord.ActivityType.listening,
}

STATUS_TYPE_MAP = {
    'dnd': discord.Status.dnd,
    'idle': discord.Status.idle,
    'online': discord.Status.online,
    'invisible': discord.Status.invisible,
    'offline': discord.Status.offline,
}


def make_activity(activity_type: str, activity_name: str) -> discord.Activity:
    activity = ACTIVITY_TYPE_MAP.get(activity_type, discord.ActivityType.playing)
    return discord.Activity(type=activity, name=activity_name)


def make_status(status_type: str) -> discord.Status:
    return STATUS_TYPE_MAP.get(status_type, discord.Status.dnd)
