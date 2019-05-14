import codecs
from gsearch.googlesearch import search

# results = search('Github')  
results = search('Github', num_results=100)

# print(results)

file = codecs.open("result.txt", "w", "utf-8")

for item in results:

	# It will not works on windows OS : utf8 problem...
	# https://stackoverflow.com/questions/934160/write-to-utf-8-file-in-python
	# print(item)
	# print(item[0])
	# print(item[1])
	# print("----------------")

	file.write(item[0])
	file.write("\n")
	file.write(item[1])
	file.write("\n----------------\n")

file.close()

