import json
import datetime
import csv
import datetime
import re


filename = "yelp_academic_dataset_review.json"
count = 0
pattern = re.compile("[^\w']")

with open("positive-words.txt") as f:
	pos_words = f.read().split()[213:]

with open("negative-words.txt") as f:
	neg_words = f.read().split()[213:]

with open('yelp_reviews.csv', 'w') as file:
	w = csv.writer(file)
	w.writerow(["user_id","business_id","date","stars","review_length", "pos_words", "neg_words", "net_sentiment"])
	
	with open(filename, encoding="utf-8") as f:
		for line in f:
			data = json.loads(line)
			votes = data['useful']
			text = data['text'].lower()
			text_tokens = pattern.sub(' ', text).split()
			stars = data['stars']
			
			# http://www.wolframalpha.com/input/?i=average+english+word+length
			review_length = len(text_tokens) / 5.1
			
			num_positive = sum([r in pos_words for r in text_tokens])
			num_negative = sum([r in neg_words for r in text_tokens])
			net_sentiment = num_positive - num_negative
			
			w.writerow([data['user_id'], data['business_id'], data['date'], data['stars'], review_length,num_positive, num_negative, net_sentiment])
			count = count + 1
			if count % 1000 == 0:
  				print ("%s: %s" % (count, datetime.datetime.now()))