# pip install beautifulsoup4
# pip install requests
# python default html parseer ir html.parser can install 3rd party lxml (External C depencency, but is very fast) 
# or another pure python one html5lib

# This will be a script or part of a script

from bs4 import BeautifulSoup as soup
import requests

URL = "https://twitter.com/elonmusk" 
# 1. Make a request to twritter
def request_page():
    try:
       response = requests.get(URL)
    except Exception as e:
        print(e)

    if response.status_code != 200:
        print("Non success status code returned " + str(response.status_code))

    twitter_page = soup(response.text, "html.parser")
    #print(twitter_page)
    return twitter_page

# 2. Give beautiful soup the response html page from twitter
def request_last_tweet(twitter_page):
    tweets = twitter_page.find_all("li", {"data-item-type": "tweet"})
    for tweet in tweets:
        print(tweet)
    #Extract tweet

twitter_page = request_page()
request_last_tweet(twitter_page)



# 3. Get the latest tweet
