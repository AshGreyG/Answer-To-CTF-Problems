from itertools import product
from utils.base64 import Base64

cipher = "QWIHBLGZZXJSXZNVBZW="
# In base64, the encoded text can be divided by 4
typos = [
    {"Q", "q", "9"},
    {"W", "w"},
    {"I", "i", "1"},
    {"H", "h"},
    {"B", "b", "6"},
    {"L", "l", "1"},
    {"G", "g", "9"},
    {"Z", "z", "2"},
    {"Z", "z", "2"},
    {"X", "x"},
    {"J", "j"},
    {"S", "s", "5"},
    {"X", "x"},
    {"Z", "z", "2"},
    {"N", "n"},
    {"V", "v"},
    {"B", "b", "6"},
    {"Z", "z", "2"},
    {"W", "w"},
]

for fixed in product(*typos) :
    b64 = "".join(fixed) + "="
    d64 = str(Base64.decode(b64))
    if "\\x" not in d64 and "_" in d64 :
        print(d64)

# Finally we can find that base64 QW1hbl92ZXJ5X2Nvb2w= can decode the string
# Aman_very_cool, so the flag is flag{Aman_very_cool}