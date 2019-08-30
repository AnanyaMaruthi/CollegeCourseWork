def reverseSentence(sentence):
	words = sentence.split()
	words.reverse()
	sentence = " ".join(words)
	print(sentence)
	rev = ""
	for word in words:
	    word = word[::-1]
	    rev += word + " "
	print(rev)

sentence = input("Enter a sentence")
reverseSentence(sentence)

