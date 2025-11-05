from typing import Dict
from utils.base64 import Base64
from utils.base64_to_image import base64_to_image

with open("./file.txt", "r", encoding = "utf-8") as file :
    encoded = ""
    for line in file.readlines() :
        encoded += line

    heap : Dict[str, int] = {}

    for char in encoded :
        if char in heap :
            heap[char] += 1
        else :
            heap[char] = 1

    for key in sorted(heap.keys(), key = lambda x : ord(x)) :
        print("{:<5}{:<5}{:<5}".format(ord(key), key, heap[key]))

    print(Base64.decode(encoded))
    print(base64_to_image(encoded, "./test"))

    # flag{thisispigpassword}
