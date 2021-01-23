import discord
from server.keep_alive import keep_alive
import src.chatbot as chatbot
import os

def main():
  bot = chatbot.build_bot()
  client = discord.Client()

  chatbot.train_bot(bot)

  @client.event
  async def on_ready():
    print("Logado como usuário {0.user}".format(client))

  @client.event
  async def on_message(message):
    if message.author == client.user:
      return

    msg = message.content

    if msg.startswith("$"):
      await message.channel.send(bot.get_response(msg))

  keep_alive()
  client.run(os.getenv("TOKEN"))

if __name__ == "__main__":
  main()

