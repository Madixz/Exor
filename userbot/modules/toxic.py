from userbot import CMD_HELP, bot
from telethon import events
import asyncio

# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


@register(outgoing=True, pattern="^.sa(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**Shalom Aleichem**")


@register(outgoing=True, pattern="^.as(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**Aleichem Shalom**")


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
    "`.sa` ; `.as`\
    \nUsage: Salam Shalom.\
    \n\n`.sinick1`\
    \nUsage: Pengen.\
    \n\n`.sinick2`\
    \nUsage: Sange`"
})
