import json
import datetime
import csv
import unicodedata


filename = "yelp_academic_dataset_user.json"

with open('users.csv', 'w') as file:

    headers = ["user_id", "year", "num_friends", "votes", "num_reviews", "avg rating"]
    w = csv.DictWriter(file, delimiter=',', lineterminator='\n', fieldnames=headers)
    with open(filename, encoding="utf-8") as f:
        for line in f:
            data = json.loads(line)
            votes = data['useful'] + data['funny'] + data['cool']
            print(len(data['friends']))
            if data['review_count'] >= 30:
                w.writerow({"user_id": data['user_id'], "year": data['yelping_since'], "num_friends":len(data['friends']),
                            "votes": votes, "num_reviews": data['review_count'], "avg rating": data['average_stars']})
