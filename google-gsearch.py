import codecs
from gsearch.googlesearch import search

# results = search('Github')  
results = search('Github', num_results=100)

# print(results)

file = codecs.open("result.txt", "w", "utf-8")

for item in results:

	# It will not works on windows OS : utf8 problem...
	# https://stackoverflow.com/questions/16346914/python-3-2-unicodeencodeerror-charmap-codec-cant-encode-character-u2013-i
	# https://github.com/llSourcell/twitter_sentiment_challenge/issues/1
	# print(item)
	# print(item[0])
	# print(item[1])
	# print("----------------")

	file.write(item[0])
	file.write("\n")
	file.write(item[1])
	file.write("\n----------------\n")

file.close()

