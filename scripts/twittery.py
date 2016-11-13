from TwitterAPI import TwitterAPI
api = TwitterAPI("pGb1oXyiZIEdQcDTN9a3d558P", "JmDv2GkfJU5jEUvLLcdMMxs9Jt9xVvHzDeRlAcgpGVURCllfYS", "4213484361-cUiKplc8SVdYkKvx6CrUFBHGzAFlyaHNJBbLHZ6", "f767WjWbFTd0BzQyPChICAfc9rIvxDIJmWlxTD3sfTnov")

def main():
    r = api.request('statuses/sample').get_iterator()
    tweet = []
    for item in r:
        if 'text' in item:
            if item['coordinates'] != None:
                tweet.append([item['text'], item['coordinates']['coordinates']])
                print(tweet[len(tweet)-1])
            elif item['place'] != None:
                center = [sum(x)/4 for x in zip(item['place']['bounding_box']['coordinates'][0][0],item['place']['bounding_box']['coordinates'][0][1],item['place']['bounding_box']['coordinates'][0][2],item['place']['bounding_box']['coordinates'][0][3])]
                tweet.append([item['text'], center])
                print(tweet[len(tweet)-1])

main()
