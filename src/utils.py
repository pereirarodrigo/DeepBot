import pickle

# Arquivo usado para a criação de arquivos .pkl, para guardar os objetos que 
# serão utilizados no processo de predição

def create_pickle(lst, pkl_url):
  return pickle.dump(lst, open(pkl_url, "wb"))

def load_pickle(pkl_url):
  return pickle.load(open(pkl_url, "rb"))