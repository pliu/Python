import sys
import json

def clean(word):
    word = word.strip(" \t.,?:!")
    return word

def count (counts, tweet):
    try:
        text = tweet['text']
    except KeyError:
        return
    else:
        words = text.split()
        for word in words:
            word = clean(word)
            if word not in counts:
                counts[word] = 1
            else:
                counts[word] += 1

def hw(tweet_file):
    counts = {}
    for line in tweet_file:
        tweet = json.loads(line)
        count(counts, tweet)
    return counts

def main():
    tweet_file = open(sys.argv[1])
    counts = hw(tweet_file)
    total = 0
    for word in counts:
        total += counts[word]
    for word in counts:
        print word, float(counts[word])/total

if __name__ == '__main__':
    main()
