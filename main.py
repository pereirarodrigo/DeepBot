from discord.ext import commands
from server.keep_alive import keep_alive
from data.chatbot import Chatbot as chatbot
import os

def main():
  bot = commands.Bot(command_prefix = '$')

  @bot.event
  async def on_ready():
    print("Logado como usuário {0.user}".format(bot))

  @bot.command()
  async def talk(ctx, message):
    if message != "":
      await ctx.send(chatbot().chatbot_response(message))

  keep_alive()
  bot.run(os.getenv("TOKEN"))

if __name__ == "__main__":
  main()

