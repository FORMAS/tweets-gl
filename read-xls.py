from nltk import word_tokenize
from nltk.tokenize import MWETokenizer
from openpyxl import Workbook
import openpyxl
import json
import sys

book = openpyxl.load_workbook('gl-filter.xlsx')

sheet = book.active

frequency_matrix 	= {}
gl_terms 			= []
tweets		 		= []
i = 0

def search_term(term):
	#i = 0
	for tweet in tweets:
		#if i == 10:
		#	break
		#print(tweet['text'])
		tt = tweet['text'].lower()
		tm = term.lower()
		if ' ' in term: # MultiToken
			tokenize_term = word_tokenize(tm)
			tokenizer = MWETokenizer('', separator=" ")
			before_tokens = len(tokenizer.tokenize(tt.split()))
			tokenizer = MWETokenizer([tokenize_term], separator=" ")
			after_tokens = len(tokenizer.tokenize(tt.split()))
			if after_tokens < before_tokens:
				sheet['H' + str(i+1)] = sheet['H' + str(i+1)].value + 1
				#book.save('tfreq-gl-filter.xlsx')
				#exit()
				#create_frequency_matrix(tm)
				#print('#MultiToken:', tm)
				#print(tokenizer.tokenize(tt.split()))
		else: # Token
			if tm in word_tokenize(tt):
				sheet['H' + str(i+1)] = sheet['H' + str(i+1)].value + 1
				#book.save('tfreq-gl-filter.xlsx')
				#exit()
				#create_frequency_matrix(tm)
				#continue
				#print('#Token:', term)
		#i+=1
		#print(i)

file_tweets = open('tweets-gl.json', 'r')
for line in file_tweets.readlines():
	tweets.append(json.loads(line))

for r in sheet.iter_rows():
	# Ignora a primeira linha (label)
	if i != 0:
		search_term(r[1].value)
	i += 1
	print(i)
	
book.save('tfreq-gl-filter.xlsx')
nterms = i

'''
	TODO
	Retirar token + (*) || (*) + token
	token + (...)
'''

def create_frequency_matrix(term):
	if term in frequency_matrix:
		frequency_matrix[term] += 1
	else:
		frequency_matrix[term] = 1
	return frequency_matrix

#print(sorted(frequency_matrix.items(), key=lambda x: x[1], reverse=True))
print("Nº de termos: ", nterms)

'''
	TODO
	Armazenar o termo e a ocorrência
'''