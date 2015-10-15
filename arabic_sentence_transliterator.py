# -*- coding: utf-8 -*-

# function that takes Arabic string and converts to English transliteration
# returns string of transliteration

def translate_me(word):
	i = 0
	word_trans = []
	while i < len(word):

		# to get the last punctuation
		# (those that are recognized as non-Arabic characters— .!\n)
		# necessary step b/c all other characters are 2 bytes, not 1
		if i == len(word)-1:
			if word[i] == " ":
				word_trans.append(" ")
				trans_as_string = "".join(word_trans)
				return trans_as_string
			elif word[i] == ".":
				word_trans.append(".")
				trans_as_string = "".join(word_trans)
				return trans_as_string
			elif word[i] == "!":
				word_trans.append("!")
				trans_as_string = "".join(word_trans)
				return trans_as_string
			elif word[i] == "\n":
				word_trans.append("\n")
				trans_as_string = "".join(word_trans)
				return trans_as_string
			
		# combines two list items to re-create Arabic character
		# finds character and replaces with English transliteration
		# appends transliteration to list
		letter = word[i] + word[i+1]
		if word[i] == " ":
			word_trans.append(" ")
			i -= 1		
		elif word[i] == ".":
			word_trans.append(".")
			i -= 1		
		elif word[i] == "!":
			word_trans.append("!")
			i -= 1		
		elif word[i] == "\n":
			word_trans.append("\n")
			i -= 1			
		elif word[i] == "0":
			word_trans.append("0")
			i -= 1			
		elif word[i] == "1":
			word_trans.append("1")
			i -= 1			
		elif word[i] == "2":
			word_trans.append("2")
			i -= 1			
		elif word[i] == "3":
			word_trans.append("3")
			i -= 1			
		elif word[i] == "4":
			word_trans.append("4")
			i -= 1			
		elif word[i] == "5":
			word_trans.append("5")
			i -= 1			
		elif word[i] == "6":
			word_trans.append("6")
			i -= 1			
		elif word[i] == "7":
			word_trans.append("7")
			i -= 1			
		elif word[i] == "8":
			word_trans.append("8")
			i -= 1			
		elif word[i] == "9":
			word_trans.append("9")
			i -= 1	
		elif word[i+1] == "0":
			word_trans.append("0")
			i -= 1			
		elif word[i+1] == "1":
			word_trans.append("1")
			i -= 1			
		elif word[i+1] == "2":
			word_trans.append("2")
			i -= 1			
		elif word[i+1] == "3":
			word_trans.append("3")
			i -= 1			
		elif word[i+1] == "4":
			word_trans.append("4")
			i -= 1			
		elif word[i+1] == "5":
			word_trans.append("5")
			i -= 1			
		elif word[i+1] == "6":
			word_trans.append("6")
			i -= 1			
		elif word[i+1] == "7":
			word_trans.append("7")
			i -= 1			
		elif word[i+1] == "8":
			word_trans.append("8")
			i -= 1			
		elif word[i+1] == "9":
			word_trans.append("9")
			i -= 1			
		elif word[i+1] == "!":
			word_trans.append("!")
			i -= 1		
		elif word[i+1] == ".":
			word_trans.append(".")
			i -= 1		
		elif word[i+1] == " ":
			word_trans.append(" ")
			i -= 1		
		elif word[i+1] == "\n":
			word_trans.append("\n")
			i -= 1		
		elif letter == "؟":
			word_trans.append("?")		
		elif letter == "ض":
			word_trans.append("dh")
		elif letter == "ص":
			word_trans.append("S")
		elif letter == "ث":
			word_trans.append("th")
		elif letter == "ق":
			word_trans.append("q")
		elif letter == "ف":
			word_trans.append("f")
		elif letter == "غ":
			word_trans.append("gh")
		elif letter == "ع":
			word_trans.append("3")
		elif letter == "ه":
			word_trans.append("h")
		elif letter == "خ":
			word_trans.append("kh")
		elif letter == "ح":
			word_trans.append("H")
		elif letter == "ج":
			word_trans.append("j")
		elif letter == "د":
			word_trans.append("d")
		elif letter == "ش":
			word_trans.append("sh")
		elif letter == "س":
			word_trans.append("s")
		elif letter == "ي":
			word_trans.append("i")
		elif letter == "ب":
			word_trans.append("b")
		elif letter == "ل":
			word_trans.append("l")
		elif letter == "ا":
			word_trans.append("a")
		elif letter == "أ":
			word_trans.append("a")
		elif letter == "ت":
			word_trans.append("t")
		elif letter == "ن":
			word_trans.append("n")
		elif letter == "م":
			word_trans.append("m")
		elif letter == "ك":
			word_trans.append("k")
		elif letter == "ط":
			word_trans.append("T")
		elif letter == "ئ":
			word_trans.append("'")
		elif letter == "ء":
			word_trans.append("'")
		elif letter == "ؤ":
			word_trans.append("u'")
		elif letter == "ر":
			word_trans.append("r")
		elif letter == "لا":
			word_trans.append("la")
		elif letter == "ى":
			word_trans.append("a")
		elif letter == "ة":
			word_trans.append("ah")
		elif letter == "و":
			word_trans.append("u")
		elif letter == "ز":
			word_trans.append("z")
		elif letter == "ظ":
			word_trans.append("TH")
		elif letter == "ذ":
			word_trans.append("th")
		else:
			word_trans.append("*")


	# add 2 because each Arabic character is two bytes(locations) of the list
		i += 2

	
	trans_as_string = "".join(word_trans)
	return trans_as_string
