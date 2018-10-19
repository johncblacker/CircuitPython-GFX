from importlib import import_module
import sys

if len(sys.argv) != 2:
        sys.stderr.write("Usage : python %s fontname(without .py suffix)\n" % sys.argv[0])
        raise SystemExit(1)
font_name = sys.argv[1]
print(font_name)
modfile = import_module(font_name)
fontfile = modfile.GFXfont()
bitmaps = fontfile.GFXbitmaps
outfile = font_name  + '.bin'
outclass = font_name + '.cls'
infile = font_name + '.py'
found = False

with open(outfile, 'wb') as outfile: 
    for font_byte in bitmaps: 
        outfile.write(font_byte.to_bytes(1, 'little')) 


with open(outclass, 'wt') as outclass:
    outclass.write('class GFXfont():\n')
    outclass.write('\tdef __init__(self):\n')
    ifile = open(infile, 'r')
    line = ifile.readline()
    for line in ifile:
        if  not found:
            if 'GFXglyphs' in line:
                found = True
            else:   
                continue
        outclass.write(line)
    
    