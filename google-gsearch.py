from gsearch.googlesearch import search

results = search('Github')  
# print(results)

for item in results:
	print(item[0])
	print(item[1])
