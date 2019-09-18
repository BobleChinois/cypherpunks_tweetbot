import time, os, re
from random import choice 
from masto import toot

def getUrl(text):
    # Separate the link from the rest of the line
    
    regex = r'https.*'

    m = re.search(regex, text)

    try:
        url = m.group()
        return url
    except:
        return None

def getQuote(text, url):
    
    raw_quote = re.split(url, text)
    quote = raw_quote[0]

    return quote

try:
    with open('quotes', 'r+') as tweetfile:
        buff = tweetfile.readlines()

    for line in buff[:]:
       
        line = line.strip(r'\n')
        link = getUrl(line)
        try:
            link is not None
            quote = getQuote(line, link)
            tweet = quote + link
            tweet_length = len(tweet)

        except:
            quote = line
            tweet = quote.strip('/n')
            tweet_length = len(tweet)

        if tweet_length <= 500:
            """print("Tweeting...")
            print(f"{tweet}")
            twitter.update_status(status=tweet)
            print("Tweeted!")"""
            
            toot(tweet) 

            print("Tooted!")

            with open('quotes', 'w') as tweetfile:
                buff.remove(line)
                tweetfile.writelines(buff)
            time.sleep(21600)
        else:
            print("Skipped line - some issue occurred")
            with open('quotes', 'w') as tweetfile:
                buff.remove(line)
                tweetfile.writelines(buff)
            continue

    print("No more lines to tweet...")

except TwythonError as e:
    print(e)
