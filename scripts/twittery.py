from TwitterAPI import TwitterAPI
import time

api = TwitterAPI("pGb1oXyiZIEdQcDTN9a3d558P", "JmDv2GkfJU5jEUvLLcdMMxs9Jt9xVvHzDeRlAcgpGVURCllfYS", "4213484361-cUiKplc8SVdYkKvx6CrUFBHGzAFlyaHNJBbLHZ6", "f767WjWbFTd0BzQyPChICAfc9rIvxDIJmWlxTD3sfTnov")

def main():
    r = api.request('statuses/filter', {'locations':'-124.848974,24.396308, -66.885444,49.384358'}).get_iterator()
    tweet = []
    interval = 5*60
    start_time = time.time()
    n = 1

    for item in r:
        if 'text' in item:
            if item['coordinates'] != None:
                tweet.append([item['text'], item['coordinates']['coordinates']])
                print(tweet[len(tweet)-1])
#            elif item['place'] != None:
 #               center = [sum(x)/4 for x in zip(item['place']['bounding_box']['coordinates'][0][0],item['place']['bounding_box']['coordinates'][0][1],item['place']['bounding_box']['coordinates'][0][2],item['place']['bounding_box']['coordinates'][0][3])]
  #              tweet.append([item['text'], center])
   #             print(tweet[len(tweet)-1])
#        if time.time() > start_time + interval * n:
#            n+=1
#            info = k_means(list(tweet))
#            print(info)
#            tweet = []
#
#def k_means(l):
#    CALLS = 100
#    old_centroids = []
#    max_updates = 1000000
#    n = 0
#    centroids = [l[i] for i in range(0, CALLS)]
#    while old_centroids != centroids and n < max_updates:
#        old_centroids = centroids
#        clusters = group_by_centroid(l, old_centroids)
#        centroids = [find_centroid(x) for x in clusters]
#        n += 1
#    return centroids
#
#def distance(x, y):
#    return ((x[0]-y[0])**2+(x[1]-y[1])**2)**0.5
#
#def find_closest(location, centroids):
#    return min(centroids, key=lambda x: distance(location, x))
#
#def group_by_first(pairs):
#    keys = []
#    for key, _ in pairs:
#        if key not in keys:
#            keys.append(key)
#    return [[y for x, y in pairs if x==key] for key in keys]
#
#def group_by_centroid(tweets, centroids):
#    groups = [[find_closest(tweets, centroids), x] for x in tweets]
#    return group_by_first(groups)
#
#def find_centroid(cluster):
#    return [mean([x[0] for x in cluster]), mean([x[1] for x in cluster])]

while True:
    main()


