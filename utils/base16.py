from typing import Optional, List

class Base16 :
    CHARSET = "0123456789ABCDEF"

    @staticmethod
    def encode(data : bytes) -> str :
        result : List[str] = []
        for byte in data :
            nibble_high = (byte >> 4) & 0b00001111 # also can and with 0x0f
            nibble_low  = byte & 0b00001111

            # '0b01100001' ------> '0b00000110' ---------------> '0b00000110'
            #              >> 4                 & '0b00001111'

            # So `nibble_low` and `nibble_high` are not greater than 16 (so 
            # why it is called *base16*)

            result.append(Base16.CHARSET[nibble_high])
            result.append(Base16.CHARSET[nibble_low])

        return "".join(result)

    @staticmethod
    def decode(encoded : str) -> Optional[bytes] :
        encoded = encoded.upper().strip()
        result : List[int] = []

        if len(encoded) % 2 != 0 :
            raise ValueError("Length of encoded Base16 string must be even")

        for i in range(0, len(encoded), 2) :
            try :
                nibble_high = Base16.CHARSET.index(encoded[i])
                nibble_low  = Base16.CHARSET.index(encoded[i + 1])
            except ValueError :
                raise ValueError(f"Invalid Base16 character: {encoded[i]}{encoded[i + 1]}")
            byte = nibble_high << 4 | nibble_low
            result.append(byte)

        return bytes(result)
