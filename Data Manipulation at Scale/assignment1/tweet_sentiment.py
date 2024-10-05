import sys
import json

def clean(word):
    word = word.upper()
    word = word.strip(" \t.,?:!")
    return word

def calcSent(scores, tweet):
    try:
        text = tweet['text']
    except KeyError:
        return 0
    else:
        total = 0
        words = text.split()
        for word in words:
            word = clean(word)
            if word in scores:
                total += scores[word]
        return total

def hw(scores, tweet_file):
    for line in tweet_file:
        tweet = json.loads(line)
        yield calcSent(scores, tweet)

def getSent(sent_file):
    scores = {}
    for line in sent_file:
        term, score  = line.split("\t")
        scores[term] = int(score)
    return scores

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    scores = getSent(sent_file)
    it = hw(scores, tweet_file)
    for value in it:
        print value

if __name__ == '__main__':
    main()
