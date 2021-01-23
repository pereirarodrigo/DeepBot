from chatterbot import ChatBot
#from chatterbot.trainers import ListTrainer
#from corpus import introductions, questions, affirmations
from chatterbot.trainers import ChatterBotCorpusTrainer

def build_bot():
  bot = ChatBot(name = "DeepBot", 
              read_only = True, 
              logic_adapters = ["chatterbot.logic.BestMatch"],
              silence_performance_warning = True
              )

  return bot

def train_bot(bot):
  bot.set_trainer(ChatterBotCorpusTrainer)
  bot.train("chatterbot.corpus.portuguese")

  #list_trainer = ListTrainer(bot)

  #for item in (introductions, questions, affirmations):
    #list_trainer.train(item)  

  