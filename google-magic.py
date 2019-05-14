import os
import sys
import time
import random
# import pprint
import codecs

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
# https://github.com/howie6879/magic_google
# pip install magic_google
from magic_google import MagicGoogle

mg = MagicGoogle()

x=0
file = codecs.open("result-"+ str(x) + ".txt", "w", "utf-8")
for url in mg.search_url(query='Github',num=100, start=x * 100):
	file.write(url)
	print(url)
	# file.write("\n")
	file.write("\n----------------\n")
file.close()
