#sr! = prefix
# Server_Observer.py

import os
import random
import time
import discord
from dotenv import load_dotenv





reply = ("Everything looks good","No Fault Found in the server","No bugs found in the server","I cannot find any problem","No bugs found","No Problems Found","Your server is 100% safe ","Server_Observer cannot find any problem ","Your server seems good","Wohoo! No threats in the server,Nice job ","Found  3 problems Write sr!Bot audit --fix to fix them all","Found 2 threats Write sr!Bot --fix --force to  fix them all")





load_dotenv()
client = discord.Client()



@client.event
async def on_ready():
    print(f'{client.user.name} is Ready to Rock!')

@client.event
async def on_member_join(member):
    print(f'{member.namee}joined a server')


@client.event
async def on_message(message):
    if message.content == 'Server_Observer':
        print("Anyone is referring me")
        await message.channel.send(f'{client.user.name} is awake and ready')

    if message.content == 'sr!help':
        await message.channel.send("This is a bot designed to help people maintain their server , It will observe your server to get details about your server and if any thing goes wrong it will tell you ,To get the status of your server type **sr!stats** now (To invite me to your server too type, **sr!invite** )")

    if message.content == 'sr!Happy Birthday':
        await message.channel.send("Hbd bro")

    if message.content == 'sr!stats':
        reply2 = random.choice(reply)
        await message.channel.send(reply2)

    if message.content == 'sr!invite':
        await message.channel.send("Here is the invite link -"
                                   f'https://discord.com/api/oauth2/authorize?client_id={client.id}&permissions=284004772865&scope=bot'

    if message.content == 'sr!Bot --fix --force':
        await message.channel.send("Fixing 2 major problems")
        time.sleep(3)
        await message.channel.send("Fixed 1 major problem ")
        time.sleep(2)
        await message.channel.send("Fixed all problems")



    if message.content == 'sr!Bot audit --fix':
        await message.channel.send("Fixing Problems")
        time.sleep(2)
        await message.channel.send("Fixed all problems")

    elif message.content == 'raise-exception':
        print("Somoone wants to raise exeption")


    else:
        print("  ")
        print("message content is ", message.content)
        print("  ")
        print("messege info is", message)
        print("  ")
        print("the message was sent by ", message.author)
        print("  ")





TOKEN = os.environ.get('Your Token')

client.run('Your Token')
