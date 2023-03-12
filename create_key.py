from random import randint
key = ""
for i in range(16):
    key += chr(randint(0, 255))

file = open("key", "w", encoding="utf8")
file.write(key)
file.close
