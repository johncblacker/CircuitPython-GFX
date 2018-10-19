Programs font-bin.py and HfiletoPY.py are two new conversion programs.  Each has a specific
purpose.  I'm hoping these programs will save having to download the original .ttf files 
for the freetype fonts found in the arduino Adafruit_GFX_Master/font directory.  

font-bin:
Takes old format <fontname>.py files containing the bitmaps and the glyphs in a single files
and extracts the bitmap into a .bin file and puts the glyph data and metrics into another file
with a .cls suffix.  You'd copy these files to the CircuitPython drive and rename the .cls
file to .py.

HfiletoPY:
Takes Adafruit converted font files with a .h file extension (i.e. those found in the Adafruit_GFX_Master fonts directory
and converts them to a bitmap file with a .bin extension and a glyphs and metrics file with and
.py extension.  These are the NEW format font files for the CircuitPython_GFX API CPtGFX.

The fontconvert.exe file takes a <fontname>.ttf file and outputs a .bin file and a .py file.

If this is confusing, send me a message.

