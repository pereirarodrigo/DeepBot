from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

def build_bot():
  bot = ChatBot(
                "Gradient",
                storage_adapter='chatterbot.storage.SQLStorageAdapter',
                logic_adapters = [
                  'chatterbot.logic.MathematicalEvaluation',
                  'chatterbot.logic.TimeLogicAdapter',
                  'chatterbot.logic.BestMatch'
                ],
                database_uri='sqlite:///database.db'
            )

  return bot

def train_bot(chatbot):
  chatbot.set_trainer(ChatterBotCorpusTrainer)

  chatbot.train(
     "chatterbot.corpus.portuguese"
  )