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


@bot.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))
async def _(event):

    if event.fwd_from:

        return

    animation_interval = 3

    animation_ttl = range(0, 103)

    input_str = event.pattern_match.group(1)

    if input_str == "sinick3":

        await event.edit(input_str)

        animation_chars = [
            "`Teruntuk Kamu` ",
            " Hay Cantik, Sudah Lama ",
            " Perasaan Ini Ku SembunyiKan ",
            " Tapi Sekarang ",
            " Aku Tak Dapat Menampung Semuanya ",
            " Semakin Aku Diam, Semakin Aku Gelisah ",
            " Hati Ini Menginginkan Dirimu ",
            " Mau Kah Kamu Menjadi PendampingKu?",
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

    if input_str == "sinick4":

        await event.edit(input_str)

        animation_chars = [
            "`KataCinta` ",
            " Lebih baik dibenci apa adanya dirimu daripada dicintai karena bukan dirimu ",
            " Cinta sejati memandang kelemahan lalu dijadikan kelebihan untuk selalu mencintai ",
            " Merelakan, melepaskan bukan sekadar mengurai ikatan. Tetap akan ada sisa yang tertinggal. Selesaikan dan mulailah yang baru. ",
            " Cinta adalah kondisi di mana kebahagiaan orang lain sangat penting untukmu sendiri ",
            " Aku mencintaimu karena hal-hal gelap tertentu harus dicintai, secara rahasia, antara bayangan dan jiwa ",
        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 103])



CMD_HELP.update({
    "toxic":
    "`.sinick1`\
    \nUsage: pengen.\
    \n\n`.sinick2`\
    \nUsage: sange."
})
