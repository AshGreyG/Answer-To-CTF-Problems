import struct
from typing import List

# Notice base91 is not the standard coding protocol. It is an alternative
# coding protocol of base64. A python implementation can see here:
#   https://github.com/aberaud/base91-python/blob/master/base91.py
# The algorithm can be found at:
#   https://stackoverflow.com/questions/46978133/base91-how-is-it-calculated

class Base91 :
    CHARSET = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!#$%&()*+,./:;<=>?@[]^_`{|}~\""
    CHARSET_HASHTABLE = {char: index for index, char in enumerate(CHARSET)}

    @staticmethod
    def encode(data : bytes) -> str :
        binary_stream = 0
        digits = 0
        encoded : List[str] = []

        for i in range(len(data)) :
            byte = data[i:i + 1] # Now the type of byte is bytes
            binary_stream |= struct.unpack("B", byte)[0] << digits
            digits += 8

            if digits > 13 :
                # Use 13 digits as a chunk
                chunk = binary_stream & 0b1111111111111 # Which is the magic number 8191

                if chunk > 88 :
                    # The reason why the point is 88 is that when `chunk` is
                    # equal to or less than 88, chunk could be optimized to 14
                    # digits because
                    #
                    # 0b1#############
                    #    ←-----------→
                    #     original chunk <= 88
                    #
                    # So now the chunk <= 8192 + 88 = 8280 < 91 * 91 = 8281
                    # and chunk % 91 ∈ [0, 90], chunk // 91 ∈ [0, 90]

                    binary_stream >>= 13
                    digits -= 13
                else :
                    chunk = binary_stream & 0b11111111111111 # Which is the magic number 16383
                    binary_stream >>= 14
                    digits -= 14

                encoded.append(Base91.CHARSET[chunk % 91])
                encoded.append(Base91.CHARSET[chunk // 91])

        if digits > 0 : # That indicates there are remained digits
            encoded.append(Base91.CHARSET[binary_stream % 91])
            if digits >= 8 or binary_stream >= 91 :
                encoded.append(Base91.CHARSET[binary_stream // 91])

        return "".join(encoded)

    @staticmethod
    def decode(encoded : str) -> bytes :
        result : List[int] = []
        chunk = -1
        binary_stream = 0
        digits = 0

        for char in encoded :
            try :
                index = Base91.CHARSET_HASHTABLE[char]
                if chunk < 0 :
                    chunk = index
                else :
                    chunk += index * 91
                    binary_stream |= chunk << digits
                    digits += 13 if (chunk & 0b1111111111111 > 88) else 14

                    while True :
                        result.append(binary_stream & 0b11111111)
                        binary_stream >>= 8
                        digits -= 8
                        if not digits >= 8 :
                            break
                    chunk = -1

            except KeyError :
                raise KeyError("Invalid Base91 characters")

        if chunk != -1 :
            result.append((binary_stream | chunk << digits) & 0b11111111)
        return bytes(result)
