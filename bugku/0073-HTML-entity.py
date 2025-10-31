# original text: comment in HTML <script> source code:
# <-- &#102;&#108;&#97;&#103;&#123;&#53;&#57;&#51;&#52;&#55;&#54;&#100;&#50;&#51;&#97;&#53;&#56;&#98;&#49;&#102;&#56;&#50;&#53;&#54;&#52;&#57;&#98;&#48;&#48;&#51;&#98;&#97;&#100;&#53;&#57;&#100;&#50;&#125; -->

original = "102;&#108;&#97;&#103;&#123;&#53;&#57;&#51;&#52;&#55;&#54;&#100;&#50;&#51;&#97;&#53;&#56;&#98;&#49;&#102;&#56;&#50;&#53;&#54;&#52;&#57;&#98;&#48;&#48;&#51;&#98;&#97;&#100;&#53;&#57;&#100;&#50;&#125"

# This is the character entity reference of HTML / XML
# See: https://en.wikipedia.org/wiki/List_of_XML_and_HTML_character_entity_references 
#
# &#nnnn; here the `n` is the codepoint of this character in decimal
# &#hhhh; here the `h` is the codepoint of this character in hexdecimal

original_codepoints = map(int, original.split(";&#"))

for cp in original_codepoints :
    print(chr(cp), end = "")

# Result is flag{593476d23a58b1f825649b003bad59d2}
