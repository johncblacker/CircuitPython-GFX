# CircuitPython-GFX  (rev: 1.2b)
A python port of the Adafruit_GFX.cpp modules plus test fonts and tools. Included in this repository are: 
- CPtGFX.py, a python port of the Adafruit_GFX.cpp module; 
- a binary version of the mpy-cross compiler compiled under Windows 10; 
- a special version of the Adafruit fontconvert program that outputs font files compatible with the CPtGFX.py module; 
- several pre-converted font files to get the user started and allowing the user to see what the converted font files look like.  
- rev: 1.2b changes result in two font files being written <fontname>.py and <fontname>.bin;
Converted font files (TTF'S) are in python code format so that they can be imported into the CPtGFX module at runtime.  

The converted version of the GFX.cpp file contains the most useful functions.  I undertook this conversion because Adafruit Industries didn't have an acceptable version of the GFX module, written in python with support for the ILI9341 (and similar) displays.  It is my understanding that more robust (and faster) support is under development at Adafruit, but no timeline has been provided.

Functions provided in the CPtGFX.py module are:
  - setFont
  - deinit
  - draw_char - draws characters either in the default font (5x8) or custom (converted TTF) font
  - setTextColor
  - getTextColor
  - setBgColor
  - getBgColor
  - setCursor
  - getCursor
  - setTextSize
  - getTextSize
  - setTextWrap
  - getTextWrap
  - getBitmap - retrieves the bit map for a single character from the converted font file
  - text      - output a line of text to the display
  - charBounds  - calculate the bounds for a single character based on values in the converted font file
  - getTextBounds - calculate the size of a rectangle that will surround a line of text (used to enable having a different background
                         - in order to highlight a string of text.
  - width - return the font width value
  - writerectangle
  - drawRect
  - fillRect
  - fillWRect - faster version of above if w > h
  - drawFastVLine
  - drawFastHLine
  - writeFastHLine
  - writeFastVLine
  - writeLine - a python version of Brosenham's algorithm - thx wikipedia and Adafruit Industries
  - drawLine
  - writeFillRect
  - drawCircle
  - drawCircleHelper  - used internally
  - fillCircle
  - fillCircleHelper  - used internally
  - drawRoundRect - draw a rectangle with rounded corners
  - fillRoundRect
  - drawTriangle
  - fillTriangle
  - setRotation -   Rotate display into one of 4 different positions
  - setScroll   -   enable scrolling
  - readDisplayCommand -    issue a read command to the ILI9341 hardware
  - writeDisplayCommand -   issue a write command to the ILI9341 hardware
  
  It's important to understand that although the screen (ILI9341, for example) specifies that x=0, y=0 is the upper left and default fonts wiil be rendered using the upper left as the base cursor position; converted fonts use the lower left corner of the "boundary box" as the baseline.  Take a look at the converted font files and you'll see that the "y" offset in the character glyph's is a negative number.  Point is, you'll have to do a little experimenting to find the ideal position for your lines.  If you were to write a line of text at point (0,0) you'd just see a single pixel line!  Read the write-up about the Adafruit GFX Graphics Library available on their website.  most of the graphics drawing (and text) functions follow the conventions outlined in the aforementioned write-up.  I've provided a basic test program that can be used to get started and provide some understanding of how to use this library.
  
Also included are several font converted font files to get started with for for reference; a compiled version of the mpy-cross.exe program which can be used to pre-compile the CPtGFX.py program into a .mpy file that's significantly smaller that the .py version.  
Lastly, a pre-compiled .cpp fontconvert program is provided to product python compatible versions of font files, since to include freetype as part of CircuitPython is probably not feasible.  The converted font file is a python CLASS called GFXFONT and contains bitmaps, glyphs, several font related constants and a _repr_ function so the GFXFONT could be printed.
Rev: 1.2b changes have resulted in a smaller API footprint because the font bitmap data now resides in a .bin file on the CircuitPython drive.
Rev: 1.2b changes are in the "testing" branch on Github.

Report any and all problems so I can correct them.  If you want to take a stab at providing canvas and frame type functions like those in the original GFX.cpp file, have at it.  I don't think it's worth the time.

One caution:  although this module supports text sizes for converted fonts (doesn't work on default font) it is painfully slow, but does work.  I've tested writing several characters with a text size of 2 (set.TextSize(2)) but it was slow - partially, I think, because the displays are using SPI currently.  Perhaps when they are supported via BUS, things will be much quicker.

Good luck, have fun.
