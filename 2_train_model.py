from numpy import array
from pickle import dump
from keras.preprocessing.text import Tokenizer
from keras.utils.vis_utils import plot_model
from keras.utils import to_categorical
from keras.models import Sequential
from keras.layers import Dense, LSTM, Embedding

from common_funcs import load_doc

# define the model
def train_model(vocab_size, seq_length):
    model = Sequential()
    model.add(Embedding(vocab_size, 50, input_length=seq_length))
    model.add(LSTM(100, return_sequences=True))
    model.add(LSTM(100))
    model.add(Dense(100, activation='relu'))
    model.add(Dense(vocab_size, activation='softmax'))
    # compile network
    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
    # summarize defined model
    # model.summary()
    return model

# load sequences
print("Load sequences file you saved earlier: \n")
in_filename = str(input())
doc = load_doc(in_filename)
lines = doc.split('\n')

# integer encode sequences of words
tokenizer = Tokenizer()
tokenizer.fit_on_texts(lines)
sequences = tokenizer.texts_to_sequences(lines)

# vocabulary size
vocab_size = len(tokenizer.word_index) + 1     

# separate into input and output
sequences = array(sequences)
X, y = sequences[:, :-1], sequences[:,-1]
y = to_categorical(y, num_classes=vocab_size)
seq_length = X.shape[1]

# define model
model = train_model(vocab_size, seq_length)
# fit model
model.fit(X, y, batch_size=128, epochs=100)
# save the model to file
print("Save trained model to a file. Ensure it ends with .h5 \n Input your model name:\n")
model_name = str(input())
model.save(model_name)

print("Save tokenizer you used to train the model. Ensure it ends with .pkl \n Input your tokenizer name:\n")
tokenizer_name = str(input())
dump(tokenizer, open(tokenizer_name), 'wb')
