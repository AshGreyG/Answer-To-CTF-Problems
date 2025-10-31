# This is the Morse code and the decoding table can see here:
# https://gist.githubusercontent.com/bjlange/cf83f8efea1276af1c7b/raw/d9f091fa863eb6852a287a75975228b9c52583b2/morse.py

decode = {
    ".-": "A",
    "-...": "B",
    "-.-.": "C",
    "-..": "D",
    ".": "E",
    "..-.": "F",
    "--.": "G",
    "....": "H",
    "..": "I",
    ".---": "J",
    "-.-": "K",
    ".-..": "L",
    "--": "M",
    "-.": "N",
    "---": "O",
    ".--.": "P",
    "--.-": "Q",
    ".-.": "R",
    "...": "S",
    "-": "T",
    "..-": "U",
    "...-": "V",
    ".--": "W",
    "-..-": "X",
    "-.--": "Y",
    "--..": "Z",
    "-----": "0",
    ".----": "1",
    "..---": "2",
    "...--": "3",
    "....-": "4",
    ".....": "5",
    "-....": "6",
    "--...": "7",
    "---..": "8",
    "----.": "9"
}

original = "..-./.-../.-/--./----.--/-../...--/..-./-.-./-.../..-./.----/--.../..-./----./...--/----./----./...../-----/....-/-----.-"
original_codepoints = original.split("/")

for cp in original_codepoints :
    if cp not in list(decode.keys()) :
        print("*", end = "")
    else :
        print(decode[cp], end = "")

# Result is FLAG*D3FCBF17F9399504*, so the answer should be flag{d3fcbf17f9399504}
