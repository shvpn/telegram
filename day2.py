from telethon import TelegramClient, events, sync
import tiktok as mytiktok
import os
import re
import time

class TelegramBot:
    def __init__(self, api_id, api_hash, bot_token, user_id):
        self.api_id = api_id
        self.api_hash = api_hash
        self.bot_token = bot_token
        self.user_id = user_id
        self.client = TelegramClient('bot_session', self.api_id, self.api_hash).start(bot_token=self.bot_token)
    
    def start(self):
        self.client.run_until_disconnected()

    def add_event_handler(self, event_handler, event_type):
        self.client.add_event_handler(event_handler, event_type)
    
    def get_all_links(self, message):
        return re.findall(r'(https?://[^\s]+)', message)
    def append_log(self, message):
        with open("log.txt", "a") as f:
            f.write(f"{message}\n") 
        

    async def reply_video(self, event):
        sender = await event.get_sender()
        
        # Skip bot messages or empty chats
        if sender.bot or event.is_channel:
            return

        # Get the message from the user
        message = event.text
        print(f"Received message: {message}")
        try:
            if 'tiktok' in message: 
                # Get all links from the message
                links = self.get_all_links(message)
                # Download the video
                await event.reply("Downloading video...")
                mytiktok.download_tiktok_video(links)
                
                # Send the video to the user
                await event.reply(file="output.mp4")
                print(f"Sent video to {sender.username or sender.id}")
            else:
                # Custom reply message
                reply_message = "I only accept TikTok video links."
                await event.reply(reply_message)

                # Reply to the user
        except Exception as e:
            print(f"Error: {e}")
            reply_message = "An error occurred. Please try again later."
            await event.reply(reply_message)
        finally:
            message1=f"""{sender.username or sender.id} sent: {message} at {time.ctime()}"""
            self.append_log(message1)
    

            
        
        





    async def auto_reply(self, event):
        sender = await event.get_sender()
        
        # Skip bot messages or empty chats
        if sender.bot or event.is_channel:
            return

        # Custom reply message
        reply_message = "Wait 15 minutes because I'm currently unavailable."
        
        # Reply to the user
        await event.reply(reply_message)
        print(f"Replied to {sender.username or sender.id} with: {reply_message}")
    

if __name__ == "__main__":
    # Replace with your API credentials
    api_id = 20702310
    api_hash = '9cfebed918ee36a0aea417c2c0be81c8'
    user_id = 'senghoutork'

    # Replace with your bot's token
    BOT_TOKEN = '7836984889:AAHhIPkTDIaXZTm3ZE2mH6MkTy44Fue6GNI'

    bot = TelegramBot(api_id, api_hash, BOT_TOKEN, user_id)
    
    # Add event handler for auto-reply
    bot.add_event_handler(bot.reply_video, events.NewMessage(incoming=True))
    
    print("Bot is running...")
    bot.start()

