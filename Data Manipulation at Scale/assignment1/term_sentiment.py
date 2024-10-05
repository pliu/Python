import sys
import json

def clean(word):
    word = word.strip(" \t.,?:!")
    return word

def calcSent(new_words, scores, tweet):
    try:
        text = tweet['text']
    except KeyError:
        return
    else:
        total = 0
        words = text.split()
        for word in words:
            word = clean(word)
            if word in scores:
                total += scores[word]
        for word in words:
            word = clean(word)
            if word not in scores:
                if word not in new_words:
                    new_words[word] = (total, 1)
                else:
                    new_words[word] = (new_words[word][0] + total, new_words[word][1] + 1)

def hw(scores, tweet_file):
    new_words = {}
    for line in tweet_file:
        tweet = json.loads(line)
        calcSent(new_words, scores, tweet)
    return new_words

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
    new_words = hw(scores, tweet_file)
    for word in new_words:
        print word, float(new_words[word][0])/new_words[word][1]

if __name__ == '__main__':
    main()
