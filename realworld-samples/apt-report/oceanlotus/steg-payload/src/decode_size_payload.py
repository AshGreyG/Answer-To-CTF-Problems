import png

def get_rgba(w, h, pixels, x, y) :
    pos = x + y * w
    pixel = pixels[pos * 4 : (pos + 1) * 4]
    return pixel[0], pixel[1], pixel[2], pixel[3]

def decode_pixel(w, h, pixels, x, y) :
    r, g, b, a = get_rgba(w, h, pixels, x, y)

    # First 
    return ((r & 0b0111) | (((b << 3) | (g & 0b0111)) << 3 )) & 0b11111111

w, h, pixels, metadata = png.Reader(filename = "./samples/payload.png").read_flat()

size = 0
x = 0
y = 0

# Decode size of payload
while x < 4 :
    size = (size >> 8) | (decode_pixel(w, h, pixels, x, y) << 24)
