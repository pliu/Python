from Crypto.Cipher import AES

def strxor (a,b):     # xor two strings of different lengths
    return "".join([chr(ord(x)^ord(y)) for (x,y) in zip(a,b)])

def CBC_decrypt (key, ct):
    key = key.decode("hex")
    ct = ct.decode("hex")
    pt = []
    i = 16
    while i < len(ct):
        decryptor = AES.new(key)
        pt.append (strxor(decryptor.decrypt (ct[i:i+16]), ct[i-16:i]))
        i = i + 16
    print "".join(x for x in pt)

def next_iv (iv):
    iv = iv.encode("hex")
    l = len(iv)
    i = int(iv,16) + 1
    iv = hex(i)[2:]
    iv = iv[:len(iv)-1]
    while len(iv) != l:
        iv = "0"+iv
    return iv.decode("hex")
    
def CTR_decrypt (key, ct):
    key = key.decode("hex")
    ct = ct.decode("hex")
    pt = []
    i = 16
    iv = ct[:16]
    while i < len(ct):
        decryptor = AES.new(key)
        pt.append (strxor(decryptor.encrypt (iv), ct[i:i+16]))
        iv = next_iv (iv)
        i = i + 16
    print "".join(x for x in pt)

key1 = "140b41b22a29beb4061bda66b6747e14" 
ct1 = "4ca00ff4c898d61e1edbf1800618fb2828a226d160dad07883d04e008a7897ee2e4b7465d5290d0c0e6c6822236e1daafb94ffe0c5da05d9476be028ad7c1d81"
CBC_decrypt(key1, ct1)

key2 = "140b41b22a29beb4061bda66b6747e14"
ct2 = "5b68629feb8606f9a6667670b75b38a5b4832d0f26e1ab7da33249de7d4afc48e713ac646ace36e872ad5fb8a512428a6e21364b0c374df45503473c5242a253"
CBC_decrypt(key2, ct2)

key3 = "36f18357be4dbd77f050515c73fcf9f2"
ct3 = "69dda8455c7dd4254bf353b773304eec0ec7702330098ce7f7520d1cbbb20fc388d1b0adb5054dbd7370849dbf0b88d393f252e764f1f5f7ad97ef79d59ce29f5f51eeca32eabedd9afa9329"
CTR_decrypt(key3, ct3)

key4 = "36f18357be4dbd77f050515c73fcf9f2"
ct4 = "770b80259ec33beb2561358a9f2dc617e46218c0a53cbeca695ae45faa8952aa0e311bde9d4e01726d3184c34451"
CTR_decrypt(key4, ct4)
