import json
import datetime
import csv
import re
import unicodedata


filename = "yelp_academic_dataset_business.json"
str = 'Restaurant'

with open('yelp_business.csv', 'w') as file:
    w = csv.writer(file)
    w.writerow(["business_id", "city", "state", "num_reviews", "avg rating"])
    with open(filename, encoding="utf-8") as f:
        for line in f:
            data = json.loads(line)
            list = repr(data['categories'])
            if re.search("Restaurant", list):
                print(data['categories'])
                w.writerow([data['business_id'], data['city'], data['state'], data['review_count'], data['stars']])

