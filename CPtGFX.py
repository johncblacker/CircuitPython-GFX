# This software is a python port of the Adafruit_GFX.cpp program file.
#   The Adafruit copyright therefore applies as well as my own.

#Software License Agreement (BSD License)
#
#Copyright (c) 2018 John Blacker.  All rights reserved.
#Copyright (c) 2012 Adafruit Industries.  All rights reserved.
#
#Redistribution and use in source and binary forms, with or without
#modification, are permitted provided that the following conditions are met:
#
#- Redistributions of source code must retain the above copyright notice,
#  this list of conditions and the following disclaimer.
#- Redistributions in binary form must reproduce the above copyright notice,
#  this list of conditions and the following disclaimer in the documentation
#  and/or other materials provided with the distribution.
#
#THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
#AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
#IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
#ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
#LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
#CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
#SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
#INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
#CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
#ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
#POSSIBILITY OF SUCH DAMAGE.


import struct




class GFX:
    GFX_HAS_FONTFILE = False
    def __init__(self, swidth, sheight, pixel=None, font_name=None):
        self._width = swidth
        self._height = sheight
        self._pixel = pixel
        self.font_name = font_name
        self.fontfile = None
        self.TextSize = 1
        self.wrap = True   # default textwrap is true
        self.Cursor_x = 0
        self.Cursor_y = 0
        self.GFXfirst = 0x20
        self.GFXlast = 0x7e
        self.TextColor = 65535
        self.BgColor = 0


        if (self.font_name == "default" or self.font_name == "font5X8.bin"):
            self.setFont("font5X8.bin")
        elif (self.font_name != None):
            self.setFont(self.font_name)
        else:
            pass
 
    def setFont(self, fontname):
        self.fontname = fontname
        if self.fontname == "font5x8.bin" :
            self.font_name = "font5x8.bin"
            self._font = open(self.font_name, 'rb') 
            self._font_width, self._font_height = struct.unpack("BB", self._font.read(2))
            self.GFXfirst = 0x20
            self.GFXlast = 0x7e
            self.GFX_HAS_FONTFILE = True
            self.fontfile = self.font_name
        else:
            #self.mod = import self.fontname
            self.fontfile = self.font_name.GFXfont()
            self.font_name = self.fontname
            self.GFXfirst = self.GFXfirst
            self.GFXlast = self.fontfile.GFXlast
            self.GFX_HAS_FONTFILE = True

    def deinit(self):
        # Close the font file as cleanup.
        self._font.close()

    def __enter__(self):
        self.init()
        return self

    def __exit__(self, exception_type, exception_value, traceback):
        self.deinit()

    def draw_char(self, ch, x, y):
        
        # print("font_name: %s" % (self.font_name))
        # print("color: %d" % (self.TextColor))
        # print("font_width: %d" % (self._font_width))
        # print("font_height: %d" % (self._font_height)) 

        if self.font_name == "font5x8.bin":

            # Don't draw the character if it will be clipped off the visible area.
            if x < -self._font_width or x >= self._width or \
                y < -self._font_height or y >= self._height:
                return
            # Go through each column of the character.
            for char_x in range(self._font_width):
                # Grab the byte for the current column of font data.
                self._font.seek(2 + (ord(ch) * self._font_width) + char_x)
                line = struct.unpack('B', self._font.read(1))[0]
                # Go through each row in the column byte.
                for char_y in range(self._font_height):
                    # Draw a pixel for each bit that's flipped on.
                    if (line >> char_y) & 0x1:
                        # print("x: %d; y: %d" % (x + char_x, y + char_y))
                        self._pixel(x + char_x, y + char_y, self.TextColor)
                        self.setCursorX = x + char_x
                        self.setCursorY = y + char_y
        else:
        # Custom font (created by CPfontconvert.exe ( a stand-alone c++ program)
        # CPfontconvert takes a <fontfile.ttf> and creates a .py "Class" object that contains:
        #           GFXbitmaps - a Python tuple of hex characters making up all the ascii characters
        #               that have been converted from the .ttf file;
        #           GFX.glyphs - a Python tuple of tuples, each containing another tuple of  attributes
        #               for a particular character.  The attributes are:
        #                   character's width;
        #                   character's height;
        #                   character's "X" value;
        #                   character's "Y" value;
        #                   character's advance value;
        #                   character's offset into GFXbitmaps.

        
        ## Character is assumed previously filtered by write() to eliminate
        ## newlines, returns, non-printable characters, etc.  Calling
        ## drawChar() directly with 'bad' characters of font may cause mayhem!
        ##  NOTE: NO CHECKING TO SEE IF THE CHARACTER(S) WILL BE CLIPPED OFF THE VISIBLE AREA, YET (TODO)

        ##c -= (uint8_t)pgm_read_byte(&gfxFont->first);
            c = ord(ch) - self.GFXfirst
            cBitmap = self.fontfile.GFXbitmaps
            self.cGlyph = self.fontfile.GFXglyphs[c]
        ##GFXglyph *glyph  = &(((GFXglyph *)pgm_read_pointer(&gfxFont->glyph))[c]);
        ##uint8_t  *bitmap = (uint8_t *)pgm_read_pointer(&gfxFont->bitmap);
            bo = self.cGlyph[0]
            #print(bo)
            w = self.cGlyph[1]
            h = self.cGlyph[2]
            xo = self.cGlyph[4]
            yo = self.cGlyph[5]
            bits = 0
            bit = 0
                    
        ## Todo: Add character clipping here

        ## NOTE: THERE IS NO 'BACKGROUND' COLOR OPTION ON CUSTOM FONTS.
        ## THIS IS ON PURPOSE AND BY DESIGN.  The background color feature
        ## has typically been used with the 'classic' font to overwrite old
        ## screen contents with new data.  This ONLY works because the
        ## characters are a uniform size; it's not a sensible thing to do with
        ## proportionally-spaced fonts with glyphs of varying sizes (and that
        ## may overlap).  To replace previously-drawn text when using a custom
        ## font, use the getTextBounds() function to determine the smallest
        ## rectangle encompassing a string, erase the area with fillRect(),
        ## then draw new text.  This WILL infortunately 'blink' the text, but
        ## is unavoidable.  Drawing 'background' pixels will NOT fix this,
        ## only creates a new set of problems.  Have an idea to work around
        ## this (a canvas object type for MCUs that can afford the RAM and
        ## displays supporting setAddrWindow() and pushColors()), but haven't
        ## implemented this yet.

        ##startWrite();
            
            # print(cBitmap)
            bitmapbyte = 0
            bitcount = 0
            for yy in range (0, h  ):               
                for xx in range (0, w ):
                    # print(" {0} {1:#010b}".format(bo, bitcount))
                    if(not(bitcount & 7)):       # checking 7 bits in each byte
                        bitmapbyte = cBitmap[bo]
                        # print(type(bitmapbyte))
                    bitcount += 1 
                    if bitcount >= 8:
                        bo += 1
                        bitcount = 0
                    # print("bitmapchar: {:#010b}".format(bitmapbyte))
                    if (bitmapbyte & 0x80):
                        if (self.TextSize == 1):
                            self._pixel( x + xo + xx , y + yo + yy , self.TextColor)
                            # print("wrote pixel at x: %d; y: %d " % (x+xo+xx, y+yo+yy))
                            self.setCursorX = x + xo + xx
                            self.setCursorY = y + yo + yy
                        else:
                            self.writeFillRect( int(x + ( xo + xx) * int(self.TextSize / 2)), int(y + (yo + yy) * (self.TextSize)), 
                                                self.TextSize, self.TextSize, self.TextColor)
                            self.setCursorX = int(x + (xo + xx) * int(self.Textsize / 2))
                            self.SetCursorY = int(y + (y0 + yy) * int(self.Textsize / 2))
                    tb = bitmapbyte << 1
                    if tb >= 256:
                        bitmapbyte = tb - 256
                    else:
                        bitmapbyte = tb
                

    # End classic vs custom font
    
    def setTextColor(self, tcolor):
        self.TextColor = tcolor
        
    def getTextColor(self):
        return self.TextColor
        
    def getBgColor(self):
        return self.BgColor
        
    def getTextSize(self):
        return self.TextSize
        
    def setBgColor(self, bgcolor):
        self.BgColor = bgcolor
        
    def setCursor(self, x, y):
        self.Cursor_x = x
        self.Cursor_y = y
        
    def getCursor(self):
        return self.Cursor_x, self.Cursor_y
                
    def getCursorX(self):
        return self.CursorX
        
    def getCursorY(self):
        return self.CursorY
        
    def setTextSize(self, s):
        if s <= 0 or s > 3:
            self.TextSize = 1
        
    def setTextWrap(self, wrap):   # wrap = true/false
        self.wrap = wrap
        
    def getTextWrap(self):
        return self.wrap
        
    def getBitmap(self, ch):
        c = ord(ch) # convert string to an number
        c -= self.GFXfirst     # normalize the character
        cBitmap = self.fontfile.GFXbitmaps
        cGlyph = self.fontfile.GFXglyphs[c]
        bo = cGlyph[0]  # offset to bitmap for character
        numBytes = (cGlyph[1] * cGlyph[2]) / 8
        tnum = int(numBytes)
        if (tnum * 8) < (cGlyph[1] * cGlyph[2]):
            intBytes = tnum + 1
        else:
            intBytes = tnum
        rValues = []   
        for indx in range(0, intBytes):
            rValues = rValues + [cBitmap[bo + indx]]
            
        return rValues
        
        
    
    def text(self, text ):
        # Draw the specified text at the specified location.
        x = self.Cursor_x
        y = self.Cursor_y
        # print(self.font_name)
        if self.font_name != "font5x8.bin":
            # print("custom font")
            for tc in text:
                if (tc == '\n'):    # new line?
                    self.Cursor_x = 0
                    self.Cursor_y += self.TextSize and self.fontfile.GFXyadvance
                else:
                    c = ord(tc) # ensure c is a number, not a string
                    if (( c >= self.GFXfirst) and ( c <= self.GFXlast)):
                        nc = ord(tc) - self.GFXfirst
                        self.cGlyph = self.fontfile.GFXglyphs[nc] # get GFXglyph for character  
                        # print(self.cGlyph)
                        w = self.cGlyph[1]
                        h = self.cGlyph[2]
                        xo = self.cGlyph[3]
                        yo = self.cGlyph[4]
                        # print(self.Cursor_x + self.TextSize * ( xo + w))
                        # print("wrap: %d" % self.wrap)
                        # print("width: %d" % self._width)
                        if (self.wrap and (( self.Cursor_x + self.TextSize * ( xo + w)) > self._width )):
                            self.Cursor_x = 0
                            self.Cursor_y += self.TextSize * self.fontfile.GFXyadvance
                            if (self.Cursor_y  > self._height):
                                self.Cursor_y = self.fontfile.GFXyadvance
                            self.draw_char(tc, self.Cursor_x, self.Cursor_y)
                        else:
                            self.draw_char(tc, self.Cursor_x, self.Cursor_y)
                    self.Cursor_x += self.cGlyph[3] * self.TextSize #advance cursor based on textsize and xadvance in glyph      
        else:
            # print("default font")
            color = self.getTextColor
            bgcolor = self.getBgColor
            size = self.getTextSize
  
            # Draw the specified text at the specified location using font5x8.bin
            for i in range(0, len(text)):
                # print("printing: %s" % text[i])
                self.draw_char(text[i], x + (i * (self._font_width + 1)), y, color, bgcolor, size)
    
    
    
    # - Pass a character, returns updated values of x, y, minx, miny, maxx, maxy
    def charBounds(self, c, x, y, minx, miny, maxx, maxy):
        if self.font_name  != "font5x8.bin" :    #   custom font
            if c == '\n':
                x = 0
                y += self.TextSize ( self.fontfile.GFXyadvance)
            elif c !=  '\r':
                first = self.GFXfirst
                last = self.GFXlast
                if (( ord(c) >= first) and (ord(c) <= last)):
                    cGlyph = self.fontfile.GFXglyphs[ ord(c) - first]   # index to character glyph
                    # print(cGlyph)
                    gw = cGlyph[1]  # get character width
                    gh = cGlyph[2]  #               height
                    xa = cGlyph[3]  #               xAdvance
                    xo = cGlyph[4]  #               xOffset
                    yo = cGlyph[5]  #               yOffset
                    # print("textsize: %d" % self.TextSize)
                    # print("gw: %d; gh: %d; xa: %d; x0: %d; y0: %d" % (gw, gh, xa, xo, yo))
                    if (self.wrap & (( x + ((xo + gw) * self.TextSize)) > self._width)):
                        x = 0
                        y += self.TextSize * self.fontfile.GFXyadvance
                    ts = self.TextSize
                    x1 = x + xo * ts
                    y1 = y + yo * ts
                    x2 = x1 + gw * ts - 1
                    y2 = y1 + gh * ts - 1
                    # print("x1: %d; y1: %d; minx: %d; miny: %d; maxx: %d; maxy: %d; x: %d; y: %d" % (x1, y1, minx, miny, maxx, maxy, x, y))
                    if (x1 < minx):
                        minx = x1
                    if (y1 < miny):
                        miny = y1
                    if (x2 > maxx):
                        maxx = x2
                    if (y2 > maxy):
                        maxy = y2
                    x += xa * ts
                    return x, y, minx, miny, maxx, maxy
        else:   # Default font (5 X 8)
            if ( c == '\n'):
                x = 0
                y += self.TextSize * 8
            elif c != '\r':
                if ( self.wrap & (( x + self.TextSize * 6) > self._width)):
                    x = 0
                    y += self.TextSize * 8
                x2 = x + self.TextSize * 6 - 1 
                y2 = y + self.TextSize * 8 - 1
                if ( x2 > maxx):
                    maxx = x2
                if (y2 > maxy):
                    maxy = y2
                if (x < minx):
                    minx = x
                if (y < miny):
                    miny = y
                x += self.TextSize * 6
                return x, y, minx, miny, maxx, maxy
                
    # Pass string and a cursor position, returns UL corner and width and height
    def getTextBounds( self, str, x, y):    # returns x1, y1, w and h as a tuple
        x1 = x 
        y1 = y 
        w = h = 0
        minx = self._width
        miny = self._height
        maxx = 0
        maxy = -(self._height)
        lst = list(str)
        i = 0
        while  i < len(lst):    
            c = lst[i]
            x, y, minx, miny, maxx, maxy = self.charBounds(c, x, y, minx, miny, maxx, maxy)
            # print("x: %d; y: %d; minx: %d; miny: %d; maxx: %d; maxy: %d" % (x, y, minx, miny, maxx, maxy))
            i += 1
        
        if (maxx >= minx):
            x1 = minx
            w = maxx - minx + 1
            
        if (maxy >= miny):
            y1 = miny
            h = maxy - miny + 1
            
        return x1, abs(y1) + 2, w, y - abs(y1) 
            
            
                    
                

    def width(self, text):
        # Return the pixel width of the specified text message.
        return len(text) * (self._font_width + 1)
        
    def writerectangle( self, x, y, w, h, color):
        for i in range( x, x + w):
            self.drawFastVLine(i, y, h, color)
            
    def drawRect(self, x, y, w, h, color): 
        self.writeFastHLine(x, y, w, color)
        self.writeFastHLine(x, y + h - 1, w, color)
        self.writeFastVLine(x, y, h, color)
        self.writeFastVLine(x + w - 1, y, h, color)
            
            
    def fillRect( self, x, y, w, h, color):
        i = x
        for i in range(x, x + w):
            self.writeFastVLine(i, y, h, color)
            
    def drawFastVLine( self, x, y, h, color):
        self.writeLine( x, y, x, y + h - 1, color)
        
    def drawFastHLine( self, x, y, w, color):
        self.writeLine( x, y, x + w - 1, y, color)
        
    def writeFastHLine( self, x, y, w, color):
        self.drawFastHLine( x, y, w, color) 
        
    def writeFastVLine( self, x, y, h, color):
        self.drawFastVLine( x, y, h, color)
        
    def writeLine(self, x0, y0, x1, y1, color):
        # print("x0: {0}, x1: {1}, y0: {2}, y1: {3}".format(x0, x1, y0, y1))  
        steep = abs(y1 - y0) > abs(x1 - x0)
        if steep:       # if steep, swap x0 and x1 / y0 and y1
            x0, y0 = y0, x0
            x1, y1 = y1, x1
            
        if (x0 > x1):
            x0, x1 = x1, x0
            y0, y1 = y1, y0
            
            # Brosenham's algorithm - thx wikibedia
        dx = x1 - x0
        dy = abs(y1 - y0)
        err = dx / 2
        if (y0 < y1):
            ystep = 1
        else:
            ystep = -1
        for x0 in range(x0, x1 + 1):
            if (steep):
                self._pixel(int(y0), int(x0), color)
            else:
                self._pixel(int(x0), int(y0), color)
            err -= dy
            if (err < 0):
                y0 += ystep
                err += dx
                
    def drawLine(self, x0, y0, x1, y1, color):
        if (x0 == x1):
            if (y0 > y1):
                y0, y1 = y1, y0
            self.drawFastVLine(x0, y0, y1 - y0 + 1, color)
        elif (y0 == y1):
            if (x0 > x1):
                x0, x1 = x1, x0
            self.drawFastHLine(x0, y0, x1 - x0 + 1, color)
        else:
            self.writeLine(x0, y0, x1, y1, color)
            
    
    def writeFillRect( self, x, y, w, h, color): 
        self.fillRect( x, y, w, h, color)
        
    def drawCircle(self, x0, y0, r, color):
        f = 1 - r
        ddF_x = 1
        ddF_y = -2 * r
        x = 0
        y = r
        
        self._pixel(x0, y0 + r, color)
        self._pixel(x0, y0 - r, color)
        self._pixel(x0 + r, y0, color)
        self._pixel(x0 - r, y0, color)
        tf = 0
        while x < y:
            
            if f >= 0:
                tf = f
                #y--
                y -= 1
                #f += 2
                ddF_y += 2
                f += ddF_y
            
            
            # x++
            x += 1
            ddF_x += 2
            f += ddF_x
            
            self._pixel(x0 + x, y0 + y, color)
            self._pixel(x0 - x, y0 + y, color)
            self._pixel(x0 + x, y0 - y, color)
            self._pixel(x0 - x, y0 - y, color)
            self._pixel(x0 + y, y0 + x, color)
            self._pixel(x0 - y, y0 + x, color)
            self._pixel(x0 + y, y0 - x, color)
            self._pixel(x0 - y, y0 - x, color)
         
            
            
    def drawCircleHelper(self, x0, y0, r, cornername, color):
        f = 1 - r
        ddF_x = 1
        ddF_y = -2 * r 
        x = 0
        y = r
        
        tf = f
        while x < y:
        
            if (f >= 0):
                # y--   y -= 1 below
                y -= 1
                ddF_y += 2
                f += ddF_y
                
            
        #   x++ 
            ddF_x += 2
            f += ddF_x
            
            if (cornername & 0x4):
                self._pixel(x0 + x, y0 + y, color)
                self._pixel(x0 + y, y0 + x, color)
            
            if (cornername & 0x2):
                self._pixel(x0 + x, y0 - y, color)
                self._pixel(x0 + y, y0 - x, color)
        
            if (cornername & 0x8):
                self._pixel(x0 - y, y0 + x, color)
                self._pixel(x0 - x, y0 + y, color)
            
            if (cornername & 0x1):
                self._pixel(x0 - y, y0 - x, color)
                self._pixel(x0 - x, y0 - y, color)
            x += 1
            
    def fillCircle( self, x0, y0, r, color):
        self.writeFastVLine(x0, y0 - r, 2 * r + 1, color)
        self.fillCircleHelper(x0, y0, r, 3, 0, color)
        
        
    def fillCircleHelper(self,  x0, y0, r, cornername, delta, color):
        # print("entry x0: {0}; y0: {1}; r: {2}; corname: {3}; delta: {4}".format(x0, y0, r, cornername, delta))
        f = 1 - r 
        ddF_x = 1
        ddF_y = -2 * r 
        x = 0
        y = r 
        tf = f
        while x < y:
            # print("x: {0}; y: {1}; f: {2}; ddf_x: {3}; ddf_y: {4}".format(x, y, f, ddF_x, ddF_y))
            if f >= 0:              
                y -= 1
                
                # print("ddf_y: {0}; f: {1}".format(ddF_y, f))
                ddF_y += 2
                f += ddF_y
            
            # x++
            x += 1
            ddF_x += 2
            f += ddF_x
            # print("f: {0}; x: {1}; y: {2}; cname: {3}".format(f, x, y, cornername))
            if (cornername & 0x1):
                # print("Vline at: {0}, {1}, {2}".format(x0+x, y0-y, 2*y+1))
                self.writeFastVLine( x0 + x, y0 - y, 2 * y + 1 + delta, color)
                # print("Vline at: {0}, {1}, {2}".format(x0+y, y0-x, 2*x+1))
                self.writeFastVLine( x0 + y, y0 - x, 2 * x + 1 + delta, color)
                
            if (cornername & 0x2):
                # print("Vline at: {0}, {1}, {2}".format(x0-x, y0-y, 2*y+1))
                self.writeFastVLine( x0 - x, y0 - y, 2 * y + 1 + delta, color)
                # print("Vline at: {0}, {1}, {2}".format(x0-y, y0-x, 2*x+1))
                self.writeFastVLine( x0 - y, y0 - x, 2 * x + 1 + delta, color)
          
            
            
    def drawRoundRect( self, x, y, w, h, r, color):
        self.writeFastHLine(x + r    , y        , w - 2 * r , color)
        self.writeFastHLine(x + r    , y + h - 1, w - 2 * r , color)
        self.writeFastVLine(x        , y + r    , h - 2 * r , color)
        self.writeFastVLine(x + w - 1, y + r    , h - 2 * r , color)
        
        self.drawCircleHelper(x + r        , y + r        , r , 1, color)
        self.drawCircleHelper(x + w - r - 1, y + r        , r , 2, color)
        self.drawCircleHelper(x + w - r - 1, y + h - r - 1, r , 4, color)
        self.drawCircleHelper(x + r        , y + h - r - 1, r , 8, color)
        
        
        
    def fillRoundRect( self, x, y, w, h, r , color):
        self.writeFillRect(x + r           , y, w - 2 * r , h , color)
        # print("I'm back")
        self.fillCircleHelper(x + w - r - 1, y + r               , r , 1, h - 2 * r - 1, color)
        self.fillCircleHelper(x + r        , y + r               , r , 2, h - 2 * r - 1 ,color)
        
    def drawTriangle( self, x0, y0, x1, y1, x2, y2, color):
        self.drawLine(x0, y0, x1, y1, color)
        self.drawLine(x1, y1, x2, y2, color)
        self.drawLine(x2, y2, x0, y0, color)
        
        
    def fillTriangle(self, x0, y0, x1, y1, x2, y2, color):
        if y0 > y1:
            y0, y1 = y1, y0 
            x0, x1 = x1, x0
        
        if y1 > y2:
            y1, y2 = y2, y1
            x1, x2 = x2, x1
            
        if y0 > y1:
            y0, y1 = y1, y0 
            x0, x1 = x1, x0
            
        if (y0 == y2):
            x = b = x0
            if (x1 < a):
                a = x1
            elif x1 > b:
                b = x1
            if (x2 < a):
                a = x2
            elif x2 > b :
                b = x2
            self.writeFastHLine(a, y0, b- a + 1, color)
            return
        dx01 = x1 - x0
        dy01 = y1 - y0
        dx02 = x2 - x0
        dy02 = y2 - y0
        dx12 = x2 - x1
        dy12 = y2 - y1
        
        sa = 0
        sb = 0
        
        if (y1 == y2):
            last = y1 
        else:
            last = y1 - 1
            
        y = y0
        for y in range(y0, last + 1):
            a = x0 + sa / dy01
            b = x0 + sb / dy02
            sa += dx01
            sb += dx02
            if a > b:
                a, b = b, a
            self.writeFastHLine( a, y, b - a + 1, color)
            
        sa = dx12 * (y - y1)
        sb = dx02 * (y - y0)
        for y in range(y, y2 + 1):
            if sa > 0:
                a = x1 + sa / dy12
            else:
                a = x1 + 0
            if sb > 0:
                b = x0 + sb / dy02
            else: 
                b = x0 + 0
            sa += dx12
            sb += dx02
            
            if a > b:
                a, b = b, a     # swap the values
            self.writeFastHLine(a, y, b - a + 1, color)
            
            
        
            
            
    
        
            
            
    
        
        





        
