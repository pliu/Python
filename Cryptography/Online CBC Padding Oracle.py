import urllib2
import sys

TARGET = "http://crypto-class.appspot.com/po?er="
CIPHERTEXT = "f20bdba6ff29eed7b046d1df9fb7000058b1ffb4210a580f748b4ac714c001bd4a61044426fb515dad3f21f18aa577c0bdf302936266926ff37dbf7035d5eeb4"

#--------------------------------------------------------------
# padding oracle
#--------------------------------------------------------------
class PaddingOracle(object):
    def query(self, q):
        target = TARGET + urllib2.quote(q)    # Create query URL
        req = urllib2.Request(target)         # Send HTTP request to server
        try:
            f = urllib2.urlopen(req)          # Wait for response
        except urllib2.HTTPError, e:          
            #print "We got: %d" % e.code       # Print response code
            if e.code == 404:
                return True # good padding
            return False # bad padding

def strxor (a,b):     # xor two strings of different lengths
    return "".join([chr(ord(x)^ord(y)) for (x,y) in zip(a,b)])

def next_check (pad, k):
    unit = hex(k)[2:]
    if len(unit) == 1:
        unit = "0" + unit
    tpad = unit + pad
    return tpad

def make_hex (j):
    unit = hex(j)[2:]
    if len(unit) == 1:
        unit = "0" + unit
    return unit

def next_position (pad, j):
    tpad = ""
    i = 0
    while i < len(pad):
        unit = strxor(strxor(pad[i:i+2].decode("hex"), make_hex(j).decode("hex")), make_hex(j+1).decode("hex")).encode("hex")
        tpad = tpad + unit
        i = i + 2
    return tpad

def fill_pad (pad):
    tpad = pad
    while len(tpad) < 32:
        tpad = "20" + tpad
    return tpad

po = PaddingOracle()

data = []
i = 32
while i < len(CIPHERTEXT):
    pad = ""
    for j in xrange (16):
        pad = next_position (pad,j)
        for k in xrange (256):
            if po.query (fill_pad(next_check(pad, k)) + CIPHERTEXT [i:i+32]):
                print fill_pad(next_check(pad, k)) + CIPHERTEXT [i:i+32]
                pad = next_check (pad, k)
                break
    data.append (pad)
    i = i + 32

pad = "10101010101010101010101010101010"

result = []
for i in xrange(len(data)):
    result.append(strxor(strxor(data[i].decode("hex"), CIPHERTEXT[32*i:32*i+32].decode("hex")),pad.decode("hex")))

print "".join(i for i in result)
