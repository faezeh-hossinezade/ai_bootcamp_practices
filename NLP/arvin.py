import numpy as np
import re

def count_str(message):
	b = {}
	for a in message:
		b.setdefault(a,0)
		b[a] = b[a]+1
	words=message.split()
	all_word_count = len(words)
	unique_words = set(words)
	num_unique_words = len(unique_words)
	try:
		ratio = num_unique_words / all_word_count
	except ZeroDivisionError:
		ratio = 0
	filtered = ''.join(filter(lambda x: x not in '".,;!-?', message))
	words_4 = [word for word in filtered.split() if word]
	try:
		avg = sum(map(len, words_4))/len(words_4)
	except ZeroDivisionError:
		avg = 0
	filter_farsi="".join(re.findall(r"[\u0600-\u06FF-\W\u06A9\u06CC\u06F0\u06F1\u06F2\u06F3\u06F4\u06F5\u06F6\u06F7\u06F8\u06F9\u0647\u066B]+", message))
	len_farsi=len(filter_farsi)
	try:
		ratio_farsi=len_farsi/sum(b.values())
	except ZeroDivisionError:
		ratio_farsi = 0
	print(f"({sum(b.values())}, {all_word_count}, {ratio}, {avg}, {ratio_farsi})")

x =str(input())
x_str=str(x)
count_str(x_str)