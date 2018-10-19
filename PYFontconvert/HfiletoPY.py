from importlib import import_module
import sys

if len(sys.argv) != 2:
        sys.stderr.write("Usage : python %s fontname(without .py suffix)\n" % sys.argv[0])
        raise SystemExit(1)
infile_name = sys.argv[1]
indx = infile_name.rfind('.h', 1)
fontname = infile_name[0: indx]   # drop .h suffix
infile = infile_name
print(fontname)

outfile = fontname  + '.bin'
outclass = fontname + '.py'
classdata = False
found = False
ifile = open(infile_name, 'r')
line = ifile.readline()     # toss first line
print(line)
bmcount = 0
with open(outfile, 'wb') as outfile: 
    while (not classdata):
        line = ifile.readline()
        print(line)
        # print(line.find("};"))
        if (line.find("};", 0, len(line)) != -1):  #  watch for end of bitmap data
            
            classdata = True
            
        a = line.replace(',', '')
        b = a.replace('0x', '')
        c = b.replace(' ', '') 
        d = c.replace("}", '')
        e = d.replace(";", '')
        outfile.write(bytes.fromhex(e))
    print("END OF BITMAPS")      
    
    
while 1:
    line = ifile.readline()
    if (line.isspace() or line.find("[", 0, len(line)) != -1):
        print("skip: %20s" % line)
    else:
        break
        
print("Processing glyphs")
GFXMinYadvance = 0
GFXyadvance = 0
GFXfirst = 0
GFXlast = 0
lastglyph = False

with open(outclass, 'wt') as outclass:
    outclass.write('class GFXfont():\n')
    outclass.write('\tdef __init__(self):\n')
    outclass.write('\t\tself.GFXglyphs = (\n')

    while (not lastglyph):
        if (line.find("};", 0, len(line)) != -1 ):    # last line of glyphs?
                lastglyph = True 
        print("processing glyph: %20s" % line)
        la = line.replace("{", "(")
        lb = la.replace("}", ")")
        lbb = lb.replace(";", '')
        lc = lbb.replace("/", "#")
        ld = lc.replace("(", "")
        le = ld.replace(")", "")
        lf = le.split(",")
    
        print("lf: %s" % lf)
        indx = lf[5].find(";", 0, len(lf[5]))
        xxx = lf[5][0:indx]
        
        yyy = eval(xxx)      # convert line data to a tuple
        print("lf[5]: %s" % lf[5])
        
        GFXMinYadvance = min(GFXMinYadvance, yyy)  # check against yoffset
        outclass.write("\t\t" + lc)
        line = ifile.readline()
    
    print("End of glyph processing...writing metrics.")    
    # outclass.write("\t\t\t)\n")     # closing paren = end of glyphs   
    print("Processing metrics")
    print(line)
    while (line.find("};", 0, len(line)) == -1):
        line = ifile.readline()
        print("skipping: %s" % line[0:20])
    metrics = line.split(",")
    print(metrics[2])
    m2 = metrics[2].replace("}", '')
    m3 = m2.replace(";", '')
    print(m3)
    fstring = "\n\n\t\tself.GFXfirst = {}\n\t\tself.GFXlast = {}\n\t\tself.GFXyadvance = {}".format(metrics[0], metrics[1], m3)
    outclass.write(fstring)
    outclass.write("\t\tself.GFXMinYadvance = " + str(GFXMinYadvance))
                        
    outclass.write("\n\tdef __repr__ (self):")
    outclass.write("\n\t\trows = ''")
    outclass.write("\n\t\tfor y in range(self.height):")
    outclass.write("\n\t\t\tfor x in range(self.width):")
    outclass.write("\n\t\t\t\trows += '*' if self.pixels[y * self.width + x] else ' '")
    outclass.write("\n\t\trows += '\\n'")
    outclass.write("\n\t\treturn rows")
    
    