import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import string

def generate_tokens(txt: str) -> list:
    """
    Processes a string and returns a list of tokens.
    :param txt: The string to process.
    :return: A list of tokens.
    """
    stop_words = stopwords.words('english') + list(string.punctuation)
    stemmer = PorterStemmer()
    tokens = [stemmer.stem(word.lower()) for word in nltk.word_tokenize(txt) \
                                                if word.lower() not in stop_words and word.isalpha()]
    return tokens

def create_revert_index(tokens: list) -> dict:
    """
    Creates a reverse index of the tokens.
    :param tokens: A list of tokens.
    :return: A dictionary of tokens.
    """
    revent_index = {}
    for index, token in enumerate(tokens):
        if token not in revent_index:
            revent_index[token] = {
                'repeat': 1,
                'indexes': [
                    index # this is not actually the index of token in tokens, 
                                        # this must be set to token index in orginal string???
                ]
            }
        else:
            revent_index[token]['repeat'] += 1
            revent_index[token]['indexes'].append(index)

    return revent_index