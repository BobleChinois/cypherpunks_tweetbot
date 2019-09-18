import time, os, re
from random import choice 
from mastodon import Mastodon
import os

cred_dir = os.path.join(os.path.dirname(__file__), 'masto_id')

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
    with open('quotes', 'r+', newline='\r') as tootfile:
        buff = tootfile.readlines()

    for line in buff[:]:
       
        line = line.strip(r'\r')
        link = getUrl(line)
        try:
            link is not None
            quote = getQuote(line, link)
            total_length = len(quote) + 23
            if total_length > 500:
                quote = quote[:(499-23)] + ' '
            toot = quote + link

        except:
            toot = line
            toot_length = len(toot)
            if toot_length > 500:
                toot = toot[:500]

        if len(toot) > 2:
            """print("Tweeting...")
            print(f"{tweet}")
            twitter.update_status(status=tweet)
            print("Tweeted!")"""
            
            mastodon = Mastodon(
                    access_token = cred_dir,
                    api_base_url = 'https://mastodon.social'
                    )

            mastodon.status_post(toot)

            print("Tooted!")

            with open('quotes', 'w') as tootfile:
                buff.remove(line)
                tootfile.writelines(buff)
            time.sleep(21600)
        else:
            print("Skipped line - some issue occurred")
            with open('quotes', 'w') as tootfile:
                buff.remove(line)
                tootfile.writelines(buff)
            continue

except:
    print("Something wrong happened")
