Telegram will not allow you to scrape members from one channel to another, but here is another way to do that.
If you make someone an admin of your channel who was not a member of your channel's and if you remove his authority after some time, he will be just a member, so this means you just added one user without his permission.

This is a Telegram bot that collects usernames from some channels or groups provided, makes one user an admin, and removes their authority within 3 seconds of the interval. 
The process will continue until the bot has collected all users with usernames(Users without usernames and bots will be skipped in the process).

You can modify the code based on the comments provided.
Go to telegram.org to generate your api_id and api_hash, and copy and paste them into the code.
Replace the channels with your 3 channels' usernames, so  a user will pass from on channel to the other.
The telegram account running the bot must be a member or admin of those channels of those channels.
If you want to deploy the bot on Replit, just use the 3 files there will be no other process. 

But you can also deploy it on your computer by using only the main.py file, to do that:

1. Create a folder named telegram_admin_bot and put main.py inside it.
2. Download Python from python.org.
3. Open CMD in that folder, and install the libraries in your terminal. Copy the code below and paste it into CMD for Windows users
   
      *pip install pyrogram tgcrypto*
   
5. Run the program.
   
      *python main.py*
   
7. Press Enter, and this starts your bot.
   this will be processed in the background(you cannot access the bot in your telegram account)

   
