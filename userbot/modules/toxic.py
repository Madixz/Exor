from userbot import CMD_HELP, bot
from telethon import events
import asyncio


@bot.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))
async def _(event):

    if event.fwd_from:

        return

    animation_interval = 3

    animation_ttl = range(0, 103)

    input_str = event.pattern_match.group(1)

    if input_str == "sinick1":

        await event.edit(input_str)

        animation_chars = [
            "`Sayang Pengen🥺` ",
            " Udah Kebelet ",
            " Pengen Ngewe ",
            " Ayangg Ayokkk ",
            " Ngeweee ",
        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 103])


@bot.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))
async def _(event):

    if event.fwd_from:

        return

    animation_interval = 3

    animation_ttl = range(0, 103)

    input_str = event.pattern_match.group(1)

    if input_str == "sinick2":

        await event.edit(input_str)

        animation_chars = [
            "`Masih Teringat` ",
            " Di Malam Itu Kita Bercumbu",
            " Di Bawah Sinar Rembulan ",
            " Engkau MencumbuiKu ",
            " Dengan Sangat Ganas ",
            " Kau Isap Kontol Ku ",
            " Dan Ku Jilat Memek Mu ",
            " Skip Nanti Lu Sange",
        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 103])

CMD_HELP.update({
    "toxic":
    "`.sinick1`\
    \nUsage: minta ngewe.\
    \n\n`.sinick2`\
    \nUsage: sangean`"
})