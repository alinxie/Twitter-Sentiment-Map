from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener

ckey="pGb1oXyiZIEdQcDTN9a3d558P"
csecret="JmDv2GkfJU5jEUvLLcdMMxs9Jt9xVvHzDeRlAcgpGVURCllfYS"
atoken="4213484361-cUiKplc8SVdYkKvx6CrUFBHGzAFlyaHNJBbLHZ6"
asecret="f767WjWbFTd0BzQyPChICAfc9rIvxDIJmWlxTD3sfTnov"

class listener(StreamListener):

    def on_data(self, data):
        print(data)
        return True
    def on_error(self, status):
        print(status)

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterStream = Stream(auth, listener())
twitterStream.filter(track=["lambda x: x"])
