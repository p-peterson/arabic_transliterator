# -*- coding: utf-8 -*-

# takes a file and returns a string of file contents


from sys import argv

script, filename = argv


def convert(filename):
	with open (filename, "r") as myfile:
		data=myfile.read()
		return data


