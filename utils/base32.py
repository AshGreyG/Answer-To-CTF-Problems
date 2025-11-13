from typing import List

class Base32 :
    CHARSET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ234567"
    CHARSET_HASHTABLE = {char: index for index, char in enumerate(CHARSET)}

    @staticmethod
    def encode(data : bytes) -> str :
        if not data :
            return ""

        binary_stream = "".join(f"{byte:08b}" for byte in data)
        padding = (5 - len(binary_stream) % 5 ) % 5
        binary_stream += "0" * padding

        encoded : List[str] = []

        for i in range(0, len(binary_stream), 5) :
            chunk = binary_stream[i:i + 5]
            index = int(chunk, 2)
            encoded.append(Base32.CHARSET[index])

        encoded_padding = (8 - len(encoded) % 8) % 8
        encoded += ["="] * encoded_padding

        return "".join(encoded)

    @staticmethod
    def decode(encoded : str) -> bytes :
        encoded = encoded.rstrip("=") # remove encoded padding
        binary_stream = ""
        result : List[int] = []
        for char in encoded :
            try :
                index = Base32.CHARSET_HASHTABLE[char]
                binary_stream += f"{index:05b}"
            except KeyError :
                raise KeyError("Invalid Base32 characters")

        # When finishing processing the binary_stream, the padding 0 at the end
        # of binary_stream may still make the decoding failed:

        # The length of `binary_stream` must be the times in 5 and we need to
        # find a times in 8 and is closest to `binary_stream`

        binary_stream = binary_stream[0:len(binary_stream) - len(binary_stream) % 8]

        for i in range(0, len(binary_stream), 8) :
            byte = int(binary_stream[i:i + 8], 2)
            result.append(byte)

        return bytes(result)
