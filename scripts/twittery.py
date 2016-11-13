from TwitterAPI import TwitterAPI
api = TwitterAPI("pGb1oXyiZIEdQcDTN9a3d558P", "JmDv2GkfJU5jEUvLLcdMMxs9Jt9xVvHzDeRlAcgpGVURCllfYS", "4213484361-cUiKplc8SVdYkKvx6CrUFBHGzAFlyaHNJBbLHZ6", "f767WjWbFTd0BzQyPChICAfc9rIvxDIJmWlxTD3sfTnov")

def main():
    r = api.request('statuses/sample').get_iterator()
    for item in r:
        if 'text' in item:
            if item['coordinates'] != None:
                print(item['text'], item['coordinates']['coordinates'])
            elif item['place'] != None:
                print(item['text'], item['place'])
            else:
                print('hello!')

main()
