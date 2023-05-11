from random import randint
key = bin(randint(0, 2**256 - 1))[2:]
key = "0" * (256 - len(str(key))) + key
file = open("key", "w", encoding="utf8")
file.write(key)
file.close
