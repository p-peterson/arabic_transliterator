# Transliterating Arabic to English text (without short vowels)

# From .txt file

# -*- coding: utf-8 -*-

from sys import argv
import file_to_string
import arabic_sentence_transliterator


script, file = argv


translit_me = file_to_string.convert(file)

print "\n--------------------------------------------------"
print "Original text:\n"
print translit_me


transd_string = arabic_sentence_transliterator.translate_me(translit_me)

print "\n--------------------------------------------------"
print "Transliterated text:\n"
print ''.join(transd_string)


print "\n--------------------------------------------------"
print "Would you like to save the transliteration as a new file?"
print "(Will create new file or truncate if already exists.)"
save = raw_input("> ")
if save == "yes" or save == "y" or save == "Yes" or save == "Y":
	print "What would you like to call it?"
	name = raw_input("> ")
	txt = open(name, "w")
	txt.write(transd_string)
	print "File saved."
else:
	print "File not saved."
	





#___________________________
#convert to string, then: to_trans = arabic_list.decode('utf-8')