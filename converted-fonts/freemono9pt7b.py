class GFXfont():
	def __init__(self):
		self.GFXglyphs = (
		  (     0,   0,   0,  11,    0,    1 ),   ## 0x20 ' '
		  (     0,   2,  11,  11,    4,  -10 ),   ## 0x21 '!'
		  (     3,   6,   5,  11,    2,  -10 ),   ## 0x22 '"'
		  (     7,   7,  12,  11,    2,  -10 ),   ## 0x23 '#'
		  (    18,   8,  12,  11,    1,  -10 ),   ## 0x24 '$'
		  (    30,   7,  11,  11,    2,  -10 ),   ## 0x25 '%'
		  (    40,   7,  10,  11,    2,   -9 ),   ## 0x26 '&'
		  (    49,   3,   5,  11,    4,  -10 ),   ## 0x27 '''
		  (    51,   2,  13,  11,    5,  -10 ),   ## 0x28 '('
		  (    55,   2,  13,  11,    4,  -10 ),   ## 0x29 ')'
		  (    59,   7,   7,  11,    2,  -10 ),   ## 0x2A '*'
		  (    66,   7,   7,  11,    2,   -8 ),   ## 0x2B '+'
		  (    73,   3,   5,  11,    2,   -1 ),   ## 0x2C ','
		  (    75,   9,   1,  11,    1,   -5 ),   ## 0x2D '-'
		  (    77,   2,   2,  11,    4,   -1 ),   ## 0x2E '.'
		  (    78,   7,  13,  11,    2,  -11 ),   ## 0x2F '#'
		  (    90,   7,  11,  11,    2,  -10 ),   ## 0x30 '0'
		  (   100,   5,  11,  11,    3,  -10 ),   ## 0x31 '1'
		  (   107,   7,  11,  11,    2,  -10 ),   ## 0x32 '2'
		  (   117,   8,  11,  11,    1,  -10 ),   ## 0x33 '3'
		  (   128,   6,  11,  11,    3,  -10 ),   ## 0x34 '4'
		  (   137,   7,  11,  11,    2,  -10 ),   ## 0x35 '5'
		  (   147,   7,  11,  11,    2,  -10 ),   ## 0x36 '6'
		  (   157,   7,  11,  11,    2,  -10 ),   ## 0x37 '7'
		  (   167,   7,  11,  11,    2,  -10 ),   ## 0x38 '8'
		  (   177,   7,  11,  11,    2,  -10 ),   ## 0x39 '9'
		  (   187,   2,   8,  11,    4,   -7 ),   ## 0x3A ':'
		  (   189,   3,  11,  11,    3,   -7 ),   ## 0x3B ''
		  (   194,   8,   8,  11,    1,   -8 ),   ## 0x3C '<'
		  (   202,   9,   4,  11,    1,   -6 ),   ## 0x3D '='
		  (   207,   9,   8,  11,    1,   -8 ),   ## 0x3E '>'
		  (   216,   7,  10,  11,    2,   -9 ),   ## 0x3F '?'
		  (   225,   8,  12,  11,    2,  -10 ),   ## 0x40 '@'
		  (   237,  11,  10,  11,    0,   -9 ),   ## 0x41 'A'
		  (   251,   9,  10,  11,    1,   -9 ),   ## 0x42 'B'
		  (   263,   9,  10,  11,    1,   -9 ),   ## 0x43 'C'
		  (   275,   9,  10,  11,    1,   -9 ),   ## 0x44 'D'
		  (   287,   9,  10,  11,    1,   -9 ),   ## 0x45 'E'
		  (   299,   9,  10,  11,    1,   -9 ),   ## 0x46 'F'
		  (   311,  10,  10,  11,    1,   -9 ),   ## 0x47 'G'
		  (   324,   9,  10,  11,    1,   -9 ),   ## 0x48 'H'
		  (   336,   5,  10,  11,    3,   -9 ),   ## 0x49 'I'
		  (   343,   8,  10,  11,    2,   -9 ),   ## 0x4A 'J'
		  (   353,   9,  10,  11,    1,   -9 ),   ## 0x4B 'K'
		  (   365,   8,  10,  11,    2,   -9 ),   ## 0x4C 'L'
		  (   375,  11,  10,  11,    0,   -9 ),   ## 0x4D 'M'
		  (   389,   9,  10,  11,    1,   -9 ),   ## 0x4E 'N'
		  (   401,   9,  10,  11,    1,   -9 ),   ## 0x4F 'O'
		  (   413,   8,  10,  11,    1,   -9 ),   ## 0x50 'P'
		  (   423,   9,  13,  11,    1,   -9 ),   ## 0x51 'Q'
		  (   438,   9,  10,  11,    1,   -9 ),   ## 0x52 'R'
		  (   450,   7,  10,  11,    2,   -9 ),   ## 0x53 'S'
		  (   459,   9,  10,  11,    1,   -9 ),   ## 0x54 'T'
		  (   471,   9,  10,  11,    1,   -9 ),   ## 0x55 'U'
		  (   483,  11,  10,  11,    0,   -9 ),   ## 0x56 'V'
		  (   497,  11,  10,  11,    0,   -9 ),   ## 0x57 'W'
		  (   511,   9,  10,  11,    1,   -9 ),   ## 0x58 'X'
		  (   523,   9,  10,  11,    1,   -9 ),   ## 0x59 'Y'
		  (   535,   7,  10,  11,    2,   -9 ),   ## 0x5A 'Z'
		  (   544,   2,  13,  11,    5,  -10 ),   ## 0x5B '['
		  (   548,   7,  13,  11,    2,  -11 ),   ## 0x5C '\'
		  (   560,   2,  13,  11,    4,  -10 ),   ## 0x5D ']'
		  (   564,   7,   5,  11,    2,  -10 ),   ## 0x5E '^'
		  (   569,  11,   1,  11,    0,    2 ),   ## 0x5F '_'
		  (   571,   3,   3,  11,    3,  -11 ),   ## 0x60 '`'
		  (   573,   9,   8,  11,    1,   -7 ),   ## 0x61 'a'
		  (   582,   9,  11,  11,    1,  -10 ),   ## 0x62 'b'
		  (   595,   7,   8,  11,    2,   -7 ),   ## 0x63 'c'
		  (   602,   9,  11,  11,    1,  -10 ),   ## 0x64 'd'
		  (   615,   8,   8,  11,    1,   -7 ),   ## 0x65 'e'
		  (   623,   6,  11,  11,    3,  -10 ),   ## 0x66 'f'
		  (   632,   9,  11,  11,    1,   -7 ),   ## 0x67 'g'
		  (   645,   9,  11,  11,    1,  -10 ),   ## 0x68 'h'
		  (   658,   7,  10,  11,    2,   -9 ),   ## 0x69 'i'
		  (   667,   5,  13,  11,    3,   -9 ),   ## 0x6A 'j'
		  (   676,   8,  11,  11,    2,  -10 ),   ## 0x6B 'k'
		  (   687,   7,  11,  11,    2,  -10 ),   ## 0x6C 'l'
		  (   697,   9,   8,  11,    1,   -7 ),   ## 0x6D 'm'
		  (   706,   9,   8,  11,    1,   -7 ),   ## 0x6E 'n'
		  (   715,   9,   8,  11,    1,   -7 ),   ## 0x6F 'o'
		  (   724,   9,  11,  11,    1,   -7 ),   ## 0x70 'p'
		  (   737,   9,  11,  11,    1,   -7 ),   ## 0x71 'q'
		  (   750,   7,   8,  11,    3,   -7 ),   ## 0x72 'r'
		  (   757,   7,   8,  11,    2,   -7 ),   ## 0x73 's'
		  (   764,   8,  10,  11,    2,   -9 ),   ## 0x74 't'
		  (   774,   8,   8,  11,    1,   -7 ),   ## 0x75 'u'
		  (   782,   9,   8,  11,    1,   -7 ),   ## 0x76 'v'
		  (   791,   9,   8,  11,    1,   -7 ),   ## 0x77 'w'
		  (   800,   9,   8,  11,    1,   -7 ),   ## 0x78 'x'
		  (   809,   9,  11,  11,    1,   -7 ),   ## 0x79 'y'
		  (   822,   7,   8,  11,    2,   -7 ),   ## 0x7A 'z'
		  (   829,   3,  13,  11,    4,  -10 ),   ## 0x7B '('
		  (   834,   1,  13,  11,    5,  -10 ),   ## 0x7C '|'
		  (   836,   3,  13,  11,    4,  -10 ),   ## 0x7D ')'
		  (   841,   7,   3,  11,    2,   -6 ) ) ## 0x7E '~'


		self.GFXfirst =   0x20
		self.GFXlast =  0x7E
		self.GFXyadvance =  18 
		self.GFXMinYadvance = -11
	def __repr__ (self):
		rows = ''
		for y in range(self.height):
			for x in range(self.width):
				rows += '*' if self.pixels[y * self.width + x] else ' '
		rows += '\n'
		return rows