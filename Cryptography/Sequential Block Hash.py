from Crypto.Hash import SHA256

myfile = "D:/Work/Programming/Python/Cryptography/SBH.mp4"
f = open(myfile, "rb")

blocks = []

try:
    read = f.read(1024)
    while read != "":
        blocks.append (read)
        read = f.read(1024)
finally:
    f.close()
    
blocks.reverse()

h = SHA256.new()
h.update(blocks [0])
app = h.digest()
i = 1
while i < len (blocks):
    h = SHA256.new()
    h.update(blocks[i])
    h.update(app)
    app = h.digest()
    i += 1

print app.encode("hex")
