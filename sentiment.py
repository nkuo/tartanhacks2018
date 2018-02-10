import requests
from pprint import pprint
import json


subscription_key=""
text_analytics_base_url = "https://eastus.api.cognitive.microsoft.com/text/analytics/v2.0/"
sentiment_api_url = text_analytics_base_url + "sentiment"

"""
documents = {'documents' : [
  {'id': '1', 'language': 'en', 'text': 'I had a wonderful experience! The rooms were wonderful and the staff was helpful.'},
  {'id': '2', 'language': 'en', 'text': 'I had a terrible time at the hotel. The staff was rude and the food was awful.'},
]}

headers   = {"Ocp-Apim-Subscription-Key": subscription_key}
response  = requests.post(sentiment_api_url, headers=headers, json=documents)
sentiments = response.json()
pprint(sentiments)
"""

text = ["I had a wonderful experience! The rooms were wonderful and the staff was helpful.",
        "I had a terrible time at the hotel. The staff was rude and the food was awful.",
        "It's strange to me that people have an issue with new Twitch guidelines."]


def getSentiment(texts):
    ls = list()
    for i in range(len(text)):
        ls.append({"id": str(i + 1), "language": "en", "text": text[i]})
    documents = dict()
    documents["documents"] = ls

    headers = {"Ocp-Apim-Subscription-Key": subscription_key}
    response = requests.post(sentiment_api_url, headers=headers, json=documents)
    sentiments = response.json()

    result = list()
    for i in range(len(text)):
        result.append(sentiments["documents"][i]["score"])
    return result