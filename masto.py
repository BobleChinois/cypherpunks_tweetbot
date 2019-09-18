from mastodon import Mastodon
import os

def toot(tweet):

    cred_dir = os.path.join(os.path.dirname(__file__), 'masto_id')
    mastodon = Mastodon(
            access_token = cred_dir,
            api_base_url = 'https://mastodon.social'
            )

    mastodon.status_post(tweet)

    return('Tooted: ', tweet)
