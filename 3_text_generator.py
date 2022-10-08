from random import randint
from pickle import load
from keras.models import load_model
from keras_preprocessing.sequence import pad_sequences

from common_funcs import load_doc

# generate a sequence from a language model
def generate_seq(model, tokenizer, seq_length, seed_text, n_words):
    result = list()
    in_text = seed_text
    # generate a fixed number of words
    for _ in range(n_words):
        # encode the text as integer
        encoded = tokenizer.texts_to_sequences([in_text])[0]
        # truncate sequences to a fixed length
        encoded = pad_sequences([encoded], maxlen=seq_length, truncating='pre')
        # predict probabilities for each word.
        yhat = model.predict_classes(encoded, verbose=0)
        # map predicted word index to word
        out_word = ''
        for word, index in tokenizer.word_index.items():
            if index == yhat:
                out_word = word
                break
        # append to input
        in_text += ' ' + out_word
        result.append(out_word)
    return ' '.join(result)

# load cleaned text sequences
print("Load sequence file you used to train model: \n")
in_filename = str(input())
doc = load_doc(in_filename)
lines = doc.split('\n')
seq_length = len(lines[0].split()) - 1

# load model
print("Load the trained model you saved: \n")
model_name = str(input())
model = load_model(model_name)

# load the tokenizer
print("Load the tokenizer you used to train model: \n")
tokenizer_name = str(input())
tokenizer = load(open(tokenizer_name), 'rb')

# select a seed text
seed_text = lines[randint(0, len(lines))]
print(f"This is the seed text: {seed_text}")

# Generate new text
print("Generating 50 texts from the seed text provided... \n\n")

generated = generate_seq(model, tokenizer, seq_length, seed_text, 50)
print(generated)