import os
import sys

from config import (
    X1, X2, X3, X4, X5,
    X6, X7, X8, X9, X10,
    OWNER_ID, SUDO_USERS,
    CMD_HNDLR as hl
)

from os import execl, getenv
from telethon import events
from datetime import datetime


@X1.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@X2.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@X3.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@X4.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@X5.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@X6.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@X7.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@X8.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@X9.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@X10.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
async def ping(e):
    if e.sender_id in SUDO_USERS:
        start = datetime.now()
        altron = await e.reply(f"•[ 🍹ᴇᴘsᴛᴇɪɴ тум 🍹 ]•")
        end = datetime.now()
        mp = (end - start).microseconds / 1000
        await altron.edit(f"[🍹] 𝐄ᴘsᴛᴇɪɴ ᴘαᴘα ɪѕ нєʀє\n[🏓] αвє αв тєʀα куα нσgα\n[⚡] кιѕкι ᴄнυ∂αι кαʀиι нαι\n\n➜ `{mp} ms`")


@X1.on(events.NewMessage(incoming=True, pattern=r"\%sreboot(?: |$)(.*)" % hl))
@X2.on(events.NewMessage(incoming=True, pattern=r"\%sreboot(?: |$)(.*)" % hl))
@X3.on(events.NewMessage(incoming=True, pattern=r"\%sreboot(?: |$)(.*)" % hl))
@X4.on(events.NewMessage(incoming=True, pattern=r"\%sreboot(?: |$)(.*)" % hl))
@X5.on(events.NewMessage(incoming=True, pattern=r"\%sreboot(?: |$)(.*)" % hl))
@X6.on(events.NewMessage(incoming=True, pattern=r"\%sreboot(?: |$)(.*)" % hl))
@X7.on(events.NewMessage(incoming=True, pattern=r"\%sreboot(?: |$)(.*)" % hl))
@X8.on(events.NewMessage(incoming=True, pattern=r"\%sreboot(?: |$)(.*)" % hl))
@X9.on(events.NewMessage(incoming=True, pattern=r"\%sreboot(?: |$)(.*)" % hl))
@X10.on(events.NewMessage(incoming=True, pattern=r"\%sreboot(?: |$)(.*)" % hl))
async def restart(e):
    if e.sender_id in SUDO_USERS:
        await e.reply(f"ʀєвσσт ᴅσиє\n[🍷] 2 мιит ωαιт ᴘℓєαѕє\n[🫧] fιʀ ααʏєɢα тєʀɪ мᴀᴀ ᴄнσᴅиє ᴇᴘsᴛᴇɪɴ ʙᴀʙʏ ")
        try:
            await X1.disconnect()
        except Exception:
            pass
        try:
            await X2.disconnect()
        except Exception:
            pass
        try:
            await X3.disconnect()
        except Exception:
            pass
        try:
            await X4.disconnect()
        except Exception:
            pass
        try:
            await X5.disconnect()
        except Exception:
            pass
        try:
            await X6.disconnect()
        except Exception:
            pass
        try:
            await X7.disconnect()
        except Exception:
            pass
        try:
            await X8.disconnect()
        except Exception:
            pass
        try:
            await X9.disconnect()
        except Exception:
            pass
        try:
            await X10.disconnect()
        except Exception:
            pass

        execl(sys.executable, sys.executable, *sys.argv)


@X1.on(events.NewMessage(incoming=True, pattern=r"\%ssudo(?: |$)(.*)" % hl))
@X2.on(events.NewMessage(incoming=True, pattern=r"\%ssudo(?: |$)(.*)" % hl))
@X3.on(events.NewMessage(incoming=True, pattern=r"\%ssudo(?: |$)(.*)" % hl))
@X4.on(events.NewMessage(incoming=True, pattern=r"\%ssudo(?: |$)(.*)" % hl))
@X5.on(events.NewMessage(incoming=True, pattern=r"\%ssudo(?: |$)(.*)" % hl))
@X6.on(events.NewMessage(incoming=True, pattern=r"\%ssudo(?: |$)(.*)" % hl))
@X7.on(events.NewMessage(incoming=True, pattern=r"\%ssudo(?: |$)(.*)" % hl))
@X8.on(events.NewMessage(incoming=True, pattern=r"\%ssudo(?: |$)(.*)" % hl))
@X9.on(events.NewMessage(incoming=True, pattern=r"\%ssudo(?: |$)(.*)" % hl))
@X10.on(events.NewMessage(incoming=True, pattern=r"\%ssudo(?: |$)(.*)" % hl))
async def addsudo(event):
    if event.sender_id != OWNER_ID:
        return await event.reply(
            "» ꜱᴏʀʀʏ, ᴏɴʟʏ ᴏᴡɴᴇʀ ᴄᴀɴ ᴀᴄᴄᴇꜱꜱ ᴛʜɪꜱ ᴄᴏᴍᴍᴀɴᴅ."
        )

    ok = await event.reply("Adding sudo user...")

    try:
        reply_msg = await event.get_reply_message()
        target = str(reply_msg.sender_id)
    except:
        return await ok.edit(
            "Reply to a user's message to add them as sudo."
        )

    sudo_file = "sudo_users.txt"

    if not os.path.exists(sudo_file):
        open(sudo_file, "w").close()

    with open(sudo_file, "r") as f:
        users = [x.strip() for x in f.readlines() if x.strip()]

    if target in users:
        return await ok.edit("This user is already a sudo user!")

    with open(sudo_file, "a") as f:
        f.write(target + "\n")

    SUDO_USERS.append(int(target))

    await ok.edit(
        f"Added sudo user:\n`{target}`"
    )
