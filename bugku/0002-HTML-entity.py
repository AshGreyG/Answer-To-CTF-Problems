# Use xxd to see file.jpg and at the end of the result there are many
# HTML character entity reference:
#
# &#107;&#101;&#121;&#123;&#121;&#111;&#117;&#32;&#97;&#114;&#101;&#32;&#114;&#105;&#103;&#104;&#116;&#125;

entity = "107;&#101;&#121;&#123;&#121;&#111;&#117;&#32;&#97;&#114;&#101;&#32;&#114;&#105;&#103;&#104;&#116;&#125"
entity_codepoints = map(int, entity.split(";&#"))

for cp in entity_codepoints :
    print(chr(cp), end = "")
