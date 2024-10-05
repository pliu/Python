import sys
import json

def count (counts, tweet):
    try:
        tags = tweet['entities']['hashtags']
    except KeyError:
        return
    else:
        for tag in tags:
            if tag['text'] not in counts:
                counts[tag['text']] = 1
            else:
                counts[tag['text']] += 1

def hw(tweet_file):
    counts = {}
    for line in tweet_file:
        tweet = json.loads(line)
        count(counts, tweet)
    return counts

def main():
    tweet_file = open(sys.argv[1])
    counts = hw(tweet_file)
    counts = counts.items()
    counts.sort(key=lambda x: -x[1])
    for i in xrange(10):
        print counts[i][0], counts[i][1]

if __name__ == '__main__':
    main()
