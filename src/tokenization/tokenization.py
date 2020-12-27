


import nltk
from nltk.tokenize import RegexpTokenizer

puncts_exceptapostrophe = '!"#$%&()*+,-./:;<=>?@[\]^`{|}~'
TOKENIZE_PATTERN = fr"[{puncts_exceptapostrophe}]|\w+|['\w]+"
regex_tokenizer = RegexpTokenizer(pattern=TOKENIZE_PATTERN)


output_file = open("output.txt","w")

with open('tr.txt',"r") as reader:
	lines = reader.readlines()
	for line in lines:
		line = line.lower()
		tokens = regex_tokenizer.tokenize(line)
		sentence = " ".join(tokens)
		output_file.write(sentence+"\n")

output_file.close()

