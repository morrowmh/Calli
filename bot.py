import discord

intents = discord.Intents.default()
intents.presences = True
intents.message_content = True
intents.members = True


def main() -> None: ...


if __name__ == '__main__':
    main()
