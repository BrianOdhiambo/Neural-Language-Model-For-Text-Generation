# Neural Language Model for Text Generation.
In this sample text generation project: we develop a model of the text then use it to generate new sequences of text.
The language model is statistical and will predict the probability of each word given an input sequence of text.

## Key Design Decision
-> Length of input sequence should be long enough to allow the model to learn  the context for the words to predict. The input length also defines the length of seed text used to generate new sequences.
-> For our model, we pick a length of 50 words  for the length of the input sequences.
-> We transform  raw text into sequences of 100 input words to 1 output word, ready to fit a model.

## Data source 
The text data used to train our model is the famous Republic book by  Greek philosopher Plato. You can download the text from [Project Gutenberg website](http://www.gutenberg.org/cache/epub/1497/pg1497.txt).
This data is in the `republic_cleant.txt` file. <br>
NB: You can use any text data of your choice. Be sure to modify the text cleaning code to fit your case, although the text cleaning code fits most raw data.

## Data Preparation
### Clean Text
We need to transform the raw text into a sequence of tokens or words that will be used to train the model.
* Replace '-' with a white space so we can split words better.
* Split words based on white space.
* Remove all punctuations from words to reduce the vocabulary size (e.g. "What?" becomes "What").
* REmoce all words that are not alphabetic to remoce standalone punctuation tokens.
* Normalize all words to lowercase to reduce the vocabulary size.

## Training Language Model
The model we train is a neural language model. It has a few unique characteristics:
* It uses a distributed representation for words so that different words with similar meanings will have a similar representation.
* It leans the representation at the same time as learning the model.
* It learns to predict the probability for the next word using the context of the last 100 words.

We use:
-> An Embedding Layer to learn the representation of words.
-> Long Short-Term Memory (LSTM) recurrent neural network to learn to predict words based on their context.

To run all the code in order run:
`sh run.sh`