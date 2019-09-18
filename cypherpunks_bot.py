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
    with open('quotes', 'r+', newline='\r') as tootfile:
        buff = tootfile.readlines()

    for line in buff[:]:
       
        line = line.strip(r'\r')
        link = getUrl(line)
        try:
            link is not None
            quote = getQuote(line, link)
            total_length = len(link) + len(quote)
            if total_length > 500:
                quote = quote[:(499-len(link))] + ' '
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
            
            #toot(toot) 
            print(toot)
            print(len(toot))

            print("Tooted!")

            with open('quotes', 'w') as tootfile:
                buff.remove(line)
                tootfile.writelines(buff)
            time.sleep(21)
        else:
            print("Skipped line - some issue occurred")
            with open('quotes', 'w') as tootfile:
                buff.remove(line)
                tootfile.writelines(buff)
            continue

except:
    print("Something wrong happened")
