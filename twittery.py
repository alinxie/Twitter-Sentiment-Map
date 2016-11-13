from TwitterAPI import TwitterAPI
from sklearn.cluster import KMeans
import numpy as np
import time
import sys
import json
from watson_developer_cloud import ToneAnalyzerV3

api = TwitterAPI("pGb1oXyiZIEdQcDTN9a3d558P", "JmDv2GkfJU5jEUvLLcdMMxs9Jt9xVvHzDeRlAcgpGVURCllfYS", "4213484361-cUiKplc8SVdYkKvx6CrUFBHGzAFlyaHNJBbLHZ6", "f767WjWbFTd0BzQyPChICAfc9rIvxDIJmWlxTD3sfTnov")
tone_analyzer = ToneAnalyzerV3(
        username='fae1b7aa-7534-4fda-b5d1-775076ca668c',
        password='TbzeEoT4cxHi',
        version='2016-05-19')
def main():
    f = open('clusters.txt', 'w')
    r = api.request('statuses/filter', {'locations':'-124.848974,24.396308, -66.885444,49.384358'}).get_iterator()
    tweet = []
    interval = 5*60
    start_time = time.time()
    n = 1
    while n < 500:
        item = next(r)
        if 'text' in item:
            if item['coordinates'] != None:
                new_item = [item['text'], item['coordinates']['coordinates']]
                tweet.append(new_item)
                print(new_item)
        n += 1
        print(n)
    tweet_locations = locations(tweet)
    clusters = cluster(tweet_locations, 8)
    cluster_text = combine_text(tweet,clusters)
    for loc, text in cluster_text.items():
        f.write('CLUSTER\n')
        f.write('-------\n')
        f.write(str(loc) + '\n')
        f.write('\n')
        f.write(text)
        f.write('\n')
    f.close()    
def watson_clusters(topic):
    api = TwitterAPI("pGb1oXyiZIEdQcDTN9a3d558P", "JmDv2GkfJU5jEUvLLcdMMxs9Jt9xVvHzDeRlAcgpGVURCllfYS", "4213484361-cUiKplc8SVdYkKvx6CrUFBHGzAFlyaHNJBbLHZ6", "f767WjWbFTd0BzQyPChICAfc9rIvxDIJmWlxTD3sfTnov")
    r = api.request('statuses/filter', {'locations':'-124.848974,24.396308, -66.885444,49.384358', 'q': topic}).get_iterator()
    tweet = []
    interval = 5*60
    start_time = time.time()
    n = 50
    while n > 0:
        item = next(r)
        if 'text' in item:
            if item['coordinates'] != None:
                new_item = [item['text'], item['coordinates']['coordinates']]
                tweet.append(new_item)
                print(new_item)
        n -= 1
    tweet_locations = locations(tweet)
    clusters = cluster(tweet_locations, 3)
    cluster_text = combine_text(tweet,clusters)
    return watsonize(cluster_text)
def locations(tweets):
    return [[tweet[1][1],tweet[1][0]] for tweet in tweets]
def cluster(loc, n_clusters):
    kmeans = KMeans(n_clusters = n_clusters, random_state = 0).fit(loc)
    return kmeans
def combine_text(tweets, clusters):
    cluster_dict = {}
    cluster_centers = clusters.cluster_centers_
    which_cluster = clusters.labels_
    for j in range(len(cluster_centers)):
        center = cluster_centers[j]
        c = tuple(center)
        cluster_dict[c] = {'string':'', 'count': 0, 'inertia': 0}
    for i in range(len(tweets)):
        tweet_cluster_index = which_cluster[i]
        tweet_cluster_loc = tuple(cluster_centers[tweet_cluster_index])
        tweet_text = tweets[i][0]
        tweet_location = tweets[i][1]
        cluster_data = cluster_dict[tweet_cluster_loc]
        cluster_data['string'] = cluster_data['string'] + tweet_text + '\n'
        cluster_data['count'] = cluster_data['count'] + 1
        cluster_data['inertia'] = cluster_data['inertia'] + distance(tweet_cluster_loc, tweet_location)
    return cluster_dict

def watsonize(cluster_text):
    tone_analyzer = ToneAnalyzerV3(
        username='fae1b7aa-7534-4fda-b5d1-775076ca668c',
        password='TbzeEoT4cxHi',
        version='2016-05-19')
    for center, data in cluster_text.items():
        s = data['string']
        emotion_data = tone_analyzer.tone(text = s, tones = 'emotion', sentences = False)
        data['emotion'] = emotion_data
    return cluster_text




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
def distance(x, y):
   return ((x[0]-y[0])**2+(x[1]-y[1])**2)**0.5

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

#while True:
#main()
#watson_clusters('pokemon')
