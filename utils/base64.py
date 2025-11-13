from typing import List

class Base64 :
    CHARSET = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    CHARSET_HASHTABLE = {char: index for index, char in enumerate(CHARSET)}

    @staticmethod
    def encode(data : bytes) -> str :
        if not data :
            return ""

        binary_stream = "".join(f"{byte:08b}" for byte in data)
        padding = (6 - len(binary_stream) % 6) % 6
        binary_stream += "0" * padding

        encoded : List[str] = []

        for i in range(0, len(binary_stream), 6) :
            chunk = binary_stream[i:i + 6]
            index = int(chunk, 2)
            encoded.append(Base64.CHARSET[index])

        encoded_padding = (4 - len(encoded) % 4) % 4
        encoded += "=" * encoded_padding

        return "".join(encoded)

    @staticmethod
    def decode(encoded : str) -> bytes :
        encoded = encoded.rstrip("=") # remove encoded padding characters
        binary_stream = ""
        result : List[int] = []

        for char in encoded :
            try :
                index = Base64.CHARSET_HASHTABLE[char]
                binary_stream += f"{index:06b}"
            except KeyError :
                raise KeyError("Invalid Base64 characters")

        # The length of `binary_stream` must be the times in 6 and we must find
        # a times in 8 and is closet to length of `binary_stream`

        binary_stream = binary_stream[0:len(binary_stream) - len(binary_stream) % 8]

        for i in range(0, len(binary_stream), 8) :
            byte = int(binary_stream[i:i + 8], 2)
            result.append(byte)

        return bytes(result)
