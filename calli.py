import tomllib
from pathlib import Path
from typing import Any

import discord
from discord import Interaction
from discord.ext import commands

from utils.presence import make_activity, make_status

PREFIX = '!'  # Ignored when using slash commands

BOT_CONFIG_PATH = Path('config/bot.toml')
SPEECH_CONFIG_PATH = Path('config/speech.toml')


def load_toml(path: Path) -> dict[str, Any]:
    with open(path, 'rb') as f:
        return tomllib.load(f)


### --- Initialize Calli --- ###

bot_config = load_toml(BOT_CONFIG_PATH)
speech_config = load_toml(SPEECH_CONFIG_PATH)

bot_intents = bot_config['intents']
intents = discord.Intents.default()
intents.presences = bot_intents['presences']
intents.message_content = bot_intents['message_content']
intents.members = bot_intents['members']

guild = discord.Object(id=bot_config['bot']['guild_id'])
calli = commands.Bot(PREFIX, intents=intents)


### --- Events --- ###


@calli.event
async def on_ready() -> None:
    await calli.wait_until_ready()

    print(f'Ready! Logged in as {calli.user}')

    synced = await calli.tree.sync(guild=guild)
    print(f'Synced {len(synced)} commands to guild_id={guild.id}')

    bot_presence = bot_config['presence']
    activity = make_activity(bot_presence['activity']['type'], bot_presence['activity']['name'])
    status = make_status(bot_presence['status']['type'])

    await calli.change_presence(activity=activity, status=status)


### --- Commands --- ###


@calli.tree.command(name='calli', description='Information about Calli', guild=guild)
async def calli_help(interaction: Interaction) -> None:
    await interaction.response.send_message("Hi, I'm Calli! Soon, help will go here.")


### --- Run Calli --- ###

calli.run(bot_config['bot']['token'])
