import string
import re

from common_funcs import load_doc

# turn a doc into clean tokens
def clean_doc(doc):
    # replace '--' with a space ' '
    doc = doc.replace('--', ' ')
    # split into tokens by white space
    tokens = doc.split()
    # prepare a regex for char filtering
    re_punc = re.compile('[%s]' % re.escape(string.punctuation))
    # remove punctuation from each word
    tokens = [re_punc.sub('', w) for w in tokens]
    # remove remaining tokens that are not alphabetic
    tokens = [word for word in tokens if word.isalpha()]
    # make lower case
    tokens = [word.lower() for word in tokens]
    return tokens    

# save tokens to file, one dialog per line
def save_doc(lines, filename):
    data = '\n'.join(lines)
    file = open(filename, 'w')
    file.write(data)
    file.close()

# load document
print("Input the name of your raw file: \n")
in_filename = str(input())
doc = load_doc(in_filename)
print(doc[:200])

# clean document
tokens = clean_doc(doc)
print(tokens[:200])
print(f'Total Tokens: {len(tokens)}')
print(f'Unique Tokens: {len(set(tokens))}')

# organize into sequences of tokens
length = 50 + 1 
sequences = list()
for i in range(length, len(tokens)):
    # select sequence of tokens
    seq = tokens[i-length:i]
    # convert into a line
    line = ' '.join(seq)
    # store 
    sequences.append(line)
print(f'Total Sequences: {len(sequences)}')

# save sequences to file
print("Save the sequences to a file. Ensure it ends with .txt \n Input your sequence file name: \n")
out_filename = str(input())
save_doc(sequences, out_filename)


