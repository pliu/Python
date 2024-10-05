import gmpy2
from gmpy2 import mpz

p = mpz("13407807929942597099574024998205846127479365820592393377723561443721764030073546976801874298166903427690031858186486050853753882811946569946433649006084171")
g = mpz("11717829880366207009516117596335367088558084999998952205599979459063929499736583746670572176471460312928594829675428279466566527115212748467589894601965568")
h = mpz("3239475104050450443565264378728065788649097520952449527834792452971981976143292558073856937958553180532878928001494706097394108577585732452307673444020333")

dic = {}
B = 2**20
base = gmpy2.powmod(g, -B, p)
for i in xrange (B):
    dic [gmpy2.f_mod(h*gmpy2.powmod(base, i, p), p)] = i
for i in xrange (B):
    if gmpy2.powmod(g, i, p) in dic:
        print dic [gmpy2.powmod(g, i, p)]*B + i
        break