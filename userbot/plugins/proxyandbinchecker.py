import datetime
import asyncio
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError, UserAlreadyParticipantError
from telethon.tl.functions.account import UpdateNotifySettingsRequest
from telethon.tl.functions.messages import ImportChatInviteRequest
from userbot.utils import admin_cmd
import time
from userbot import ALIVE_NAME

name = str(ALIVE_NAME)

bot = "@CasperCarderBot"


@borg.on(admin_cmd("proxy ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    sysarg = event.pattern_match.group(1)
    
    if "." in sysarg :
     async with borg.conversation(bot) as conv:
          try:
              await conv.send_message("/start")
              await event.delete()
              response = await conv.get_response()
              await conv.send_message("!proxy " + sysarg)
              audio = await conv.get_response()
              await borg.send_message(event.chat_id, audio.text)
          except YouBlockedUserError:
              await event.edit("**Error:** `unblock` @CasperCarderBot `and retry!")
     if "x" not in sysarg:
      async with borg.conversation(bot) as conv:
          try:
              await conv.send_message("/start")
              await event.delete()
              response = await conv.get_response()
              await conv.send_message("!proxy ")
              audio = await conv.get_response()
              await borg.send_message(event.chat_id, audio.text)
          except YouBlockedUserError:
              await event.edit("**Error:** `unblock` @CasperCarderBot `and retry!!")
@borg.on(admin_cmd("bin ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    sysarg = event.pattern_match.group(1)

     if "x" not in sysarg:
      async with borg.conversation(bot) as conv:
          try:
              await conv.send_message("/start")
              await event.delete()
              response = await conv.get_response()
              await conv.send_message("!bin " + sysarg)
              audio = await conv.get_response()
              await borg.send_message(event.chat_id, audio.text)
          except YouBlockedUserError:
              await event.edit("**Error:** `unblock` @CasperCarderBot `and retry!")



