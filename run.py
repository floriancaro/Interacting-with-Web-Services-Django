#!/usr/bin/env python3

import os
import requests

data_path = "/data/feedback"
website_url = "http://<corpweb-external-IP>/feedback/"

# initialize dictionary to hold feedback information
feedback_data = {}

# parse every feedback txt file and add the contained information to the dictionary
for f in os.listdir(data_path):
    with open(os.path.join(data_path,f)) as feedback:
        feedback_list = feedback.read().splitlines() 
        feedback_data = {
                        "title": feedback_list[0],
                        "name": feedback_list[1],
                        "date": feedback_list[2],
                        "feedback": feedback_list[3]
                        }
        # check dictionary contents
        print(feedback_data)

        # post feedback entries to website
        response = requests.post(website_url, json=feedback_data)

        # check for HTTP error messages
        response.raise_for_status()
