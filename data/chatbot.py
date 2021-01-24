from data.model import Model as model
import nltk
from nltk.data import load
from nltk import TreebankWordTokenizer
import pickle
import numpy as np 
from keras.models import load_model
import json
import random
import src.utils as u 

class Chatbot:
  def __init__(self):
    self.chatbot = model()
    self._lemmatizer = nltk.stem.WordNetLemmatizer()
    self._model = load_model(r"src/model.h5", compile = False)
    self._intents = self.chatbot.get_intents()
    self._words = u.load_pickle(r"pickles/words.pkl")
    self._classes = u.load_pickle(r"pickles/classes.pkl")

  def clean_up_sentence(self, sentence):
    # Tokenizando o padrão e dividindo palavras em arrays
    tokenizer = load("file:portuguese.pickle")

    sentence_words = tokenizer.tokenize(sentence)
    # Criando uma forma reduzida da palavra
    sentence_words = [self._lemmatizer.lemmatize(word.lower()) for word in sentence_words]

    return sentence_words

  # Retorna um array de bag of words (0 ou 1 para cada palavra que existe na sentença)
  def bow(self, sentence, words):
    # Tokenizando o padrão
    sentence_words = self.clean_up_sentence(sentence)
    # Bag of words (matriz de N palavras, ou matriz de vocabulário)
    bag = [0] * len(words)

    for s in sentence_words:
      for i, w in enumerate(words):
        if w == s:
          # Atribui 1 se a palavra atual está na posição do vocabulário
          bag[i] = 1

    return (np.array(bag))

  def predict_class(self, sentence, model):
    error_threshold = 0.25
    # Filtrando as predições inferiores ao threshold
    p = self.bow(sentence, self._words)
    res = self._model.predict(np.array([p]))[0]

    results = [[i, r] for i, r in enumerate(res) if r > error_threshold]

    # Organizar pela probabilidade
    results.sort(key = lambda x: x[1], reverse = True)

    return_list = []

    for r in results:
      return_list.append({"intent": self._classes[r[0]], "probability" : str(r[1])})

    return return_list
 
  def get_response(self, ints, intents_json):
    tag = ints[0]["intent"]
    list_of_intents = intents_json["intents"]
    result = ""

    for i in list_of_intents:
      if(i["tag"] == tag):
        result = random.choice(i["responses"])

        break

      else:
        pass

    return result

  def chatbot_response(self, text):
    ints = self.predict_class(text, self._model)
    res = self.get_response(ints, self._intents)

    return res
