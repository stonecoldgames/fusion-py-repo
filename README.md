# fusion-py-repo
=====
## Summary
this is a repo for ross/daniel compprog class
https://www.devdungeon.com/content/make-discord-bot-python
Currently building a discord bot to moderate/improve/liven the fusion discord server, written in python.
Goal is to learn discord api and understand how to script a bot
```python
import discord
```
this was quite a problem, as we had trouble just installing python, and updating various deprecated packages, and the discord api is a pain to set up. There is very little easily accessible documentation for this api, which has made it that much more of a challenge.
The End result of this project should be a bot that moderates a channel with humor and plays some music maybe? 
devdungeon has some good starter scripts, such as one that allows you to greet the bot:
```python
if message.content.startswith('!hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
```

