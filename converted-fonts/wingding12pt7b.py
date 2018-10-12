class GFXfont:
	def __init__(self):
		self.GFXbitmaps = (
		0xFF, 0xFF, 0xC0, 0x03, 0xE0, 0x01, 0xF0, 0x00, 0xF8, 0x00, 0x77, 0xFF,
		0xFF, 0xF8, 0xFF, 0xF8, 0x3F, 0xFC, 0x1F, 0xFE, 0x0F, 0xFF, 0x8F, 0xFF,
		0xFF, 0xFF, 0xF7, 0xFF, 0xFB, 0xFF, 0xFD, 0xFF, 0xFE, 0xFF, 0xFF, 0xFF,
		0x80, 0x03, 0xF0, 0x03, 0x03, 0x01, 0x0C, 0x20, 0x83, 0x04, 0x40, 0xC0,
		0x90, 0x30, 0x28, 0x00, 0x06, 0x02, 0x01, 0x81, 0xC0, 0x61, 0x74, 0x18,
		0xC9, 0xC6, 0x78, 0x79, 0x48, 0x0C, 0x90, 0x00, 0x22, 0x00, 0x10, 0x40,
		0x08, 0x0C, 0x0C, 0x00, 0xFC, 0x00, 0x00, 0x00, 0x10, 0x00, 0x06, 0x00,
		0x00, 0xC0, 0x3F, 0xB0, 0x04, 0x06, 0x00, 0x49, 0xC0, 0x09, 0x74, 0x00,
		0xAE, 0x20, 0x0D, 0xA1, 0x00, 0x7C, 0x08, 0x18, 0x00, 0x86, 0xFC, 0x08,
		0x83, 0xBF, 0x00, 0x80, 0x00, 0x06, 0x00, 0x00, 0x30, 0x00, 0x00, 0xDF,
		0xC0, 0x06, 0x04, 0x00, 0x39, 0x20, 0x04, 0xEA, 0x00, 0x47, 0x50, 0x08,
		0x5D, 0x01, 0x03, 0xE0, 0x10, 0x01, 0x81, 0x03, 0xF6, 0x0F, 0xDC, 0x10,
		0x30, 0x0C, 0x33, 0x14, 0xA5, 0x2A, 0x4A, 0xA2, 0xC8, 0xB2, 0x7C, 0x96,
		0xAD, 0xDA, 0xB2, 0xAC, 0xB6, 0x2A, 0x12, 0x04, 0x42, 0x08, 0x81, 0xC0,
		0x04, 0x00, 0x0C, 0x40, 0xCB, 0xC0, 0xB9, 0x40, 0x5D, 0x40, 0x25, 0x40,
		0x12, 0xC0, 0x0D, 0x40, 0x13, 0xC0, 0x20, 0x40, 0x4E, 0x20, 0x51, 0x10,
		0x51, 0x08, 0x7B, 0x08, 0x64, 0x04, 0x30, 0x02, 0x0F, 0x02, 0x00, 0xC1,
		0x00, 0x32, 0x00, 0x0C, 0x08, 0x01, 0x80, 0x14, 0x01, 0x40, 0x12, 0x00,
		0x90, 0x09, 0x03, 0x88, 0xC0, 0x69, 0x81, 0xA4, 0x1F, 0xC1, 0x7A, 0x14,
		0x66, 0x3A, 0x81, 0xF0, 0x0F, 0x81, 0x5C, 0x66, 0x28, 0x5E, 0x86, 0xF8,
		0x32, 0x81, 0xD6, 0x03, 0x11, 0xC1, 0x10, 0x09, 0x00, 0x50, 0x02, 0x80,
		0x28, 0x02, 0x80, 0x10, 0x00, 0x7C, 0x1F, 0xF0, 0x7A, 0x09, 0x80, 0xBF,
		0xFC, 0x10, 0x10, 0x82, 0x03, 0xE8, 0x40, 0x22, 0x30, 0x07, 0xA8, 0x00,
		0x7E, 0x00, 0x07, 0xC0, 0x0F, 0x07, 0xFA, 0x03, 0x40, 0xC1, 0xFF, 0xE8,
		0x21, 0x01, 0x0B, 0xE0, 0x18, 0x88, 0x00, 0xAF, 0x00, 0x0F, 0xC0, 0x00,
		0x03, 0x02, 0x81, 0x40, 0xA0, 0x50, 0x28, 0x14, 0x3E, 0x75, 0x6B, 0x75,
		0xBA, 0x9A, 0xCE, 0x86, 0x04, 0x82, 0x21, 0x10, 0x87, 0x80, 0x3C, 0x21,
		0x10, 0x88, 0x24, 0x0C, 0x2E, 0x6B, 0x33, 0xB5, 0xDA, 0xD5, 0xCB, 0x87,
		0x02, 0x81, 0x40, 0xA0, 0x50, 0x28, 0x18, 0x00, 0x01, 0x80, 0x0D, 0x4C,
		0x05, 0xAA, 0x02, 0xD5, 0x0D, 0x6A, 0x85, 0x76, 0x82, 0xBB, 0x40, 0xB9,
		0xA0, 0x4C, 0x10, 0x16, 0x13, 0x84, 0x09, 0x22, 0x03, 0x61, 0x06, 0x40,
		0x80, 0x40, 0x40, 0x40, 0x10, 0x40, 0x04, 0x40, 0x02, 0x20, 0x00, 0xE0,
		0x00, 0x03, 0xF0, 0x03, 0x03, 0x01, 0x00, 0x20, 0x80, 0x04, 0x40, 0x00,
		0x91, 0x86, 0x28, 0x61, 0x86, 0x00, 0x01, 0x80, 0x00, 0x62, 0x01, 0x18,
		0x80, 0x46, 0x10, 0x21, 0x44, 0x08, 0x90, 0x84, 0x22, 0x1E, 0x10, 0x40,
		0x08, 0x0C, 0x0C, 0x00, 0xFC, 0x00, 0x03, 0xF0, 0x03, 0x03, 0x01, 0x00,
		0x20, 0x80, 0x04, 0x40, 0x00, 0x91, 0x86, 0x28, 0x61, 0x86, 0x00, 0x01,
		0x80, 0x00, 0x60, 0x00, 0x18, 0x00, 0x06, 0x3F, 0xF1, 0x40, 0x00, 0x90,
		0x00, 0x22, 0x00, 0x10, 0x40, 0x08, 0x0C, 0x0C, 0x00, 0xFC, 0x00, 0x03,
		0xF0, 0x03, 0x03, 0x01, 0x00, 0x20, 0x80, 0x04, 0x40, 0x00, 0x91, 0x86,
		0x28, 0x61, 0x86, 0x00, 0x01, 0x80, 0x00, 0x60, 0x78, 0x18, 0x61, 0x86,
		0x10, 0x21, 0x48, 0x04, 0x92, 0x01, 0x22, 0x00, 0x10, 0x40, 0x08, 0x0C,
		0x0C, 0x00, 0xFC, 0x00, 0x00, 0x00, 0x22, 0x01, 0xE2, 0x24, 0x02, 0x31,
		0x28, 0x02, 0x0C, 0x00, 0x0F, 0x06, 0x04, 0x0F, 0x01, 0xE0, 0x1F, 0x80,
		0x44, 0x7F, 0xE0, 0x93, 0x7F, 0xE0, 0x80, 0xFF, 0xF0, 0x80, 0xFF, 0xF0,
		0x00, 0xFF, 0xF0, 0x00, 0xFF, 0xF0, 0x00, 0xFF, 0xF0, 0x00, 0x7F, 0xE0,
		0x00, 0x7F, 0xE0, 0x00, 0x3F, 0xC0, 0x00, 0x0F, 0x00, 0x00, 0x0F, 0x01,
		0xF8, 0x3F, 0xC3, 0xFC, 0x26, 0x42, 0x64, 0x1F, 0x81, 0x98, 0x0F, 0x01,
		0x10, 0x0F, 0x0C, 0x03, 0xF9, 0xF0, 0xF0, 0x1F, 0x03, 0x0C, 0xE0, 0x7E,
		0x06, 0x80, 0x00, 0x8F, 0x00, 0xB0, 0xC0, 0xC0, 0x40, 0x80, 0x40, 0x80,
		0x40, 0x80, 0x43, 0x80, 0x7D, 0x80, 0x41, 0x80, 0x41, 0x80, 0x41, 0x9F,
		0x41, 0xA1, 0xC1, 0xC1, 0x81, 0x81, 0x01, 0x81, 0x83, 0x80, 0xFC, 0x80,
		0x00, 0x80, 0x00, 0x80, 0x00, 0x80, 0x00, 0x00, 0x00, 0x02, 0x00, 0x00,
		0x09, 0xF0, 0x00, 0x3C, 0x20, 0x00, 0xC0, 0x40, 0x02, 0x01, 0x00, 0x0C,
		0x04, 0x00, 0x10, 0x10, 0x00, 0x40, 0x40, 0x01, 0x3D, 0x80, 0x05, 0x29,
		0x80, 0x98, 0xA1, 0xFC, 0x43, 0x00, 0x61, 0x08, 0x03, 0x04, 0x20, 0x70,
		0x10, 0x7F, 0x00, 0x20, 0x00, 0x00, 0x80, 0x00, 0x02, 0x00, 0x00, 0x08,
		0x00, 0x00, 0x03, 0x00, 0x01, 0xC0, 0x00, 0x60, 0x00, 0x38, 0x00, 0x0C,
		0x00, 0x07, 0x00, 0x03, 0xC1, 0x80, 0xE0, 0x7F, 0xFF, 0x3F, 0xFF, 0xD0,
		0x1C, 0x18, 0x0E, 0x00, 0x0E, 0x00, 0x07, 0x00, 0x07, 0x00, 0x03, 0x00,
		0x01, 0x80, 0x01, 0x80, 0x00, 0x00, 0x00, 0x01, 0x80, 0x01, 0x80, 0x1F,
		0xF8, 0x1C, 0x38, 0x10, 0x08, 0x10, 0x08, 0xE0, 0x07, 0x60, 0x06, 0x20,
		0x04, 0x20, 0x04, 0x30, 0x0C, 0x70, 0x0E, 0x0C, 0x30, 0x07, 0xE0, 0x06,
		0x60, 0x04, 0x20, 0x00, 0x00, 0x00, 0x00, 0x40, 0x06, 0x00, 0x60, 0x0F,
		0x01, 0xF0, 0x1F, 0x83, 0xFC, 0x7F, 0xEF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF,
		0xFF, 0xFF, 0x7F, 0xE3, 0xFC, 0x0F, 0x00, 0x00, 0x80, 0x00, 0x40, 0x00,
		0xF8, 0x01, 0x11, 0x0C, 0x88, 0x99, 0xC4, 0x70, 0xD2, 0x59, 0x87, 0xC3,
		0x00, 0x80, 0x61, 0xF0, 0xCD, 0x25, 0x87, 0x11, 0xCC, 0x88, 0x98, 0x44,
		0x40, 0x0F, 0x80, 0x01, 0x00, 0x00, 0x80, 0x00, 0x10, 0x03, 0x0E, 0x39,
		0xE3, 0xBC, 0x1F, 0x80, 0xF0, 0x0F, 0x01, 0xFC, 0x3D, 0xFF, 0x8E, 0x70,
		0x00, 0x00, 0x01, 0x00, 0x06, 0x00, 0x0C, 0x00, 0x18, 0x00, 0x30, 0x00,
		0x60, 0x00, 0xC0, 0x01, 0xC0, 0x63, 0x80, 0xF3, 0x00, 0x36, 0x00, 0x3E,
		0x00, 0x1C, 0x00, 0x1C, 0x00, 0x10, 0x00, 0xFF, 0xFF, 0xFF, 0xFF, 0xF0,
		0x00, 0x78, 0x40, 0x3C, 0x61, 0x9E, 0x33, 0xCF, 0x1D, 0xC7, 0x87, 0xC3,
		0xC3, 0xC1, 0xE1, 0xF0, 0xF0, 0xFC, 0x79, 0xEF, 0xBD, 0xE3, 0x9E, 0x60,
		0x0F, 0x00, 0x07, 0xFF, 0xFF, 0xFF, 0xFF, 0x80, 0x00, 0x00, 0x7F, 0xFF,
		0xFB, 0xFF, 0xFE, 0x60, 0x03, 0xCC, 0x00, 0xD9, 0x80, 0x33, 0x30, 0x06,
		0x66, 0x01, 0x8C, 0xCC, 0x61, 0x9B, 0x9C, 0x33, 0x3F, 0x06, 0x63, 0xC0,
		0xCC, 0x78, 0x19, 0x86, 0x03, 0x30, 0x80, 0x66, 0x00, 0x0C, 0xFF, 0xFF,
		0x9F, 0xFF, 0xF0, 0x07, 0xC0, 0x08, 0x80, 0x11, 0x00, 0x22, 0x0F, 0xC7,
		0xF0, 0x00, 0x60, 0x00, 0xC0, 0x01, 0xFC, 0x7E, 0x08, 0x80, 0x11, 0x00,
		0x22, 0x00, 0x44, 0x00, 0x88, 0x01, 0x10, 0x02, 0x20, 0x07, 0xC0, 0x0F,
		0xC0, 0x23, 0x00, 0x8C, 0x02, 0x30, 0xF8, 0xFE, 0x00, 0x38, 0x00, 0xE0,
		0x03, 0xF8, 0xFC, 0x23, 0xF0, 0x8C, 0x02, 0x30, 0x08, 0xC0, 0x23, 0x00,
		0x8C, 0x02, 0x30, 0x0F, 0xC0, 0x3F, 0x00, 0x03, 0x00, 0x0C, 0x00, 0xFC,
		0x07, 0xF8, 0x3B, 0x70, 0xCC, 0xCF, 0xFF, 0xFF, 0xFF, 0x33, 0x30, 0x6D,
		0x81, 0xFE, 0x00, 0xC0, 0x03, 0x00, 0x0C, 0x00, 0x30, 0x00, 0xC0, 0x03,
		0x00, 0x3F, 0xE0, 0x7C, 0x21, 0xC3, 0x0E, 0x1C, 0x21, 0xF9, 0x3F, 0xFF,
		0xFE, 0x4F, 0xC2, 0x1C, 0x38, 0x61, 0xC2, 0x1F, 0x03, 0xFE, 0x00, 0x01,
		0x00, 0x02, 0x00, 0x0A, 0x00, 0x36, 0x0F, 0xFF, 0xE9, 0x04, 0x9A, 0x0B,
		0x18, 0x0C, 0x30, 0x18, 0x60, 0x31, 0xA0, 0xB2, 0x41, 0x2F, 0xFF, 0xE0,
		0xD8, 0x00, 0xA0, 0x00, 0x80, 0x01, 0x00, 0x03, 0xE0, 0x07, 0x8E, 0x0F,
		0x00, 0x07, 0x00, 0x07, 0x00, 0x03, 0x80, 0x23, 0x80, 0x11, 0xC0, 0x3E,
		0xE0, 0x0E, 0x70, 0x07, 0x38, 0x02, 0x8E, 0x00, 0x07, 0x00, 0x01, 0xC0,
		0x00, 0xF0, 0x00, 0x1E, 0x00, 0x03, 0xF8, 0x00, 0x03, 0xE0, 0x06, 0x0C,
		0x04, 0x01, 0x0C, 0x00, 0x44, 0x00, 0x15, 0xE0, 0x0B, 0xF8, 0x03, 0xE6,
		0x01, 0xF3, 0x0C, 0xF9, 0x86, 0x7F, 0xE0, 0x3F, 0xF0, 0x37, 0xFC, 0x33,
		0xFF, 0xF8, 0xFF, 0xF8, 0x3F, 0xF8, 0x0F, 0xF8, 0x01, 0xF0, 0x00, 0x00,
		0x80, 0x00, 0x60, 0x00, 0x8C, 0x00, 0x3E, 0x01, 0xCE, 0x01, 0xF0, 0x70,
		0x04, 0x7C, 0x02, 0x23, 0x01, 0x70, 0x83, 0xF8, 0x61, 0xA4, 0x30, 0x92,
		0x14, 0x05, 0x0A, 0x02, 0x89, 0x81, 0x7C, 0x61, 0x9C, 0x1F, 0xC0, 0x07,
		0x80, 0x00, 0x00, 0xC0, 0x00, 0x30, 0x03, 0x7F, 0xB0, 0xFF, 0xFC, 0x1C,
		0xCE, 0x07, 0xB7, 0x83, 0x7F, 0xB0, 0xCF, 0xCC, 0xFF, 0x3F, 0xFF, 0xCF,
		0xF3, 0x3F, 0x30, 0xDF, 0xEC, 0x1E, 0xDE, 0x07, 0x33, 0x83, 0xFF, 0xF0,
		0xDF, 0xEC, 0x00, 0xC0, 0x00, 0x30, 0x00, 0x3C, 0x00, 0x3C, 0x7F, 0x00,
		0xC6, 0xE3, 0x00, 0x83, 0xC1, 0x81, 0x83, 0xC1, 0xC3, 0x03, 0xC0, 0xC3,
		0x03, 0xC0, 0xC2, 0x03, 0x40, 0x66, 0x06, 0x60, 0x66, 0x06, 0x00, 0x64,
		0x00, 0x00, 0x24, 0x00, 0x00, 0x3C, 0x00, 0x00, 0x3C, 0x00, 0x00, 0x3C,
		0x00, 0x00, 0x38, 0x00, 0x00, 0x18, 0x00, 0x00, 0x18, 0x00, 0x00, 0x18,
		0x00, 0x00, 0x18, 0x00, 0x00, 0x18, 0x00, 0x00, 0x18, 0x00, 0x00, 0x18,
		0x00, 0xC0, 0x00, 0x39, 0x80, 0x03, 0x0C, 0x00, 0x18, 0x30, 0x01, 0x81,
		0xC0, 0x1C, 0x06, 0x00, 0xC0, 0x18, 0x0C, 0x00, 0xE0, 0xE0, 0x03, 0xFE,
		0x00, 0x38, 0x38, 0x03, 0x00, 0x60, 0x10, 0x01, 0x01, 0x80, 0x0C, 0x08,
		0x00, 0x20, 0x40, 0x01, 0x02, 0x00, 0x08, 0x10, 0x00, 0x40, 0x40, 0x04,
		0x02, 0x00, 0x20, 0x08, 0x02, 0x00, 0x30, 0x60, 0x00, 0x7C, 0x00, 0xE0,
		0x00, 0xE7, 0xFF, 0xF0, 0x30, 0x30, 0x06, 0x06, 0x00, 0xC0, 0xC0, 0x18,
		0x18, 0x03, 0x03, 0x00, 0x60, 0x60, 0x0C, 0x0C, 0x01, 0x81, 0x80, 0x30,
		0x30, 0x06, 0x06, 0x00, 0xC0, 0xC0, 0x18, 0x18, 0x03, 0x03, 0x00, 0x60,
		0x60, 0x0C, 0x0C, 0x07, 0xFF, 0xE3, 0x80, 0x03, 0x80, 0x01, 0xFF, 0x00,
		0x3F, 0xFF, 0xC1, 0xE0, 0x0F, 0xDF, 0xC0, 0x03, 0x63, 0x00, 0x02, 0x06,
		0x00, 0x08, 0x08, 0x1F, 0x20, 0x20, 0xC6, 0x80, 0x84, 0x05, 0x8C, 0x10,
		0x13, 0xE0, 0x40, 0x40, 0x01, 0x01, 0x00, 0x03, 0x1B, 0x00, 0x0F, 0xEF,
		0xC0, 0x1E, 0x0F, 0xFF, 0xF0, 0x03, 0xFE, 0x00, 0x00, 0x7C, 0x00, 0x30,
		0x60, 0x0C, 0x06, 0x03, 0x00, 0xC0, 0x60, 0x0C, 0x0C, 0x01, 0x81, 0x80,
		0x30, 0x30, 0x06, 0x02, 0x01, 0xC0, 0x60, 0x38, 0x7C, 0x06, 0x31, 0x81,
		0xCC, 0x18, 0x31, 0x01, 0x0E, 0x20, 0x21, 0x84, 0x04, 0x70, 0xC1, 0x0C,
		0x0C, 0x61, 0x80, 0xF0, 0x70, 0x00, 0x0C, 0x00, 0x01, 0x80, 0x00, 0x30,
		0x00, 0x03, 0x18, 0x00, 0x3C, 0xC7, 0x30, 0x13, 0xDC, 0x06, 0x9D, 0x81,
		0xE7, 0x60, 0x71, 0x99, 0x1C, 0x66, 0xE6, 0x19, 0xF9, 0x86, 0x73, 0x61,
		0x9C, 0xD8, 0x66, 0x36, 0x19, 0x8D, 0x86, 0x63, 0x61, 0x98, 0xD8, 0x66,
		0x66, 0x19, 0x99, 0x86, 0x66, 0x61, 0x9B, 0x00, 0x07, 0x80, 0x01, 0xC0,
		0x00, 0xE0, 0x00, 0xEC, 0x00, 0x01, 0x80, 0x01, 0xF0, 0x00, 0xFF, 0x80,
		0x38, 0x38, 0x0E, 0x03, 0x81, 0x80, 0x30, 0x30, 0x06, 0x06, 0x00, 0xC0,
		0xC0, 0x18, 0x0C, 0x06, 0x1F, 0xC1, 0xFF, 0xF8, 0x3F, 0x80, 0x00, 0x00,
		0x00, 0x00, 0x00, 0x00, 0x3F, 0xFF, 0xFF, 0xFF, 0xFF, 0xE3, 0x18, 0x03,
		0x39, 0xC0, 0x0F, 0x6B, 0x00, 0x73, 0x98, 0x03, 0x9C, 0xC0, 0x18, 0xC6,
		0x00, 0xC6, 0x30, 0x06, 0x31, 0x80, 0x31, 0x8C, 0x01, 0x8C, 0x60, 0x0C,
		0x63, 0x00, 0x63, 0x18, 0x03, 0x18, 0xC0, 0x18, 0xC6, 0x00, 0xC6, 0x30,
		0x06, 0x31, 0x80, 0x31, 0x8C, 0x01, 0x8C, 0x60, 0x00, 0x03, 0x00, 0x00,
		0x0C, 0x20, 0x00, 0x3F, 0x80, 0x00, 0x08, 0x00, 0x00, 0x00, 0x00, 0xF0,
		0x00, 0x3F, 0xE0, 0x00, 0x38, 0x00, 0x1E, 0x00, 0x0E, 0x80, 0x07, 0x20,
		0x03, 0x8C, 0xC1, 0xC3, 0x38, 0xE0, 0xC7, 0x70, 0x30, 0xF8, 0x00, 0x1C,
		0x00, 0x0F, 0x80, 0x07, 0x70, 0x03, 0x8E, 0x01, 0xC1, 0x80, 0xE0, 0x00,
		0x10, 0x00, 0x00, 0xE0, 0xE0, 0x00, 0xC2, 0x80, 0x03, 0x1B, 0x00, 0x04,
		0xCC, 0x00, 0x1B, 0x10, 0x00, 0x68, 0x40, 0x01, 0xE1, 0x80, 0x03, 0x86,
		0x00, 0x0C, 0x18, 0x00, 0x30, 0x63, 0xC0, 0xC1, 0x98, 0x83, 0x06, 0xC1,
		0x0C, 0x0E, 0x04, 0x00, 0x30, 0x10, 0x00, 0xC0, 0x40, 0x03, 0x83, 0x00,
		0x0F, 0x08, 0x00, 0x67, 0xC0, 0x01, 0x80, 0x00, 0x0C, 0x00, 0x03, 0xE0,
		0x00, 0x02, 0x08, 0x20, 0x71, 0xC3, 0x86, 0x9B, 0x7C, 0xE7, 0x8E, 0x2C,
		0x10, 0x61, 0x80, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
		0x00, 0x30, 0xC1, 0x03, 0x8E, 0x3C, 0x77, 0xDB, 0x26, 0x38, 0x71, 0xE0,
		0x82, 0x0C, 0xC0, 0x06, 0xC0, 0x18, 0xC0, 0x60, 0xC1, 0x81, 0x83, 0x03,
		0x04, 0x03, 0x18, 0x06, 0x30, 0xFF, 0xFE, 0x18, 0xC0, 0x31, 0x80, 0x63,
		0x01, 0x83, 0x03, 0x06, 0x04, 0x04, 0x18, 0x0C, 0x60, 0x0D, 0x80, 0x0C,
		0x00, 0x00, 0x01, 0x07, 0x80, 0x03, 0x08, 0xDF, 0x01, 0x30, 0xFF, 0xE2,
		0x20, 0xC1, 0xFC, 0x61, 0x81, 0x80, 0x43, 0x01, 0x80, 0xCE, 0x03, 0x80,
		0xF0, 0x03, 0x80, 0xC0, 0x07, 0x80, 0xC0, 0x0B, 0x00, 0xE0, 0x13, 0x00,
		0x70, 0x63, 0x00, 0x1F, 0x87, 0x00, 0x00, 0x07, 0x00, 0x00, 0x04, 0x00,
		0x00, 0xF0, 0x00, 0x00, 0x11, 0x80, 0x00, 0x02, 0x18, 0x00, 0x60, 0x61,
		0x80, 0x06, 0x06, 0x18, 0x00, 0x20, 0x63, 0x00, 0x02, 0x06, 0x60, 0x00,
		0x40, 0x78, 0x7F, 0xF8, 0x0F, 0x1F, 0xFE, 0x01, 0x33, 0x86, 0x00, 0x23,
		0xA0, 0x40, 0x04, 0x1C, 0x0C, 0x00, 0xC1, 0xC0, 0x80, 0x2C, 0x0C, 0x10,
		0x07, 0xC0, 0xE2, 0x00, 0x7C, 0x06, 0x40, 0x03, 0x60, 0x78, 0x00, 0x37,
		0x07, 0x80, 0x03, 0x1F, 0x9C, 0x00, 0x20, 0x00, 0xF0, 0x04, 0x00, 0x03,
		0xC0, 0x80, 0x00, 0x0F, 0xF0, 0x18, 0x36, 0x0C, 0x41, 0x8C, 0x18, 0xF9,
		0xFF, 0x9F, 0xF9, 0xFF, 0x9F, 0xF9, 0xF0, 0xF9, 0xFF, 0x9F, 0xF9, 0xFF,
		0x9F, 0xF9, 0xF1, 0x83, 0x18, 0x33, 0x06, 0xC1, 0x80, 0x07, 0x70, 0x06,
		0x64, 0x0E, 0x02, 0x09, 0x01, 0xC4, 0x41, 0x12, 0x20, 0x89, 0x02, 0x05,
		0x06, 0x81, 0x82, 0xE0, 0xC1, 0x10, 0x5E, 0x73, 0xC8, 0x00, 0x24, 0x08,
		0x13, 0x04, 0x18, 0x62, 0x30, 0x12, 0x90, 0x07, 0x70, 0x00, 0x03, 0x30,
		0x01, 0xFE, 0x00, 0x7F, 0x80, 0xDF, 0xEC, 0x7F, 0xFF, 0x9F, 0xFF, 0xE7,
		0xFF, 0xFB, 0xFB, 0x7F, 0xFD, 0x3F, 0xFF, 0x4B, 0xF7, 0xED, 0xF8, 0xF8,
		0xFC, 0x7F, 0xFF, 0x9F, 0xFF, 0xE3, 0xFF, 0xF0, 0x3F, 0xF0, 0x07, 0x38,
		0x00, 0x0E, 0x00, 0x7C, 0xE0, 0x06, 0x66, 0x07, 0xA3, 0x98, 0x3F, 0x8C,
		0xC0, 0xCC, 0x73, 0x02, 0x13, 0x8C, 0x08, 0x5E, 0x30, 0x01, 0x8C, 0xE0,
		0x0C, 0x19, 0x80, 0x60, 0x63, 0x82, 0x01, 0x87, 0xF0, 0x8C, 0x00, 0x01,
		0xE0, 0xF8, 0x01, 0xC1, 0x98, 0x01, 0xC7, 0x17, 0x81, 0x8C, 0x7F, 0x06,
		0x38, 0xCC, 0x0C, 0x72, 0x10, 0x31, 0xE8, 0x40, 0xCC, 0x60, 0x03, 0x60,
		0xC0, 0x1D, 0x81, 0x80, 0x66, 0x01, 0x07, 0x0C, 0x43, 0xF8, 0x1E, 0x00,
		0x00, 0x1E, 0x00, 0x00, 0xC4, 0x1F, 0x06, 0x01, 0x87, 0x18, 0x18, 0x06,
		0x60, 0xC0, 0x1C, 0xC6, 0x00, 0x31, 0xE8, 0x40, 0xC7, 0x21, 0x03, 0x38,
		0xCC, 0x0C, 0xC7, 0xF0, 0x67, 0x17, 0x81, 0x99, 0x80, 0x1C, 0xF8, 0x01,
		0xC0, 0x00, 0x01, 0xE0, 0x3E, 0x08, 0xC3, 0x86, 0x01, 0x98, 0x04, 0x06,
		0xE0, 0x0C, 0x1B, 0x00, 0x18, 0xCC, 0x08, 0x5E, 0x30, 0x21, 0x38, 0xC0,
		0xCC, 0x71, 0x83, 0xF8, 0xC6, 0x07, 0xA3, 0x8E, 0x00, 0x66, 0x0E, 0x00,
		0x7C, 0x0F, 0x00, 0x00, 0x1F, 0x80, 0x00, 0x31, 0x80, 0x00, 0x01, 0x80,
		0x00, 0xFE, 0x83, 0x87, 0xC3, 0x9F, 0x9E, 0x01, 0xFF, 0xFC, 0x61, 0xF3,
		0xF1, 0xC7, 0xC7, 0xE2, 0x1F, 0x7B, 0xC4, 0xFC, 0x01, 0x87, 0xF0, 0x00,
		0x07, 0x80, 0x00, 0x00, 0x01, 0xE0, 0x00, 0x0F, 0xC0, 0x00, 0x31, 0x80,
		0x00, 0xC0, 0x03, 0x82, 0xFE, 0x0F, 0xCE, 0x1F, 0x3F, 0xF0, 0x0F, 0x67,
		0xC3, 0x1F, 0xC7, 0xC7, 0x1E, 0xF7, 0xC2, 0x3C, 0x07, 0xE4, 0x78, 0x07,
		0xF0, 0xC0, 0x03, 0xC0, 0x00, 0x00, 0x3C, 0x00, 0x01, 0xFC, 0x30, 0x07,
		0xE4, 0x7B, 0xDF, 0x08, 0xFC, 0x7C, 0x71, 0xF9, 0xF0, 0xC7, 0xF7, 0xF0,
		0x0F, 0x7F, 0xF8, 0x7C, 0x7C, 0x6F, 0xE0, 0x00, 0x30, 0x00, 0x00, 0x31,
		0x80, 0x00, 0x3F, 0x00, 0x00, 0x1E, 0x00, 0x00, 0x78, 0x00, 0x61, 0xFC,
		0x03, 0xC4, 0xFC, 0x07, 0x88, 0x7D, 0xEF, 0x1C, 0x7C, 0x7F, 0x18, 0x7C,
		0xDE, 0x01, 0xFD, 0x9F, 0x0F, 0xFF, 0x0F, 0xEC, 0x7C, 0x00, 0x60, 0x00,
		0x31, 0x80, 0x00, 0x7E, 0x00, 0x00, 0xF0, 0x00, 0x00, 0xFF, 0xFF, 0xFF,
		0xFF, 0xFF, 0xF0, 0x00, 0x07, 0x84, 0x04, 0x3C, 0x70, 0x71, 0xE1, 0xC7,
		0x0F, 0x07, 0x70, 0x78, 0x1F, 0x03, 0xC0, 0x70, 0x1E, 0x07, 0xC0, 0xF0,
		0x77, 0x07, 0x87, 0x1C, 0x3C, 0x70, 0x71, 0xE1, 0x01, 0x0F, 0x00, 0x00,
		0x7F, 0xFF, 0xFF, 0xFF, 0xFF, 0xF8, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xF0,
		0x00, 0x07, 0x80, 0x00, 0x3C, 0x02, 0x01, 0xE0, 0x38, 0x0F, 0x03, 0x60,
		0x78, 0x31, 0x83, 0xC3, 0x06, 0x1E, 0x30, 0x1C, 0xF3, 0x00, 0x77, 0x90,
		0x01, 0x3C, 0x00, 0x01, 0xE0, 0x00, 0x0F, 0x00, 0x00, 0x7F, 0xFF, 0xFF,
		0xFF, 0xFF, 0xF8, 0x38, 0x0E, 0x3E, 0x0F, 0xB1, 0x8C, 0x78, 0xC6, 0x3C,
		0x63, 0x1B, 0xFF, 0xF8, 0xFF, 0xF8, 0x0C, 0x60, 0x06, 0x30, 0x03, 0x18,
		0x0F, 0xFF, 0x8F, 0xFF, 0xEC, 0x63, 0x1E, 0x31, 0x8F, 0x18, 0xC6, 0xF8,
		0x3E, 0x38, 0x0E, 0x00, 0x03, 0xE0, 0x06, 0x0C, 0x0C, 0x71, 0x84, 0xC6,
		0x44, 0x41, 0x12, 0x40, 0x4A, 0x20, 0x23, 0x10, 0x11, 0x88, 0x08, 0xC4,
		0x04, 0x62, 0x02, 0x29, 0x01, 0x24, 0x41, 0x11, 0x31, 0x90, 0xC7, 0x18,
		0x18, 0x30, 0x03, 0xE0, 0x00, 0x03, 0xE0, 0x06, 0x0C, 0x0C, 0x01, 0x84,
		0x30, 0x44, 0x38, 0x12, 0x04, 0x0A, 0x02, 0x03, 0x01, 0x01, 0x80, 0x80,
		0xC0, 0x40, 0x60, 0x20, 0x28, 0x10, 0x24, 0x08, 0x11, 0x04, 0x10, 0xC0,
		0x18, 0x18, 0x30, 0x03, 0xE0, 0x00, 0x03, 0xE0, 0x06, 0x0C, 0x0C, 0xF1,
		0x84, 0x84, 0x44, 0x01, 0x12, 0x00, 0x8A, 0x00, 0x43, 0x00, 0x41, 0x80,
		0x40, 0xC0, 0x40, 0x60, 0x40, 0x28, 0x40, 0x24, 0x60, 0x11, 0x3F, 0x90,
		0xC0, 0x18, 0x18, 0x30, 0x03, 0xE0, 0x00, 0x03, 0xE0, 0x06, 0x0C, 0x0C,
		0xF9, 0x84, 0x06, 0x44, 0x01, 0x12, 0x00, 0x8A, 0x00, 0x43, 0x00, 0x41,
		0x81, 0xC0, 0xC0, 0x10, 0x60, 0x04, 0x28, 0x02, 0x24, 0x01, 0x11, 0x01,
		0x10, 0xCF, 0x18, 0x18, 0x30, 0x03, 0xE0, 0x00, 0x03, 0xE0, 0x06, 0x0C,
		0x0C, 0x01, 0x84, 0x08, 0x44, 0x0C, 0x12, 0x0A, 0x0A, 0x09, 0x03, 0x04,
		0x81, 0x84, 0x40, 0xC4, 0x20, 0x63, 0xF8, 0x28, 0x08, 0x24, 0x04, 0x11,
		0x02, 0x10, 0xC0, 0x18, 0x18, 0x30, 0x03, 0xE0, 0x00, 0x03, 0xE0, 0x06,
		0x0C, 0x0C, 0x01, 0x84, 0x7C, 0x44, 0x20, 0x12, 0x10, 0x0A, 0x08, 0x03,
		0x07, 0x81, 0x80, 0x60, 0xC0, 0x18, 0x60, 0x0C, 0x28, 0x06, 0x24, 0x06,
		0x11, 0x1E, 0x10, 0xC0, 0x18, 0x18, 0x30, 0x03, 0xE0, 0x00, 0x03, 0xE0,
		0x06, 0x0C, 0x0C, 0x79, 0x84, 0xC0, 0x44, 0x40, 0x12, 0x60, 0x0A, 0x30,
		0x03, 0x1B, 0x81, 0x8E, 0x20, 0xC6, 0x08, 0x63, 0x04, 0x29, 0x82, 0x24,
		0x41, 0x11, 0x31, 0x10, 0xCF, 0x18, 0x18, 0x30, 0x03, 0xE0, 0x00, 0x03,
		0xE0, 0x06, 0x0C, 0x0C, 0x01, 0x84, 0x00, 0x44, 0x7F, 0x12, 0x00, 0x8A,
		0x00, 0x83, 0x00, 0x81, 0x80, 0x40, 0xC0, 0x40, 0x60, 0x40, 0x28, 0x20,
		0x24, 0x20, 0x11, 0x10, 0x10, 0xC0, 0x18, 0x18, 0x30, 0x03, 0xE0, 0x00,
		0x03, 0xE0, 0x06, 0x0C, 0x0C, 0x71, 0x84, 0x44, 0x44, 0x22, 0x12, 0x11,
		0x0A, 0x0C, 0x83, 0x03, 0x81, 0x83, 0xC0, 0xC1, 0x30, 0x61, 0x0C, 0x28,
		0x82, 0x24, 0x41, 0x11, 0x31, 0x10, 0xCF, 0x18, 0x18, 0x30, 0x03, 0xE0,
		0x00, 0x03, 0xE0, 0x06, 0x0C, 0x0C, 0x79, 0x84, 0x46, 0x44, 0x41, 0x12,
		0x20, 0xCA, 0x10, 0x63, 0x08, 0x31, 0x82, 0x38, 0xC0, 0xFC, 0x60, 0x06,
		0x28, 0x03, 0x24, 0x01, 0x11, 0x01, 0x10, 0xCF, 0x18, 0x18, 0x30, 0x03,
		0xE0, 0x00, 0x03, 0xE0, 0x06, 0x0C, 0x0F, 0x1D, 0x84, 0x91, 0x44, 0x48,
		0x92, 0x28, 0x2A, 0x14, 0x13, 0x0A, 0x09, 0x85, 0x04, 0xC2, 0x82, 0x61,
		0x41, 0x28, 0xA0, 0xA4, 0x48, 0x91, 0x24, 0x50, 0xD1, 0xD8, 0x18, 0x30,
		0x03, 0xE0, 0x00, 0x03, 0xE0, 0x07, 0xFC, 0x0F, 0xFF, 0x87, 0xC7, 0xC7,
		0xC9, 0xF3, 0xCE, 0xFB, 0xE7, 0x3F, 0xF3, 0x9F, 0xF9, 0xCF, 0xFC, 0xE7,
		0xFE, 0x73, 0xEF, 0x3B, 0xE7, 0xC9, 0xF1, 0xF1, 0xF0, 0xFF, 0xF8, 0x1F,
		0xF0, 0x03, 0xE0, 0x00, 0x03, 0xE0, 0x07, 0xFC, 0x0F, 0xFF, 0x87, 0xE7,
		0xC7, 0xE3, 0xF3, 0xF9, 0xFB, 0xFC, 0xFF, 0xFE, 0x7F, 0xFF, 0x3F, 0xFF,
		0x9F, 0xFF, 0xCF, 0xEF, 0xE7, 0xE7, 0xF3, 0xF1, 0xFF, 0xF0, 0xFF, 0xF8,
		0x1F, 0xF0, 0x03, 0xE0, 0x00, 0x03, 0xE0, 0x07, 0xFC, 0x0F, 0xFF, 0x87,
		0x83, 0xC7, 0x9C, 0xF3, 0xFE, 0x7B, 0xFF, 0x3F, 0xFF, 0x3F, 0xFF, 0x3F,
		0xFE, 0x3F, 0xFE, 0x7F, 0xEF, 0x01, 0xE7, 0x80, 0xF1, 0xFF, 0xF0, 0xFF,
		0xF8, 0x1F, 0xF0, 0x03, 0xE0, 0x00, 0x03, 0xE0, 0x07, 0xFC, 0x0F, 0xFF,
		0x87, 0x83, 0xC7, 0xDC, 0xF3, 0xFE, 0x7B, 0xFF, 0x3F, 0xFF, 0x3F, 0xFE,
		0x3F, 0xFF, 0xC7, 0xFF, 0xF3, 0xEF, 0xF9, 0xE7, 0xDC, 0xF1, 0xE0, 0xF0,
		0xFF, 0xF8, 0x1F, 0xF0, 0x03, 0xE0, 0x00, 0x03, 0xE0, 0x07, 0xFC, 0x0F,
		0xFF, 0x87, 0xE7, 0xC7, 0xE3, 0xF3, 0xE1, 0xFB, 0xF4, 0xFF, 0xF6, 0x7F,
		0xF3, 0x3F, 0xF8, 0x07, 0xFC, 0x03, 0xEF, 0xE7, 0xE7, 0xF3, 0xF1, 0xF9,
		0xF0, 0xFF, 0xF8, 0x1F, 0xF0, 0x03, 0xE0, 0x00, 0x03, 0xE0, 0x07, 0xFC,
		0x0F, 0xFF, 0x87, 0xFF, 0xC7, 0xC0, 0xF3, 0xE0, 0x7B, 0xF3, 0xFF, 0xF9,
		0xFF, 0xFC, 0x3F, 0xFF, 0xC7, 0xFF, 0xF3, 0xEF, 0xF9, 0xE7, 0xDC, 0xF1,
		0xE1, 0xF0, 0xFF, 0xF8, 0x1F, 0xF0, 0x03, 0xE0, 0x00, 0x03, 0xE0, 0x07,
		0xFC, 0x0F, 0xFF, 0x87, 0x83, 0xC7, 0x9D, 0xF3, 0xDF, 0xFB, 0xCF, 0xFF,
		0xE4, 0x7F, 0xF1, 0x9F, 0xF9, 0xE7, 0xFC, 0xF3, 0xEE, 0x79, 0xE7, 0x99,
		0xF1, 0xE1, 0xF0, 0xFF, 0xF8, 0x1F, 0xF0, 0x03, 0xE0, 0x00, 0x03, 0xE0,
		0x07, 0xFC, 0x0F, 0xFF, 0x87, 0xFF, 0xC7, 0x80, 0xF3, 0xC0, 0x7B, 0xFF,
		0x3F, 0xFF, 0x3F, 0xFF, 0x3F, 0xFF, 0xBF, 0xFF, 0x9F, 0xEF, 0x9F, 0xE7,
		0xCF, 0xF1, 0xFF, 0xF0, 0xFF, 0xF8, 0x1F, 0xF0, 0x03, 0xE0, 0x00, 0x03,
		0xE0, 0x07, 0xFC, 0x0F, 0xFF, 0x87, 0xC7, 0xC7, 0xC9, 0xF3, 0xE4, 0xFB,
		0xF2, 0x7F, 0xF8, 0x7F, 0xFC, 0x1F, 0xFC, 0xC7, 0xFE, 0xFB, 0xEF, 0x7D,
		0xE7, 0x9C, 0xF1, 0xE1, 0xF0, 0xFF, 0xF8, 0x1F, 0xF0, 0x03, 0xE0, 0x00,
		0x03, 0xF0, 0x03, 0xFF, 0x01, 0xE1, 0xE0, 0xF0, 0x1C, 0x78, 0xC7, 0x9E,
		0x78, 0xEF, 0x9E, 0x3F, 0xE7, 0x8F, 0xF8, 0xC3, 0xFF, 0x00, 0xFF, 0xE2,
		0x3D, 0xFF, 0x1E, 0x7F, 0xC7, 0x8E, 0x03, 0xC1, 0x81, 0xE0, 0x3F, 0xF0,
		0x03, 0xF0, 0x00, 0x03, 0xE0, 0x07, 0xFC, 0x0F, 0xFF, 0x84, 0xF1, 0xC4,
		0x67, 0x33, 0x37, 0xDB, 0x93, 0xE7, 0xC9, 0xF3, 0xE4, 0xF9, 0xF2, 0x7C,
		0xF9, 0x3E, 0x6C, 0xDF, 0x66, 0x67, 0x31, 0x3C, 0x70, 0xFF, 0xF8, 0x1F,
		0xF0, 0x03, 0xE0, 0x00, 0x5F, 0xA0, 0x38, 0xFB, 0xFF, 0xFF, 0xEF, 0x8E,
		0x00, 0x0F, 0xC0, 0x7F, 0x83, 0xFF, 0x1F, 0xFE, 0xFF, 0xFF, 0xFF, 0xFF,
		0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xF7, 0xFF, 0x8F, 0xFC, 0x1F, 0xE0,
		0x3F, 0x00, 0x03, 0xE0, 0x07, 0xFC, 0x0F, 0x07, 0x86, 0x00, 0xC6, 0x00,
		0x33, 0x00, 0x1B, 0x00, 0x07, 0x80, 0x03, 0xC0, 0x01, 0xE0, 0x00, 0xF0,
		0x00, 0x6C, 0x00, 0x66, 0x00, 0x31, 0x80, 0x30, 0xF0, 0x78, 0x1F, 0xF0,
		0x03, 0xE0, 0x00, 0x03, 0xE0, 0x07, 0xFC, 0x0F, 0xFF, 0x87, 0xFF, 0xC7,
		0xC1, 0xF3, 0x80, 0x3B, 0xC0, 0x1F, 0xC0, 0x07, 0xE0, 0x03, 0xF0, 0x01,
		0xFC, 0x01, 0xEE, 0x00, 0xE7, 0xC1, 0xF1, 0xFF, 0xF0, 0xFF, 0xF8, 0x1F,
		0xF0, 0x03, 0xE0, 0x00, 0x03, 0xE0, 0x07, 0xFC, 0x0F, 0xFF, 0x87, 0xFF,
		0xC7, 0xFF, 0xF3, 0xF1, 0xFB, 0xF0, 0x7F, 0xF0, 0x1F, 0xF8, 0x0F, 0xFC,
		0x07, 0xFF, 0x07, 0xEF, 0xC7, 0xE7, 0xFF, 0xF1, 0xFF, 0xF0, 0xFF, 0xF8,
		0x1F, 0xF0, 0x03, 0xE0, 0x00, 0x03, 0xF0, 0x03, 0xFF, 0x01, 0xC0, 0xE0,
		0xE0, 0x1C, 0x70, 0x03, 0x98, 0x00, 0x6C, 0x1E, 0x0F, 0x0F, 0xC3, 0xC3,
		0xF0, 0xF0, 0xFC, 0x3C, 0x3F, 0x0F, 0x07, 0x83, 0x60, 0x01, 0x9C, 0x00,
		0xE3, 0x80, 0x70, 0x70, 0x38, 0x0F, 0xFC, 0x00, 0xFC, 0x00 )


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
		(     0,  17,  17,  21,    2,  -16 ),   ## 0x20 ' '
		(    37,  18,  18,  21,    2,  -17 ),   ## 0x21 '!'
		(    78,  20,  13,  22,    1,  -12 ),   ## 0x22 '"'
		(   111,  20,  13,  22,    1,  -12 ),   ## 0x23 '#'
		(   144,  10,  19,  14,    2,  -18 ),   ## 0x24 '$'
		(   168,  16,  20,  19,    2,  -18 ),   ## 0x25 '%'
		(   208,  12,  16,  16,    2,  -18 ),   ## 0x26 '&'
		(   232,  12,  16,  16,    2,  -13 ),   ## 0x27 '''
		(   256,  19,   9,  23,    2,  -13 ),   ## 0x28 '('
		(   278,  19,   9,  23,    2,  -13 ),   ## 0x29 ')'
		(   300,   9,  19,  13,    2,  -17 ),   ## 0x2A '*'
		(   322,   9,  19,  13,    2,  -18 ),   ## 0x2B '+'
		(   344,  17,  19,  21,    2,  -18 ),   ## 0x2C ','
		(   385,  18,  18,  20,    1,  -17 ),   ## 0x2D '-'
		(   426,  18,  18,  20,    1,  -17 ),   ## 0x2E '.'
		(   467,  18,  18,  20,    1,  -17 ),   ## 0x2F '/'
		(   508,  24,  18,  27,    2,  -17 ),   ## 0x30 '0'
		(   562,  12,  18,  16,    2,  -17 ),   ## 0x31 '1'
		(   589,  16,  21,  20,    2,  -18 ),   ## 0x32 '2'
		(   631,  22,  20,  26,    2,  -19 ),   ## 0x33 '3'
		(   686,  17,  18,  21,    2,  -17 ),   ## 0x34 '4'
		(   725,  16,  18,  21,    3,  -17 ),   ## 0x35 '5'
		(   761,  12,  17,  16,    2,  -16 ),   ## 0x36 '6'
		(   787,  17,  17,  20,    2,  -16 ),   ## 0x37 '7'
		(   824,  12,  11,  15,    2,  -13 ),   ## 0x38 '8'
		(   841,  16,  15,  19,    2,  -17 ),   ## 0x39 '9'
		(   871,  17,  17,  21,    2,  -16 ),   ## 0x3A ':'
		(   908,  19,  18,  21,    2,  -17 ),   ## 0x3B ';'
		(   951,  15,  17,  18,    2,  -16 ),   ## 0x3C '<'
		(   983,  14,  18,  18,    2,  -17 ),   ## 0x3D '='
		(  1015,  14,  17,  17,    2,  -16 ),   ## 0x3E '>'
		(  1045,  13,  13,  17,    2,  -14 ),   ## 0x3F '?'
		(  1067,  15,  17,  19,    2,  -16 ),   ## 0x40 '@'
		(  1099,  17,  17,  21,    2,  -16 ),   ## 0x41 'A'
		(  1136,  17,  18,  21,    2,  -17 ),   ## 0x42 'B'
		(  1175,  17,  18,  22,    2,  -17 ),   ## 0x43 'C'
		(  1214,  18,  18,  21,    2,  -17 ),   ## 0x44 'D'
		(  1255,  24,  22,  28,    2,  -16 ),   ## 0x45 'E'
		(  1321,  21,  22,  25,    2,  -16 ),   ## 0x46 'F'
		(  1379,  19,  19,  23,    2,  -17 ),   ## 0x47 'G'
		(  1425,  22,  17,  26,    2,  -16 ),   ## 0x48 'H'
		(  1472,  19,  24,  23,    2,  -18 ),   ## 0x49 'I'
		(  1529,  18,  22,  22,    2,  -16 ),   ## 0x4A 'J'
		(  1579,  19,  16,  23,    2,  -17 ),   ## 0x4B 'K'
		(  1617,  21,  23,  25,    2,  -17 ),   ## 0x4C 'L'
		(  1678,  18,  18,  22,    2,  -17 ),   ## 0x4D 'M'
		(  1719,  22,  21,  26,    2,  -17 ),   ## 0x4E 'N'
		(  1777,  21,  14,  26,    2,  -14 ),   ## 0x4F 'O'
		(  1814,  15,  18,  19,    2,  -17 ),   ## 0x50 'P'
		(  1848,  24,  16,  25,    2,  -13 ),   ## 0x51 'Q'
		(  1896,  28,  22,  31,    2,  -17 ),   ## 0x52 'R'
		(  1973,  12,   9,  13,    1,  -18 ),   ## 0x53 'S'
		(  1987,  12,   9,  13,    1,  -18 ),   ## 0x54 'T'
		(  2001,  17,  17,  21,    2,  -16 ),   ## 0x55 'U'
		(  2038,  18,  17,  21,    2,  -17 ),   ## 0x56 'V'
		(  2077,  22,  13,  24,    1,  -12 ),   ## 0x57 'W'
		(  2113,  22,  13,  24,    1,  -12 ),   ## 0x58 'X'
		(  2149,  22,  13,  24,    1,  -12 ),   ## 0x59 'Y'
		(  2185,  22,  13,  24,    1,  -12 ),   ## 0x5A 'Z'
		(  2221,  23,  13,  24,    1,  -12 ),   ## 0x5B '['
		(  2259,  23,  13,  24,    0,  -12 ),   ## 0x5C '\'
		(  2297,  23,  13,  24,    1,  -12 ),   ## 0x5D ']'
		(  2335,  23,  13,  24,    0,  -12 ),   ## 0x5E '^'
		(  2373,  21,  17,  25,    2,  -16 ),   ## 0x5F '_'
		(  2418,  21,  17,  25,    2,  -16 ),   ## 0x60 '`'
		(  2463,  17,  17,  21,    2,  -16 ),   ## 0x61 'a'
		(  2500,  17,  17,  21,    2,  -16 ),   ## 0x62 'b'
		(  2537,  17,  17,  21,    2,  -16 ),   ## 0x63 'c'
		(  2574,  17,  17,  21,    2,  -16 ),   ## 0x64 'd'
		(  2611,  17,  17,  21,    2,  -16 ),   ## 0x65 'e'
		(  2648,  17,  17,  21,    2,  -16 ),   ## 0x66 'f'
		(  2685,  17,  17,  21,    2,  -16 ),   ## 0x67 'g'
		(  2722,  17,  17,  21,    2,  -16 ),   ## 0x68 'h'
		(  2759,  17,  17,  21,    2,  -16 ),   ## 0x69 'i'
		(  2796,  17,  17,  21,    2,  -16 ),   ## 0x6A 'j'
		(  2833,  17,  17,  21,    2,  -16 ),   ## 0x6B 'k'
		(  2870,  17,  17,  21,    2,  -16 ),   ## 0x6C 'l'
		(  2907,  17,  17,  21,    2,  -16 ),   ## 0x6D 'm'
		(  2944,  17,  17,  21,    2,  -16 ),   ## 0x6E 'n'
		(  2981,  17,  17,  21,    2,  -16 ),   ## 0x6F 'o'
		(  3018,  17,  17,  21,    2,  -16 ),   ## 0x70 'p'
		(  3055,  17,  17,  21,    2,  -16 ),   ## 0x71 'q'
		(  3092,  17,  17,  21,    2,  -16 ),   ## 0x72 'r'
		(  3129,  17,  17,  21,    2,  -16 ),   ## 0x73 's'
		(  3166,  17,  17,  21,    2,  -16 ),   ## 0x74 't'
		(  3203,  17,  17,  21,    2,  -16 ),   ## 0x75 'u'
		(  3240,  18,  17,  21,    2,  -16 ),   ## 0x76 'v'
		(  3279,  17,  17,  21,    2,  -16 ),   ## 0x77 'w'
		(  3316,   3,   4,   8,    2,  -10 ),   ## 0x78 'x'
		(  3318,   7,   7,  11,    2,  -11 ),   ## 0x79 'y'
		(  3325,  14,  14,  18,    2,  -15 ),   ## 0x7A 'z'
		(  3350,  17,  17,  21,    2,  -16 ),   ## 0x7B '{'
		(  3387,  17,  17,  21,    2,  -16 ),   ## 0x7C '|'
		(  3424,  17,  17,  21,    2,  -16 ),   ## 0x7D '}'
		(  3461,  18,  18,  21,    2,  -17 )	## 0x7E '~'
			)

		self.GFXfirst = 0x20
		self.GFXlast = 0x7E
		self.GFXyadvance = 26
		self.GFXMinYadvance = -19
				## from face->size->metrics.height
	def __repr__ (self):
		rows = ''
		for y in range(self.height):
			for x in range(self.width):
				rows += '*' if self.pixels[y * self.width + x] else ' '
		rows += '\n'
		return rows

## Approx. 4174 bytes