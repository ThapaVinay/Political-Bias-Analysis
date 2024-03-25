import json 
from joblib import load
import numpy as np

import spacy
nlp = spacy.load("en_core_web_lg")

__model = None

# for preprocessing
def preprocess(text):
    doc = nlp(text)

    filtered_tokens = []

    for token in doc:
        if token.is_stop or token.is_punct:
            continue
        filtered_tokens.append(token.lemma_)
    
    return " ".join(filtered_tokens)

# vectorise
def vectorize(text):
    return text.vector

# for finding the bias
def get_bias(text):
    clean_text = preprocess(text)
    embeddings = vectorize(clean_text)
    
    return __model.predict(embeddings)[0]

# for loading the model
def load_saved_model():
    global __model
    
    with open("model.joblib", "rb") as f:
        __model = load(f)


# main function
if __name__ == "__main__":
    load_saved_model()
