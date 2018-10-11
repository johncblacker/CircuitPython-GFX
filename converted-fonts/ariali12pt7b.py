class GFXfont:
	def __init__(self):
		self.GFXbitmaps = (
		0x18, 0xC6, 0x63, 0x18, 0xC4, 0x23, 0x18, 0x84, 0x00, 0x18, 0xC0, 0x33,
		0x73, 0x66, 0x66, 0x66, 0x46, 0x06, 0x30, 0x61, 0x83, 0x18, 0x18, 0xC0,
		0xC6, 0x7F, 0xFF, 0xFF, 0xE3, 0x18, 0x18, 0xC0, 0xC6, 0x0C, 0x31, 0xFF,
		0xFF, 0xFF, 0x98, 0xC0, 0xC6, 0x0C, 0x30, 0x63, 0x00, 0x00, 0xC0, 0x7C,
		0x1F, 0xE1, 0x9B, 0x31, 0xB3, 0x18, 0x31, 0x83, 0x90, 0x1F, 0x00, 0x78,
		0x03, 0xC0, 0x36, 0xC3, 0x6C, 0x66, 0x66, 0x67, 0x6C, 0x3F, 0xC1, 0xF8,
		0x0C, 0x00, 0xC0, 0x3E, 0x01, 0x9F, 0xC0, 0xC6, 0x30, 0x63, 0x8C, 0x30,
		0xC3, 0x08, 0x31, 0xC6, 0x0C, 0x63, 0x03, 0xF9, 0x80, 0x78, 0x40, 0x00,
		0x23, 0xE0, 0x19, 0xFC, 0x0C, 0x63, 0x06, 0x38, 0xC1, 0x0C, 0x30, 0xC3,
		0x1C, 0x60, 0xC6, 0x30, 0x3F, 0x98, 0x07, 0x80, 0x03, 0xC0, 0x3F, 0x81,
		0xC6, 0x06, 0x18, 0x18, 0x60, 0x63, 0x01, 0xBC, 0x03, 0xC0, 0x3E, 0x01,
		0xDC, 0x0E, 0x38, 0xB0, 0x77, 0xC0, 0xFB, 0x01, 0xCE, 0x1F, 0x9F, 0xE7,
		0x1F, 0x08, 0x6F, 0x6D, 0x80, 0x03, 0x06, 0x0C, 0x18, 0x18, 0x30, 0x30,
		0x60, 0x60, 0x60, 0xC0, 0xC0, 0xC0, 0xC0, 0xC0, 0xC0, 0xC0, 0xC0, 0x60,
		0x60, 0x60, 0x30, 0x0C, 0x06, 0x06, 0x06, 0x03, 0x03, 0x03, 0x03, 0x03,
		0x03, 0x03, 0x03, 0x06, 0x06, 0x06, 0x0C, 0x0C, 0x18, 0x18, 0x30, 0x60,
		0xC0, 0x18, 0x18, 0xFF, 0x3C, 0x3C, 0x66, 0x24, 0x06, 0x00, 0x60, 0x06,
		0x00, 0x60, 0x06, 0x0F, 0xFF, 0xFF, 0xF0, 0x60, 0x06, 0x00, 0x60, 0x06,
		0x00, 0x60, 0x6C, 0x95, 0x00, 0xFF, 0xFC, 0x6C, 0x00, 0x60, 0x18, 0x03,
		0x00, 0xC0, 0x18, 0x06, 0x00, 0x80, 0x30, 0x04, 0x01, 0x80, 0x20, 0x0C,
		0x03, 0x00, 0x60, 0x18, 0x03, 0x00, 0xC0, 0x00, 0x07, 0x80, 0xFE, 0x1C,
		0x63, 0x83, 0x30, 0x36, 0x03, 0x60, 0x3E, 0x03, 0xC0, 0x3C, 0x07, 0xC0,
		0x6C, 0x06, 0xC0, 0xCC, 0x1C, 0x63, 0x87, 0xF0, 0x1E, 0x00, 0x03, 0x07,
		0x0E, 0x3E, 0xF6, 0xC6, 0x04, 0x0C, 0x0C, 0x0C, 0x08, 0x18, 0x18, 0x18,
		0x10, 0x30, 0x30, 0x07, 0x80, 0xFE, 0x1C, 0x63, 0x83, 0x30, 0x30, 0x03,
		0x00, 0x70, 0x06, 0x01, 0xC0, 0x38, 0x07, 0x00, 0xE0, 0x38, 0x03, 0x00,
		0x60, 0x0F, 0xFE, 0xFF, 0xE0, 0x07, 0xC0, 0xFE, 0x18, 0x73, 0x03, 0x10,
		0x30, 0x03, 0x00, 0x60, 0x7C, 0x07, 0xC0, 0x0C, 0x00, 0x60, 0x06, 0xC0,
		0x6C, 0x0E, 0x61, 0xC7, 0xF8, 0x1F, 0x00, 0x00, 0x30, 0x07, 0x00, 0xE0,
		0x1E, 0x03, 0x60, 0x66, 0x0C, 0x41, 0x8C, 0x30, 0xC6, 0x0C, 0xC1, 0x8F,
		0xFE, 0xFF, 0xE0, 0x18, 0x01, 0x80, 0x30, 0x03, 0x00, 0x0F, 0xF0, 0x7F,
		0x83, 0x00, 0x30, 0x01, 0x80, 0x0D, 0xE0, 0x7F, 0x87, 0x0E, 0x30, 0x30,
		0x01, 0x80, 0x0C, 0x00, 0x6C, 0x07, 0x60, 0x31, 0x87, 0x0F, 0xF0, 0x1F,
		0x00, 0x07, 0x83, 0xF8, 0x63, 0x98, 0x37, 0x00, 0xDE, 0x1F, 0xE7, 0x8E,
		0xE0, 0xD8, 0x1B, 0x03, 0x60, 0x6C, 0x1D, 0x83, 0x18, 0xE3, 0xF8, 0x1E,
		0x00, 0x7F, 0xFF, 0xFC, 0x03, 0x00, 0xC0, 0x30, 0x06, 0x01, 0x80, 0x60,
		0x0C, 0x03, 0x00, 0x60, 0x0C, 0x03, 0x00, 0x60, 0x0C, 0x03, 0x00, 0x60,
		0x00, 0x07, 0xC1, 0xFE, 0x18, 0x73, 0x03, 0x30, 0x33, 0x03, 0x18, 0x61,
		0xFC, 0x3F, 0xC7, 0x0E, 0xE0, 0x6C, 0x06, 0xC0, 0x6C, 0x0E, 0xE1, 0xC7,
		0xF8, 0x1F, 0x00, 0x0F, 0x03, 0xF8, 0xE3, 0x18, 0x36, 0x06, 0xC0, 0xD8,
		0x1B, 0x03, 0x60, 0xEE, 0x3C, 0xFF, 0x0F, 0x60, 0x1D, 0x83, 0x38, 0xC3,
		0xF8, 0x3C, 0x00, 0x18, 0xC0, 0x00, 0x00, 0x00, 0x00, 0x00, 0xC6, 0x00,
		0x18, 0xC0, 0x00, 0x00, 0x00, 0x00, 0x00, 0xC6, 0x10, 0x88, 0x80, 0x00,
		0x20, 0x1C, 0x0F, 0x0F, 0x07, 0x81, 0x80, 0x1E, 0x00, 0xF0, 0x07, 0xC0,
		0x1C, 0x00, 0x80, 0xFF, 0xFF, 0xFC, 0x00, 0x00, 0x00, 0x01, 0xFF, 0xFF,
		0xF8, 0x80, 0x1C, 0x01, 0xF0, 0x07, 0x80, 0x3C, 0x00, 0xC0, 0xF0, 0x78,
		0x78, 0x1C, 0x02, 0x00, 0x00, 0x1F, 0x1F, 0xE6, 0x1F, 0x03, 0x00, 0xC0,
		0x60, 0x38, 0x1C, 0x0E, 0x07, 0x01, 0x80, 0xC0, 0x30, 0x00, 0x00, 0x01,
		0x80, 0x60, 0x00, 0x00, 0xFE, 0x00, 0x1F, 0xFE, 0x00, 0xF0, 0x3C, 0x07,
		0x00, 0x38, 0x38, 0xF3, 0x70, 0xC7, 0xEC, 0xC6, 0x38, 0xE1, 0x99, 0x81,
		0x86, 0xC6, 0x06, 0x1B, 0x30, 0x18, 0x6C, 0xC0, 0x61, 0xB3, 0x01, 0x8E,
		0xCC, 0x0E, 0x33, 0x30, 0x31, 0xCC, 0x63, 0xCE, 0x19, 0xFF, 0xF0, 0x61,
		0xC7, 0x00, 0xC0, 0x00, 0x73, 0x80, 0x07, 0x87, 0xC0, 0x7C, 0x07, 0xFF,
		0xC0, 0x03, 0xFC, 0x00, 0x00, 0x38, 0x00, 0x38, 0x00, 0x6C, 0x00, 0x6C,
		0x00, 0xCC, 0x00, 0xCC, 0x01, 0x8C, 0x03, 0x0C, 0x03, 0x0E, 0x06, 0x06,
		0x07, 0xFE, 0x0F, 0xFE, 0x1C, 0x06, 0x18, 0x06, 0x30, 0x07, 0x30, 0x03,
		0x60, 0x03, 0x0F, 0xF0, 0x3F, 0xE0, 0x81, 0xC6, 0x03, 0x18, 0x0C, 0x60,
		0x31, 0x01, 0x8F, 0xFC, 0x3F, 0xF8, 0xC0, 0x63, 0x00, 0xD8, 0x03, 0x60,
		0x0D, 0x80, 0x76, 0x03, 0xBF, 0xFC, 0xFF, 0xE0, 0x03, 0xF0, 0x1F, 0xF0,
		0x70, 0x71, 0xC0, 0x77, 0x00, 0x6C, 0x00, 0x38, 0x00, 0x60, 0x00, 0xC0,
		0x01, 0x80, 0x03, 0x00, 0x06, 0x00, 0x6C, 0x01, 0x8C, 0x07, 0x1C, 0x1C,
		0x1F, 0xF0, 0x0F, 0x80, 0x0F, 0xF0, 0x0F, 0xFC, 0x18, 0x0E, 0x18, 0x06,
		0x18, 0x03, 0x18, 0x03, 0x38, 0x03, 0x30, 0x03, 0x30, 0x03, 0x30, 0x03,
		0x30, 0x06, 0x60, 0x06, 0x60, 0x0E, 0x60, 0x1C, 0x60, 0x38, 0xFF, 0xF0,
		0xFF, 0xC0, 0x0F, 0xFF, 0x0F, 0xFF, 0x18, 0x00, 0x18, 0x00, 0x18, 0x00,
		0x18, 0x00, 0x38, 0x00, 0x3F, 0xFE, 0x3F, 0xFC, 0x30, 0x00, 0x30, 0x00,
		0x60, 0x00, 0x60, 0x00, 0x60, 0x00, 0x60, 0x00, 0xFF, 0xF8, 0xFF, 0xF8,
		0x0F, 0xFE, 0x0F, 0xFC, 0x1C, 0x00, 0x18, 0x00, 0x18, 0x00, 0x18, 0x00,
		0x38, 0x00, 0x3F, 0xFC, 0x3F, 0xF8, 0x30, 0x00, 0x30, 0x00, 0x60, 0x00,
		0x60, 0x00, 0x60, 0x00, 0x60, 0x00, 0xC0, 0x00, 0xC0, 0x00, 0x03, 0xF8,
		0x07, 0xFE, 0x07, 0x83, 0x87, 0x00, 0x63, 0x00, 0x33, 0x00, 0x01, 0x80,
		0x01, 0x80, 0x00, 0xC0, 0xFF, 0x60, 0x7F, 0x30, 0x01, 0x98, 0x00, 0xCC,
		0x00, 0x63, 0x00, 0x61, 0xE0, 0xF0, 0x7F, 0xF0, 0x0F, 0xE0, 0x00, 0x0C,
		0x01, 0x86, 0x00, 0xC6, 0x00, 0xC3, 0x00, 0x61, 0x80, 0x30, 0xC0, 0x18,
		0xE0, 0x18, 0x7F, 0xFC, 0x3F, 0xFE, 0x18, 0x03, 0x0C, 0x01, 0x0C, 0x01,
		0x86, 0x00, 0xC3, 0x00, 0x61, 0x80, 0x21, 0x80, 0x30, 0xC0, 0x18, 0x00,
		0x0C, 0x18, 0x60, 0xC1, 0x83, 0x0E, 0x18, 0x30, 0x60, 0xC3, 0x06, 0x0C,
		0x18, 0x60, 0xC0, 0x00, 0x30, 0x01, 0x80, 0x18, 0x00, 0xC0, 0x06, 0x00,
		0x30, 0x03, 0x00, 0x18, 0x00, 0xC0, 0x06, 0x00, 0x61, 0x83, 0x0C, 0x18,
		0x60, 0xC3, 0x8C, 0x0F, 0xE0, 0x3C, 0x00, 0x0C, 0x03, 0x06, 0x07, 0x07,
		0x07, 0x03, 0x07, 0x01, 0x87, 0x00, 0xC6, 0x00, 0xE6, 0x00, 0x6F, 0x00,
		0x3F, 0x80, 0x1E, 0x60, 0x0E, 0x38, 0x0E, 0x0C, 0x06, 0x07, 0x03, 0x01,
		0x81, 0x80, 0x61, 0x80, 0x38, 0xC0, 0x0C, 0x00, 0x0C, 0x01, 0x80, 0x60,
		0x0C, 0x01, 0x80, 0x30, 0x0E, 0x01, 0x80, 0x30, 0x06, 0x00, 0xC0, 0x30,
		0x06, 0x00, 0xC0, 0x18, 0x07, 0xFF, 0xFF, 0xC0, 0x0E, 0x00, 0xF0, 0xF0,
		0x0F, 0x1F, 0x01, 0xA1, 0xB0, 0x1A, 0x1B, 0x03, 0x61, 0xB0, 0x36, 0x1B,
		0x06, 0x61, 0x98, 0x66, 0x39, 0x8C, 0xC3, 0x18, 0xCC, 0x31, 0x9C, 0xC3,
		0x19, 0x8C, 0x31, 0x98, 0xC3, 0x0F, 0x08, 0x60, 0xF1, 0x86, 0x0E, 0x18,
		0x60, 0xE1, 0x80, 0x0C, 0x03, 0x0E, 0x03, 0x1E, 0x03, 0x1E, 0x06, 0x1B,
		0x06, 0x1B, 0x06, 0x3B, 0x86, 0x31, 0x86, 0x31, 0x8E, 0x31, 0xCC, 0x30,
		0xCC, 0x60, 0xCC, 0x60, 0xEC, 0x60, 0x6C, 0x60, 0x7C, 0xC0, 0x78, 0xC0,
		0x38, 0x03, 0xF0, 0x07, 0xFE, 0x07, 0x83, 0x87, 0x00, 0xE7, 0x00, 0x3B,
		0x00, 0x0F, 0x80, 0x07, 0x80, 0x03, 0xC0, 0x01, 0xE0, 0x00, 0xF0, 0x00,
		0xD8, 0x00, 0x6E, 0x00, 0x73, 0x00, 0x70, 0xE0, 0xF0, 0x3F, 0xF0, 0x07,
		0xE0, 0x00, 0x0F, 0xFC, 0x0F, 0xFE, 0x1C, 0x07, 0x18, 0x03, 0x18, 0x03,
		0x18, 0x03, 0x38, 0x06, 0x30, 0x0E, 0x3F, 0xFC, 0x3F, 0xF0, 0x30, 0x00,
		0x60, 0x00, 0x60, 0x00, 0x60, 0x00, 0x60, 0x00, 0xC0, 0x00, 0xC0, 0x00,
		0x03, 0xF0, 0x07, 0xFE, 0x07, 0x83, 0x87, 0x00, 0x67, 0x00, 0x3B, 0x00,
		0x0F, 0x80, 0x07, 0x80, 0x03, 0xC0, 0x01, 0xE0, 0x00, 0xF0, 0x00, 0xF8,
		0x10, 0xE6, 0x1C, 0x73, 0x07, 0xF0, 0xE1, 0xF0, 0x3F, 0xF8, 0x07, 0xEE,
		0x00, 0x03, 0x00, 0x00, 0x80, 0x0F, 0xFC, 0x0F, 0xFE, 0x18, 0x07, 0x18,
		0x03, 0x18, 0x03, 0x18, 0x07, 0x38, 0x0E, 0x3F, 0xFC, 0x3F, 0xF8, 0x30,
		0x60, 0x30, 0x30, 0x60, 0x30, 0x60, 0x18, 0x60, 0x18, 0x60, 0x0C, 0xC0,
		0x0C, 0xC0, 0x06, 0x07, 0xE0, 0x7F, 0xE3, 0x83, 0x8C, 0x03, 0x30, 0x0C,
		0xC0, 0x01, 0xC0, 0x03, 0xC0, 0x07, 0xC0, 0x03, 0xC0, 0x03, 0xB0, 0x06,
		0xC0, 0x1B, 0x80, 0x67, 0x07, 0x0F, 0xF8, 0x1F, 0x80, 0xFF, 0xFF, 0xFF,
		0xF0, 0x30, 0x00, 0xC0, 0x02, 0x00, 0x18, 0x00, 0x60, 0x01, 0x80, 0x06,
		0x00, 0x10, 0x00, 0xC0, 0x03, 0x00, 0x0C, 0x00, 0x30, 0x00, 0x80, 0x06,
		0x00, 0x18, 0x00, 0x18, 0x06, 0x30, 0x0C, 0xC0, 0x31, 0x80, 0x63, 0x00,
		0xC6, 0x01, 0x98, 0x03, 0x30, 0x0C, 0x60, 0x19, 0xC0, 0x33, 0x00, 0x66,
		0x01, 0xCC, 0x03, 0x18, 0x0E, 0x18, 0x38, 0x3F, 0xE0, 0x1F, 0x80, 0x60,
		0x06, 0x60, 0x06, 0x60, 0x0C, 0x60, 0x0C, 0x60, 0x18, 0x30, 0x38, 0x30,
		0x30, 0x30, 0x70, 0x30, 0x60, 0x30, 0xC0, 0x18, 0xC0, 0x19, 0x80, 0x19,
		0x80, 0x1B, 0x00, 0x1B, 0x00, 0x0E, 0x00, 0x0E, 0x00, 0xC0, 0x38, 0x06,
		0xC0, 0x38, 0x06, 0xC0, 0x78, 0x0C, 0xC0, 0x78, 0x1C, 0xC0, 0xD8, 0x18,
		0xC0, 0xD8, 0x38, 0xE1, 0x9C, 0x30, 0xE3, 0x9C, 0x70, 0xE3, 0x1C, 0x60,
		0xE7, 0x1C, 0xE0, 0x66, 0x1C, 0xC0, 0x6E, 0x0D, 0x80, 0x6C, 0x0D, 0x80,
		0x7C, 0x0F, 0x00, 0x78, 0x0F, 0x00, 0x70, 0x0E, 0x00, 0x70, 0x0E, 0x00,
		0x06, 0x00, 0x70, 0x38, 0x07, 0x00, 0xC0, 0x70, 0x03, 0x07, 0x00, 0x18,
		0x70, 0x00, 0x67, 0x00, 0x03, 0x70, 0x00, 0x0F, 0x00, 0x00, 0x70, 0x00,
		0x07, 0x80, 0x00, 0x7E, 0x00, 0x06, 0x30, 0x00, 0x60, 0xC0, 0x06, 0x06,
		0x00, 0x60, 0x18, 0x06, 0x00, 0xE0, 0x60, 0x03, 0x00, 0xE0, 0x0E, 0x60,
		0x0C, 0x70, 0x18, 0x30, 0x38, 0x38, 0x30, 0x18, 0x60, 0x1C, 0xE0, 0x0D,
		0xC0, 0x0F, 0x80, 0x07, 0x00, 0x03, 0x00, 0x06, 0x00, 0x06, 0x00, 0x06,
		0x00, 0x06, 0x00, 0x0C, 0x00, 0x0C, 0x00, 0x1F, 0xFC, 0xFF, 0xF0, 0x01,
		0xC0, 0x0E, 0x00, 0x70, 0x03, 0x80, 0x0C, 0x00, 0x60, 0x03, 0x00, 0x18,
		0x00, 0xC0, 0x07, 0x00, 0x38, 0x01, 0xC0, 0x0E, 0x00, 0x3F, 0xFE, 0xFF,
		0xF8, 0x0F, 0x87, 0xC3, 0x01, 0x01, 0x80, 0xC0, 0x60, 0x30, 0x10, 0x18,
		0x0C, 0x06, 0x03, 0x01, 0x01, 0x80, 0xC0, 0x60, 0x30, 0x10, 0x18, 0x0F,
		0x87, 0xC0, 0xC3, 0x0C, 0x18, 0x61, 0x86, 0x18, 0x70, 0xC3, 0x0C, 0x30,
		0xC1, 0x86, 0x18, 0x0F, 0x83, 0xE0, 0x18, 0x06, 0x03, 0x80, 0xC0, 0x30,
		0x0C, 0x03, 0x01, 0x80, 0x60, 0x18, 0x06, 0x03, 0x80, 0xC0, 0x30, 0x0C,
		0x03, 0x01, 0x80, 0x60, 0xF8, 0x3E, 0x00, 0x0C, 0x07, 0x81, 0xE0, 0xCC,
		0x33, 0x0C, 0xC6, 0x19, 0x86, 0xC0, 0xC0, 0xFF, 0xFF, 0xFF, 0xF0, 0xE6,
		0x63, 0x0F, 0x87, 0xF8, 0xC3, 0xB0, 0x30, 0x06, 0x3F, 0xDF, 0xFF, 0x06,
		0xC0, 0xD8, 0x1B, 0x8F, 0x3F, 0xE3, 0xCC, 0x0C, 0x00, 0xC0, 0x18, 0x01,
		0x80, 0x1B, 0xC1, 0xFE, 0x3C, 0x73, 0x83, 0x30, 0x33, 0x03, 0x20, 0x36,
		0x03, 0x60, 0x66, 0x06, 0x71, 0xCD, 0xF8, 0xCF, 0x00, 0x0F, 0x83, 0xF8,
		0xE3, 0xB0, 0x36, 0x01, 0x80, 0x30, 0x06, 0x00, 0xC0, 0xD8, 0x33, 0x8E,
		0x3F, 0x83, 0xE0, 0x00, 0x18, 0x00, 0xC0, 0x0E, 0x00, 0x60, 0xF3, 0x0F,
		0xD8, 0xE3, 0xCE, 0x0E, 0x60, 0x76, 0x03, 0x30, 0x19, 0x80, 0xCC, 0x06,
		0x60, 0x73, 0x87, 0x0F, 0xF8, 0x3E, 0xC0, 0x0F, 0x81, 0xFE, 0x38, 0x66,
		0x03, 0x60, 0x3F, 0xFF, 0xFF, 0xFC, 0x00, 0xC0, 0x0C, 0x06, 0x61, 0xC7,
		0xF8, 0x1F, 0x00, 0x0F, 0x8F, 0x86, 0x03, 0x0F, 0xE7, 0xF0, 0xC0, 0x60,
		0x30, 0x18, 0x18, 0x0C, 0x06, 0x03, 0x01, 0x01, 0x80, 0xC0, 0x00, 0x0F,
		0x30, 0xFD, 0x8E, 0x3C, 0xC0, 0xE6, 0x07, 0x60, 0x33, 0x01, 0x98, 0x0C,
		0xC0, 0x66, 0x07, 0x18, 0x70, 0xFF, 0x81, 0xEC, 0x00, 0x63, 0x06, 0x18,
		0x70, 0x7F, 0x01, 0xF0, 0x00, 0x0C, 0x00, 0xC0, 0x18, 0x01, 0x80, 0x19,
		0xC1, 0xFE, 0x3C, 0x63, 0x86, 0x30, 0x63, 0x06, 0x30, 0xE6, 0x0C, 0x60,
		0xC6, 0x0C, 0x60, 0xCC, 0x18, 0xC1, 0x80, 0x0C, 0x18, 0x00, 0x01, 0x83,
		0x0E, 0x18, 0x30, 0x60, 0xC3, 0x06, 0x0C, 0x18, 0x60, 0xC0, 0x00, 0xC0,
		0x18, 0x00, 0x00, 0x00, 0x18, 0x03, 0x00, 0x40, 0x18, 0x03, 0x00, 0x60,
		0x0C, 0x03, 0x00, 0x60, 0x0C, 0x01, 0x80, 0x60, 0x0C, 0x01, 0x80, 0x30,
		0x0C, 0x0F, 0x81, 0xE0, 0x00, 0x0C, 0x00, 0xC0, 0x1C, 0x01, 0x80, 0x18,
		0x61, 0x8C, 0x39, 0x83, 0x30, 0x36, 0x03, 0xE0, 0x3B, 0x07, 0x30, 0x63,
		0x06, 0x18, 0x61, 0x8C, 0x1C, 0xC0, 0xC0, 0x0C, 0x18, 0x60, 0xC1, 0x83,
		0x0E, 0x18, 0x30, 0x60, 0xC3, 0x06, 0x0C, 0x18, 0x60, 0xC0, 0x19, 0xC7,
		0x83, 0xFD, 0xF8, 0xD1, 0xE3, 0x1C, 0x38, 0x63, 0x06, 0x0C, 0x60, 0xC1,
		0x9C, 0x18, 0x33, 0x06, 0x0C, 0x60, 0xC1, 0x8C, 0x18, 0x31, 0x83, 0x06,
		0x60, 0xC1, 0x8C, 0x18, 0x30, 0x19, 0xC1, 0xFE, 0x3C, 0x63, 0x86, 0x30,
		0x63, 0x06, 0x30, 0x66, 0x0C, 0x60, 0xC6, 0x0C, 0x60, 0xCC, 0x18, 0xC1,
		0x80, 0x0F, 0x81, 0xFE, 0x38, 0x67, 0x03, 0x60, 0x3C, 0x03, 0xC0, 0x3C,
		0x03, 0xC0, 0x6C, 0x0E, 0x61, 0xC7, 0xF8, 0x1F, 0x00, 0x0C, 0xE0, 0x7F,
		0x87, 0x8E, 0x38, 0x31, 0x81, 0x8C, 0x0C, 0x60, 0x66, 0x03, 0x30, 0x31,
		0x81, 0x8E, 0x18, 0xDF, 0x86, 0x78, 0x30, 0x01, 0x80, 0x0C, 0x00, 0xC0,
		0x06, 0x00, 0x00, 0x0F, 0x31, 0xFD, 0x8C, 0x2C, 0xC1, 0xC6, 0x06, 0x60,
		0x33, 0x03, 0x98, 0x18, 0xC0, 0xC6, 0x0E, 0x38, 0xF0, 0xFF, 0x03, 0xD8,
		0x00, 0xC0, 0x06, 0x00, 0x70, 0x03, 0x00, 0x18, 0x00, 0x19, 0xC6, 0xE1,
		0xC0, 0xE0, 0x30, 0x0C, 0x03, 0x01, 0x80, 0x60, 0x18, 0x06, 0x03, 0x00,
		0xC0, 0x00, 0x0F, 0x83, 0xF8, 0xE3, 0x98, 0x33, 0x80, 0x3C, 0x01, 0xE0,
		0x0E, 0xC0, 0xD8, 0x1B, 0x87, 0x3F, 0xC1, 0xF0, 0x04, 0x18, 0x60, 0xC7,
		0xEF, 0xC6, 0x0C, 0x30, 0x60, 0xC3, 0x06, 0x0C, 0x18, 0x3C, 0x78, 0x18,
		0x30, 0xC1, 0x8E, 0x1C, 0x60, 0xC3, 0x06, 0x18, 0x31, 0xC1, 0x8C, 0x18,
		0x60, 0xC3, 0x0E, 0x18, 0xF0, 0xFF, 0x03, 0x98, 0x00, 0xC0, 0x6C, 0x0C,
		0xC0, 0xCE, 0x18, 0x61, 0x86, 0x30, 0x63, 0x06, 0x60, 0x66, 0x02, 0xC0,
		0x3C, 0x03, 0x80, 0x38, 0x00, 0xC1, 0x83, 0x60, 0xC1, 0xB0, 0xE0, 0x98,
		0x70, 0xC6, 0x2C, 0x63, 0x36, 0x61, 0x93, 0x30, 0xC8, 0x90, 0x6C, 0x58,
		0x34, 0x28, 0x0A, 0x14, 0x07, 0x0E, 0x03, 0x06, 0x00, 0x30, 0x31, 0x86,
		0x18, 0xC0, 0xD8, 0x0D, 0x80, 0x70, 0x06, 0x00, 0xE0, 0x1B, 0x01, 0xB0,
		0x31, 0x86, 0x18, 0xC0, 0xC0, 0x30, 0x18, 0xC0, 0xC3, 0x03, 0x06, 0x18,
		0x18, 0x60, 0x63, 0x01, 0x8C, 0x06, 0x60, 0x19, 0x80, 0x2C, 0x00, 0xB0,
		0x03, 0x80, 0x0E, 0x00, 0x30, 0x01, 0xC0, 0x06, 0x00, 0xF0, 0x03, 0x80,
		0x00, 0x3F, 0xE7, 0xFC, 0x03, 0x00, 0xC0, 0x30, 0x0E, 0x03, 0x80, 0xE0,
		0x18, 0x06, 0x01, 0x80, 0x7F, 0xCF, 0xF8, 0x03, 0x83, 0xC3, 0x81, 0x80,
		0xC0, 0x40, 0x60, 0x30, 0x18, 0x18, 0x38, 0x1C, 0x07, 0x01, 0x80, 0xC0,
		0x60, 0x30, 0x30, 0x18, 0x0C, 0x07, 0x81, 0xC0, 0xFF, 0xFF, 0xFF, 0xFF,
		0xFF, 0xF0, 0x07, 0x03, 0x80, 0xC0, 0x60, 0x30, 0x30, 0x18, 0x0C, 0x06,
		0x03, 0x80, 0xE0, 0x70, 0x60, 0x60, 0x30, 0x18, 0x1C, 0x0C, 0x06, 0x03,
		0x0F, 0x07, 0x00, 0x78, 0x0F, 0xE3, 0xC7, 0xF0, 0x1E )


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
