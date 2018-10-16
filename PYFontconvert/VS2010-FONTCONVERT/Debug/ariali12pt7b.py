class GFXfont:
	def __init__(self):

		#   Format of the following GFXglyphs tuple is as follows:
		#
		#   bitmapOffset   - offset into the GFXbitmaps tuple 
		#   width   - width of the character 
		#   height  - height of the character 
		#   xAdvance    - The horizontal distance the cursor position must be incremented 
		#               (for left-to-right writing) or decremented (for right-to-left writing) 
		#                  by after each glyph is rendered when processing text. 
		#                   It is always positive for horizontal layouts, and null for vertical ones.
		#   xOffset - The horizontal distance from the current pen position to the
		#               glyph's left bbox (glyph's boundary box) edge. 
		#               It is positive for horizontal layouts, and in most cases negative for vertical ones.
		#   yOffset -  The vertical distance from the baseline to the top of the glyph'sbbox.
		#               It is usually positive for horizontal layouts, and negative for vertical ones.

		self.GFXglyphs = (
		(     0,   0,   0,   7,    0,    1 ),   ## 0x20 ' '
		(     0,   5,  17,   7,    1,  -16 ),   ## 0x21 '!'
		(    11,   8,   6,   9,    2,  -16 ),   ## 0x22 '"'
		(    17,  13,  17,  13,    1,  -16 ),   ## 0x23 '#'
		(    45,  12,  20,  13,    1,  -17 ),   ## 0x24 '$'
		(    75,  18,  18,  21,    2,  -16 ),   ## 0x25 '%'
		(   116,  14,  17,  16,    2,  -16 ),   ## 0x26 '&'
		(   146,   3,   6,   5,    3,  -16 ),   ## 0x27 '''
		(   149,   8,  22,   8,    2,  -16 ),   ## 0x28 '('
		(   171,   8,  22,   8,   -1,  -16 ),   ## 0x29 ')'
		(   193,   8,   7,   9,    3,  -16 ),   ## 0x2A '*'
		(   200,  12,  12,  14,    2,  -14 ),   ## 0x2B '+'
		(   218,   3,   6,   7,    0,   -1 ),   ## 0x2C ','
		(   221,   7,   2,   8,    1,   -6 ),   ## 0x2D '-'
		(   223,   3,   2,   7,    1,   -1 ),   ## 0x2E '.'
		(   224,  11,  17,   7,   -1,  -16 ),   ## 0x2F '/'
		(   248,  12,  17,  13,    1,  -16 ),   ## 0x30 '0'
		(   274,   8,  17,  13,    3,  -16 ),   ## 0x31 '1'
		(   291,  12,  17,  13,    1,  -16 ),   ## 0x32 '2'
		(   317,  12,  17,  13,    1,  -16 ),   ## 0x33 '3'
		(   343,  12,  17,  13,    1,  -16 ),   ## 0x34 '4'
		(   369,  13,  17,  13,    1,  -16 ),   ## 0x35 '5'
		(   397,  11,  17,  13,    2,  -16 ),   ## 0x36 '6'
		(   421,  11,  17,  13,    3,  -16 ),   ## 0x37 '7'
		(   445,  12,  17,  13,    1,  -16 ),   ## 0x38 '8'
		(   471,  11,  17,  13,    2,  -16 ),   ## 0x39 '9'
		(   495,   5,  13,   7,    1,  -12 ),   ## 0x3A ':'
		(   504,   5,  17,   7,    0,  -12 ),   ## 0x3B ';'
		(   515,  11,  11,  14,    2,  -13 ),   ## 0x3C '<'
		(   531,  11,   7,  14,    2,  -11 ),   ## 0x3D '='
		(   541,  11,  11,  14,    2,  -13 ),   ## 0x3E '>'
		(   557,  10,  17,  13,    3,  -16 ),   ## 0x3F '?'
		(   579,  22,  22,  24,    1,  -16 ),   ## 0x40 '@'
		(   640,  16,  17,  16,   -1,  -16 ),   ## 0x41 'A'
		(   674,  14,  17,  16,    1,  -16 ),   ## 0x42 'B'
		(   704,  15,  17,  17,    2,  -16 ),   ## 0x43 'C'
		(   736,  16,  17,  17,    1,  -16 ),   ## 0x44 'D'
		(   770,  16,  17,  16,    1,  -16 ),   ## 0x45 'E'
		(   804,  16,  17,  15,    1,  -16 ),   ## 0x46 'F'
		(   838,  17,  17,  19,    2,  -16 ),   ## 0x47 'G'
		(   875,  17,  17,  17,    1,  -16 ),   ## 0x48 'H'
		(   912,   7,  17,   6,    1,  -16 ),   ## 0x49 'I'
		(   927,  13,  17,  12,    1,  -16 ),   ## 0x4A 'J'
		(   955,  17,  17,  16,    1,  -16 ),   ## 0x4B 'K'
		(   992,  11,  17,  13,    1,  -16 ),   ## 0x4C 'L'
		(  1016,  20,  17,  20,    0,  -16 ),   ## 0x4D 'M'
		(  1059,  16,  17,  17,    1,  -16 ),   ## 0x4E 'N'
		(  1093,  17,  17,  19,    2,  -16 ),   ## 0x4F 'O'
		(  1130,  16,  17,  16,    1,  -16 ),   ## 0x50 'P'
		(  1164,  17,  19,  19,    2,  -16 ),   ## 0x51 'Q'
		(  1205,  16,  17,  17,    1,  -16 ),   ## 0x52 'R'
		(  1239,  14,  17,  16,    2,  -16 ),   ## 0x53 'S'
		(  1269,  14,  17,  15,    3,  -16 ),   ## 0x54 'T'
		(  1299,  15,  17,  17,    2,  -16 ),   ## 0x55 'U'
		(  1331,  16,  17,  16,    2,  -16 ),   ## 0x56 'V'
		(  1365,  24,  17,  24,    3,  -16 ),   ## 0x57 'W'
		(  1416,  21,  17,  17,   -1,  -16 ),   ## 0x58 'X'
		(  1461,  16,  17,  16,    3,  -16 ),   ## 0x59 'Y'
		(  1495,  14,  17,  15,    1,  -16 ),   ## 0x5A 'Z'
		(  1525,   9,  22,   7,    0,  -16 ),   ## 0x5B '['
		(  1550,   6,  17,   7,    2,  -16 ),   ## 0x5C '\'
		(  1563,  10,  22,   7,   -2,  -16 ),   ## 0x5D ']'
		(  1591,  10,   9,  11,    2,  -16 ),   ## 0x5E '^'
		(  1603,  14,   2,  13,   -2,    4 ),   ## 0x5F '_'
		(  1607,   4,   4,   8,    3,  -16 ),   ## 0x60 '`'
		(  1609,  11,  13,  13,    1,  -12 ),   ## 0x61 'a'
		(  1627,  12,  17,  13,    1,  -16 ),   ## 0x62 'b'
		(  1653,  11,  13,  12,    1,  -12 ),   ## 0x63 'c'
		(  1671,  13,  17,  13,    1,  -16 ),   ## 0x64 'd'
		(  1699,  12,  13,  13,    1,  -12 ),   ## 0x65 'e'
		(  1719,   9,  17,   7,    1,  -16 ),   ## 0x66 'f'
		(  1739,  13,  18,  13,    1,  -12 ),   ## 0x67 'g'
		(  1769,  12,  17,  13,    1,  -16 ),   ## 0x68 'h'
		(  1795,   7,  17,   6,    1,  -16 ),   ## 0x69 'i'
		(  1810,  11,  22,   5,   -3,  -16 ),   ## 0x6A 'j'
		(  1841,  12,  17,  12,    1,  -16 ),   ## 0x6B 'k'
		(  1867,   7,  17,   6,    1,  -16 ),   ## 0x6C 'l'
		(  1882,  19,  13,  20,    1,  -12 ),   ## 0x6D 'm'
		(  1913,  12,  13,  13,    1,  -12 ),   ## 0x6E 'n'
		(  1933,  12,  13,  13,    1,  -12 ),   ## 0x6F 'o'
		(  1953,  13,  18,  13,    0,  -12 ),   ## 0x70 'p'
		(  1983,  13,  18,  12,    1,  -12 ),   ## 0x71 'q'
		(  2013,  10,  13,   8,    0,  -12 ),   ## 0x72 'r'
		(  2030,  11,  13,  12,    1,  -12 ),   ## 0x73 's'
		(  2048,   7,  17,   7,    1,  -16 ),   ## 0x74 't'
		(  2063,  13,  13,  13,    1,  -12 ),   ## 0x75 'u'
		(  2085,  12,  13,  12,    2,  -12 ),   ## 0x76 'v'
		(  2105,  17,  13,  16,    1,  -12 ),   ## 0x77 'w'
		(  2133,  12,  13,  12,    0,  -12 ),   ## 0x78 'x'
		(  2153,  14,  18,  12,    0,  -12 ),   ## 0x79 'y'
		(  2185,  11,  13,  11,    0,  -12 ),   ## 0x7A 'z'
		(  2203,   9,  22,   8,    1,  -16 ),   ## 0x7B '{'
		(  2228,   2,  22,   6,    2,  -16 ),   ## 0x7C '|'
		(  2234,   9,  22,   8,   -1,  -16 ),   ## 0x7D '}'
		(  2259,  12,   4,  14,    2,   -9 )	## 0x7E '~'
			)

		self.GFXfirst = 0x20
		self.GFXlast = 0x7E
		self.GFXyadvance = 27
		self.GFXMinYadvance = -17
				## from face->size->metrics.height
	def __repr__ (self):
		rows = ''
		for y in range(self.height):
			for x in range(self.width):
				rows += '*' if self.pixels[y * self.width + x] else ' '
		rows += '\n'
		return rows

## Approx. 2937 bytes