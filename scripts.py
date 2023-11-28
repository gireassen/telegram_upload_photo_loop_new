import asyncio
from telethon import TelegramClient
from telethon.tl.functions.photos import UploadProfilePhotoRequest, DeletePhotosRequest
import os
import time
api_id = '123'
api_hash = '123'
path_to_drew = 'D:\\Python_scrypts\\telegram_head_drew\\time_images'
client = TelegramClient("carpediem", api_id, api_hash)
client.start() 
async def main():
    while True:
        for file in os.listdir(path_to_drew):
            await client(DeletePhotosRequest(await client.get_profile_photos('me')))
            await client(UploadProfilePhotoRequest(await client.upload_file(path_to_drew+'\\'+file)))
            time.sleep(60)
if __name__ == '__main__':
    import asyncio
    asyncio.get_event_loop().run_until_complete(main())
