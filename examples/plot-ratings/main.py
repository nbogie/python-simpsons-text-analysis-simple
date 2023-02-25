# in order to run this programme you will need to install textblob in console
# pip install textblob

# to enable noun phrase and other analyses, we installed a further package in console
# python -m textblob.download_corpora

import sys
import requests
import json
import numpy as np
import matplotlib.pyplot as plt
from pprint import pprint

# 83 is simpsons.  82 is G.o.T.
episodes_API_url = "https://api.tvmaze.com/shows/83/episodes"

# Make a GET request to the API
response = requests.get(episodes_API_url)

# Convert the (hopefully) json-format body of the response to a structured python object
data = json.loads(response.text)
# pprint(data)

# plot a scatter graph of a time series using matplotlib
plt.scatter([ep['airdate'] for ep in data], [
            ep['rating']['average'] for ep in data])

# reduce the number of labels on the x axis
plt.xticks(rotation=90)
plt.xticks(np.arange(0, len(data), 50))

# save plot to file
plt.savefig('simpsons_ratings.png')
# plt.show()
