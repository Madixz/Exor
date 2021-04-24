from time import sleep
from platform import uname
from userbot import ALIVE_NAME, CMD_HELP
from userbot.events import register

# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


@register(outgoing=True, pattern="^.p(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**Assalamualaikum Dulu Biar Sopan**")


@register(outgoing=True, pattern=r"^\.pe(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**Assalamualaikum Warahmatullahi Wabarakatuh**")


@register(outgoing=True, pattern="^.P(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit(f"**Haii Salken Saya {DEFAULTUSER}**")
    sleep(2)
    await typew.edit("**Assalamualaikum...**")


@register(outgoing=True, pattern=r"^\.l(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**Wa'alaikumsalam**")


@register(outgoing=True, pattern=r"^\.sa(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**Shalom Aleichem**")


@register(outgoing=True, pattern="^.SA(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit(f"**Haii Salken Saya {DEFAULTUSER}**")
    sleep(2)
    await typew.edit("**Shalom Aleichem**")


@register(outgoing=True, pattern=r"^\.as(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**Aleichem Shalom**")


CMD_HELP.update({
    "salam":
    "`.p`\
\nUsage: Assalamualaikum Dulu Biar Sopan.\
\n\n`.pe`\
\nUsage: Salam Panjang Dan Lengkap.\
\n\n`.P`\
\nUsage: Salam Kenal Dan Salam.\
\n\n`.l`\
\nUsage: Untuk Menjawab Salam.\
\n\n`.sa`\
\nUsage: Salam Shalom.\
\n\n`.SA`\
\nUsage: Salam Kenal Dan Salam Shalom.\
\n\n`.as`\
\nUsage: Untuk Menjawab Salam."
})
