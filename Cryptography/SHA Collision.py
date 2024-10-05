from hashlib import sha256
import os

dic = {}
limit = int(2**24.4)
for i in xrange(1,limit*8):
    test = os.urandom(10)
    h = int(bin(int(sha256(test).hexdigest(),16))[-50:])
    if h in dic:
        print dic[h].encode("hex")
        print test.encode("hex")
    else:
        dic[h] = test
    if i%limit == 0:
        dic = {}
        print "reset"
