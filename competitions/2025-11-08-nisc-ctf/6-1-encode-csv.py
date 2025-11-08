import base64
import csv
from typing import List

def encode(data : bytes, key : str = "a1a60171273e74a6") -> bytes :
    res = b""

    for i in range(len(data)) :
        c = key[(i + 1) & 0b1111]
        res += bytes.fromhex(hex(data[i] ^ ord(c))[2:].zfill(2))

    return res

def decode(encoded : bytes, key : str = "a1a60171273e74a6") -> bytes :
    res = b""

    for i in range(len(encoded)) :
        c = key[(i + 1) & 0b1111]
        res += bytes.fromhex(hex(encoded[i] ^ ord(c))[2:].zfill(2))

    return res

# data = "AshGrey"
#
# encode_data = base64.b64encode(encode(data.encode()))
# print(encode_data.decode())
#
# decode_data = decode(base64.b64decode(encode_data))
# print(decode_data.decode())

decoded_data_csv : List[List[str]] = [["user", "name", "phone", "address"]]

with open("./encoded_data.csv", "r") as encoded :
    reader = csv.reader(encoded)
    for row in reader :
        decoded_data_csv.append(list(map(
            lambda data : decode(base64.b64decode(data)).decode(),
            row
        )))

with open("./output.csv", "w", newline = "\n", encoding = "utf-8") as file :
    writer = csv.writer(file)
    writer.writerows(decoded_data_csv)

# Flag is DASCTF{63519917490045674824297218495327} 
