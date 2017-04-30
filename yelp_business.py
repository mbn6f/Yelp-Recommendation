import json
import csv
import re


filename = "yelp_academic_dataset_business.json"
str = 'Restaurant'
count, bcount = 0

with open('yelp_business.csv', 'w') as file:
    w = csv.writer(file)
    w.writerow(["business_id", "city", "state", "num_reviews", "avg rating"])
    with open(filename, encoding="utf-8") as f:
        for line in f:
            data = json.loads(line)
            count += 1
            list = repr(data['categories'])
            if re.search("Restaurant", list):
                print(data['categories'])
                bcount += 1
                w.writerow([data['business_id'], data['city'], data['state'], data['review_count'], data['stars']])
        print(count)
        print("bcount: "+ bcount);


