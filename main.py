import discord
import tweepy
from discord.ext import tasks
from SECRET import *

links = []
accounts = ["1324458539214020609", "32771325"]


class MyStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        print(status.user.screen_name)
        user_id = status.user.id_str
        if user_id in accounts and not status.favorited:
            links.append("https://twitter.com/i/web/status/" + status.id_str)
            print("https://twitter.com/i/web/status/" + status.id_str)


client = discord.Client()

# auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
# auth.set_access_token(
#     ACCESS_TOKEN, ACCESS_SECRET,
# )
# api = tweepy.API(auth)
# # print(api.get_user(1324458539214020609))python
# myStreamListener = MyStreamListener()
# myStream = tweepy.Stream(auth=api.auth, listener=myStreamListener)
# myStream.filter(follow=accounts)
# myStream.sample(languages=["en"])


# @client.event
# async def on_ready():
#     print(f"We have logged in as {client.user}")
#     new_tweets.start()


# @client.event
# async def on_message(message):

#     if message.author == client.user:
#         return

#     # Defining Keywords for bot to respond to
#     unlucky_data = ["unlucky", "unluck"]
#     for word in unlucky_data:
#         if word in message.content.lower():
#             await message.channel.send(file=discord.File("unlucky_steel.jpg"))
#             return

#     lucky_data = ["lucky", "luck"]
#     for word_2 in lucky_data:
#         if word_2 in message.content.lower():
#             await message.channel.send(file=discord.File("lucky_steel.jpg"))
#             return
#     # Command for bot
#     if message.content.startswith("!unlucky"):
#         await message.channel.send(file=discord.File("unlucky_steel.jpg"))
#         return


# @tasks.loop(minutes=1.0)
# async def new_tweets():
#     print("YEP")
#     if links:
#         general = client.get_channel(820522358874832926)
#         for link in links:
#             await general.send(link)
#             links.pop()


client.run(BOT_TOKEN)
