import discord

TOKEN = 'NDc4NjkwOTYxMTIwMTY1OTAw.DlO19g.Rv1qZa5Ws-tTWO21Q_dJ-W2BAHA'

client = discord.Client()

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
    if message.content.startswith('!users'):
        
        #for member in msg:
            #await client.send_message(message.channel, msg)
        for server in client.servers:
            for member in server.members:
                yield member
    if message.content.startswith('!quit'):
        client.logout()


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)