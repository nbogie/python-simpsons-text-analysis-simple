# in order to run this programme you will need to install textblob in console
# pip install textblob

# to enable noun phrase and other analyses, we installed a further package in console
# python -m textblob.download_corpora

from textblob import TextBlob
from pprint import pprint
import requests
import json
import re


def build_topics_index():
    topics = {}

    for episode in data:
        summary = episode["summary"]
        # strip out any html tag from summary text, using a regex
        summary = re.sub(r'<[^>]*>', '', summary)
        ep_code = episode["season"], episode["number"]

        # Create a TextBlob object and perform sentiment analysis
        blob = TextBlob(summary)
        nps = blob.noun_phrases
        for np in nps:
            if np in topics:
                topics[np].append(ep_code)
            else:
                topics[np] = [ep_code]
        # sentiment_score = blob.sentiment.polarity
    return topics


# 83 is simpsons.  82 is G.o.T.
episodes_API_url = "https://api.tvmaze.com/shows/83/episodes"

# Make a GET request to the API
response = requests.get(episodes_API_url)

# Convert the (hopefully) json-format body of the response to a structured python object
data = json.loads(response.text)

topics = build_topics_index()

for topic, occs in topics.items():
    if (len(occs) > 1):
        print(topic, occs)
