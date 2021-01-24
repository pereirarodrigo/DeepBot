from discord.ext import commands
from server.keep_alive import keep_alive
import data.chatbot as cbot
import os

def main():
  bot = commands.Bot(command_prefix = commands.when_mentioned_or("$"))
  chatbot = cbot.build_bot()

  cbot.train_bot(chatbot)

  @bot.event
  async def on_ready():
    print("Logado como usuário {0.user}".format(bot))

  @bot.command(pass_context = True, aliases = ["b", "c"])
  async def talk(ctx, message):
    if message != "":
      await ctx.send(chatbot.get_response(message))

  keep_alive()
  bot.run(os.getenv("TOKEN"))

if __name__ == "__main__":
  main()

