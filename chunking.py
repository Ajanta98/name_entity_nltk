import nltk
from nltk.corpus import inaugural
from nltk.tokenize import PunktSentenceTokenizer

train_text = inaugural.raw("1801-Jefferson.txt")
sample_text = inaugural.raw("1801-Jefferson.txt")

sent_tokenizer = PunktSentenceTokenizer(train_text)

tokenized = sent_tokenizer.tokenize(sample_text)

def process_content():
	try:
		for i in tokenized:
			words=nltk.word_tokenize(i)
			tagged=nltk.pos_tag(words)

			chunky = r"""Chunk: {<RB.?>*<VB.?>*<NNP>+<NN>} """
			chunkparse = nltk.RegexpParser(chunky)
			chunki=chunkparse.parse(tagged)
			chunki.draw()
			print(tagged)
	except Exception as e:
		print(str(e))

process_content()