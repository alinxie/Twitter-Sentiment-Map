from TwitterAPI import TwitterAPI

ckey="pGb1oXyiZIEdQcDTN9a3d558P"
csecret="JmDv2GkfJU5jEUvLLcdMMxs9Jt9xVvHzDeRlAcgpGVURCllfYS"
atoken="4213484361-cUiKplc8SVdYkKvx6CrUFBHGzAFlyaHNJBbLHZ6"
asecret="f767WjWbFTd0BzQyPChICAfc9rIvxDIJmWlxTD3sfTnov"

# Update this to be dynamic and take user input
search_term = "america"

api = TwitterAPI(ckey, csecret, atoken, asecret)
r = api.request('search/tweets', {'q': search_term})

for tweets in r:
    print(tweets['text'])
    if  tweets['coordinates'] != None:
        print('\n' + tweets['coordinates'])
    print('\n')
