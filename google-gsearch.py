from gsearch.googlesearch import search

# results = search('Github')  
results = search('Github', num_results=100)

# print(results)

for item in results:
	print(item)
