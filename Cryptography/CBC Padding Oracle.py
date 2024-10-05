def strxor (a,b):     # xor two strings of different lengths
    return "".join([chr(ord(x)^ord(y)) for (x,y) in zip(a,b)])

file = open("./CBC_PO.txt", "r")
target = file.readline()
buffer = file.readlines()
file.close()
data = []
for i in xrange(len(buffer)):
    hex_start = buffer[i].find("/")
    code_start = buffer[i].find('1.1"')
    if buffer[i][code_start+5:code_start+8] == "404":
        if (i+1 == len(buffer)) or (buffer[i][hex_start+33:hex_start+65] != buffer[i+1][hex_start+33:hex_start+65]):
            data.append([buffer[i][hex_start+1:hex_start+33],buffer[i][hex_start+33:hex_start+65]])
hex_start = target.find("/")
end = target.find(" ", hex_start)
target = target[hex_start+1:end]

pad = "10101010101010101010101010101010"

result = []
for i in xrange(len(data)-1):
    result.append(strxor(strxor(data[i][1].decode("hex"), data[i+1][0].decode("hex")),pad.decode("hex")))

print "".join(i for i in result)
