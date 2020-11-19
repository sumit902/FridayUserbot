import requests
from telethon.errors import (
    BadRequestError,
    ChatAdminRequiredError,
    ImageProcessFailedError,
    PhotoCropSizeSmallError,
    UserAdminInvalidError,
)
from telethon.errors.rpcerrorlist import MessageTooLongError, UserIdInvalidError
from telethon.tl.functions.channels import (
    EditAdminRequest,
    EditBannedRequest,
    EditPhotoRequest,
)
from telethon.tl.functions.messages import UpdatePinnedMessageRequest
from telethon.tl.types import (
    ChannelParticipantsAdmins,
    ChatAdminRights,
    ChatBannedRights,
    MessageEntityMentionName,
    MessageMediaPhoto,
)

from fridaybot.utils import friday_on_cmd, sudo_cmd


@friday.on(friday_on_cmd(pattern=r"nsfw"))
@friday.on(sudo_cmd(pattern=r"nsfw", allow_sudo=True))
async def nsfw(event):
    url = "https://nsfw-categorize.it/api/upload"
    replymsg = await event.get_reply_message()
    photo = None
    if replymsg and replymsg.media:
        if isinstance(replymsg.media, MessageMediaPhoto):
            photo = await borg.download_media(message=replymsg.photo)
        elif "image" in replymsg.media.document.mime_type.split("/"):
            photo = await borg.download_file(replymsg.media.document)
        else:
            await event.edit("`Reply To Image`")
    if photo:
        files = {"image": (f"{photo}", open(f"{photo}", "rb"))}
        r = requests.post(url, files=files).json()
        if r["status"] == "OK":
            await event.edit(
                "This image is classified as " + str(r["data"]["classification"])
            )
        else:
            await event.edit("Response UnsucessFull. Try Again.")
