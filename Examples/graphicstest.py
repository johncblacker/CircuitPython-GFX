# /***************************************************
# This is our GFX example for the Adafruit ILI9341 Breakout and Shield
#   ----> http://www.adafruit.com/products/1651

# Check out the links above for our tutorials and wiring diagrams
# These displays use SPI to communicate, 4 or 5 pins are required to
# interface (RST is optional)
# Adafruit invests time and resources providing this open source code,
# please support Adafruit and open-source hardware by purchasing
# products from Adafruit!

# Written by Limor Fried/Ladyada for Adafruit Industries.
# Converted to python by John Blacker, developer of CircuitPython_GFX
# MIT license, all text above must be included in any redistribution
# ****************************************************/

import ariali12pt7b
import CPtGFX as GFX
import ili9341 as ili9341
from Adafruit_rgb_display import color565
import busio
import board
import time
import digitalio

#  color definitions
BLACK = 0x0000
BLUE  = 0x001f
RED   = 0xf800
GREEN = 0x07e0
CYAN  = 0x07ff
MAGENTA = 0xF81F
YELLOW  = 0xffe0
WHITE   = 0xffff

# ILI9341 Display command values
ILI9341_RDMODE    = 0X0A
ILI9341_RDMADCTL = 0X0B
ILI9341_RDPIXFMT = 0X0C
ILI9341_RDIMGFMT = 0X0D
ILI9341_RDSELFDIAG = 0X0F 
ILI9341_MADCTL   = 0X36

# MADCTL values
MADCTL_MY   =   0X80
MADCTL_MX   =   0X40
MADCTL_MV   =   0X20
MADCTL_ML   =   0X10
MADCTL_RGB  =   0X00
MADCTL_BGR  =   0X08
MADCTL_MH   =   0X04

cs = digitalio.DigitalInOut(board.D2)
dc = digitalio.DigitalInOut(board.D7)

spi = busio.SPI(clock=board.SCK, MOSI=board.MOSI, MISO=board.MISO)
# Setup ILI9341 display using TFT FeatherWing pinout for CS & DC pins.
display = ili9341.ILI9341(spi, cs=cs, dc=dc)

display.newWidth(240)
display.newHeight(320)

gfx = GFX.GFX(240, 320, pixel=display.pixel, font_name=ariali12pt7b,
          dispobj=display,
          newWidth=display.newWidth,
          newHeight=display.newHeight)
          

def testText():
    gfx.setFill(BLACK)
    start = time.monotonic()
    gfx.setCursor(0, 0)
    gfx.setTextColor(WHITE);    gfx.setTextSize(1);
    gfx.text("Hello World!\n")
    gfx.setTextColor(YELLOW);   gfx.setTextSize(2);
    gfx.text('1234.56\n')
    gfx.setTextColor(RED);      gfx.setTextSize(3);
    gfx.text('0XDEADBEEF\n')
    gfx.setTextColor(GREEN)
    gfx.setTextSize(5)
    gfx.text("Groop ")
    gfx.setTextSize(2)
    gfx.text("I implore thee, ")
    gfx.setTextSize(1)
    gfx.text("my foonting turlingdromes.")
    gfx.text("And hooptiously drangle me ")
    gfx.text("with crinkly bindlewordles,")
    gfx.text(" Or I will rend thee")
    gfx.text(" in the gobberwarts ")
    gfx.text("with my blurglecruncheon,")
    gfx.text(" see if I don't!")
    return time.monotonic() - start



def testFillScreen():
    start = time.monotonic()
    gfx.setFill(BLACK)
    gfx.setFill(RED)
    gfx.setFill(GREEN)
    gfx.setFill(BLUE)
    gfx.setFill(BLACK)
    return time.monotonic() - start



def testLines(color):
    start = time.monotonic()
    w = gfx.getWidth()
    h = gfx.getHeight()
    gfx.setFill(BLACK)
    x2 = 0
    x1 = y1 = 0
    y2 = h - 1
    start = time.monotonic()
    for x2 in range(0, w, 6):
        gfx.drawLine(x1, y1, x2, y2, color)
    x2 = w - 1;
    for y2 in range (0, h, 6):
        gfx.drawLine(x1, y1, x2, y2, color)
    t = time.monotonic() - start
    gfx.setFill(BLACK)
    x1 = w - 1
    y1 = 0
    y2 = h - 1
    
    start = time.monotonic()
    for x2 in range(0,  w, 6):
        gfx.drawLine(x1, y2, x2, y2, color)
        
    x2 = 0
    for y2 in range(0, h, 6):
        gfx.drawLine(x1, y1, x2, y2, color)
        t += time.monotonic() - start   

    gfx.setFill(BLACK)

    x1 = 0
    y1 = h - 1
    y2 = 0
  
    start = time.monotonic() # 
    
    for x2 in range(0, w, 6):
        gfx.drawLine(x1, y1, x2, y2, color)
        
    x2 = w - 1
    
    for y2 in range(0, h, 6):
        gfx.drawLine(x1, y1, x2, y2, color)
        
    t += time.monotonic() - start
    
    gfx.setFill(BLACK)
  
    x1  = w - 1
    y1  = h - 1
    y2  = 0
    
    start = time.monotonic()
    
    for x2 in range(2, w, 6):
        gfx.drawLine(x1, y1, x2, y2, color)
    x2 = 0
    for y2 in range(0, h, 6):
        gfx.drawLine(x1, y1, x2, y2, color)
  
    t += time.monotonic() - start
    return t
        
def testFastLines(color1, color2):
    w = gfx.getWidth()
    h = gfx.getHeight()
    
    gfx.setFill(BLACK)
    y=x=0
    start = time.monotonic()
    for y in range(0, h, 5):
        gfx.drawFastHLine(0, y, w, color1)
    for x in range(0, w, 5):
        gfx.drawFastVLine(x, 0, h, color2)
        
    return time.monotonic() - start

def testRects(color):
    w = gfx.getWidth()
    h = gfx.getHeight()
    cx = gfx.getWidth() // 2
    cy = gfx.getHeight() // 2
    
    gfx.setFill(BLACK)
    n   =   min(w, h)
    i = 0
    start = time.monotonic()
    for i in range(2, n, 6):
        i2 = i // 2
        gfx.drawRect(cx - i2, cy - i2, i, i, color)
        
    return time.monotonic() - start


def testFillRects(color1, color2):
    cx = gfx.getWidth() // 2 - 1
    cy = gfx.getHeight() // 2 - 1
    
    gfx.setFill(BLACK)
    n = min(gfx.getWidth(), gfx.getHeight())
    
    gfx.setFill(BLACK)
    i = t = 0
    for i in range(n, 0, -6):
        i2 = i // 2 - 1
        start = time.monotonic()
        
        gfx.fillRect(cx - i2, cy - i2, i, i, color1)
        t += time.monotonic() - start
        gfx.drawRect(cx - i2, cy - i2, i, i, color2)
        return time.monotonic() - start

def testFilledCircles(radius, color):
    w = gfx.getWidth()
    h = gfx.getHeight()
    x = y = 0
    gfx.setFill(BLACK)
    r2 = radius * 2
    start = time.monotonic()
    
    for x in range(radius, w, r2):
        for y in range(radius, h, r2):
            gfx.fillCircle(x, y, radius, color)
            
    return time.monotonic() - start


def testCircles(radius, color):
    w = gfx.getWidth()
    h = gfx.getHeight()
    r2 = radius * 2
    x = y = 0
    start = time.monotonic()
    for x in range(0, w, r2):
        for y in range(0, h, r2):
            gfx.drawCircle(x, y, radius, color)
            
    return time.monotonic() - start


def testTriangles():
    cx = gfx.getWidth() //2 - 1
    cy = gfx.getHeight() // 2 - 1
    
    gfx.setFill(BLACK)
    n = min(cx, cy)
    start = time.monotonic()
    i = 0
    for i in range(0, n, 5):
        gfx.drawTriangle(   cx, cy - i, 
                            cx - i, cy + i,
                            cx + i, cy + i,
                            color565(i, i, i))
                            
    return time.monotonic() - start

def testFilledTriangles():
    cx = gfx.getWidth() // 2 - 1
    cy = gfx.getHeight() // 2 - 1
    
    gfx.setFill(BLACK)
    t = 0
    start = 0
    i = 0
    start = time.monotonic()
    for i in range(min(cx, cy), 10, 5):
        start = time.monotonic()
        gfx.fillTriangle( cx, cy - i, cx - i, cy + i, cx + i, cy + i,
                          color565(0, i*20, i*10))
        t += time.monotonic() - start
        
        gfx.drawTriangle( cx, cy - i, cx - i, cy + i, cx + i,
                          cy + i,
                          color565(i*10, i*10, 0))
    return t

def testRoundRects():
    cx = gfx.getWidth() // 2 - 1
    cy = gfx.getHeight() // 2 - 1
    
    gfx.setFill(BLACK)
    
    w = min(gfx.getWidth(), gfx.getHeight())
    start = time.monotonic()
    i = 0
    for i in range(0, w, 6):
        i2 = i // 2
        gfx.drawRoundRect( cx - i2, cy - i2, i, i, i // 8, color565(i, 0, 0))
        
    return time.monotonic() - start

def testFillRoundRects():
    cx = gfx.getWidth() // 2 - 1
    cy = gfx.getHeight() // 2 - 1
    i = 0
   
    m = min(gfx.getWidth() , gfx.getHeight() )
    gfx.setFill(BLACK)
    start = time.monotonic()

    # display.fill_rectangle(0, 50, 100, 100,  RED)
    gfx.fillRoundRect(100, 150, 50, 50, 10, BLUE)
    time.sleep(5)
    return time.monotonic() - start 
    for i in range(m, 20, -6):
        i2 = i // 2
        gfx.fillRoundRect( cx - i2, cy - i2, i, i, i // 8, color565(i2, i * 2, i2))
    return time.monotonic() - start
 
#   Main processing begins here 
# Through the "miracle of subclassing, we're able to issue these commands
print("Power Mode:             %r " % gfx.readDisplayCommand(ILI9341_RDMODE))
print("Memory  access control: %r" % gfx.readDisplayCommand(ILI9341_RDMADCTL))
print("Pixel format:           %r" % gfx.readDisplayCommand(ILI9341_RDPIXFMT))
print("Image format:           %r" % gfx.readDisplayCommand(ILI9341_RDIMGFMT))
print("Self diag flag:         %r" % gfx.readDisplayCommand(ILI9341_RDSELFDIAG))

print("Let the benchmark begin at:        %f" % time.monotonic())
time.sleep(.1)
print("Screen fill                           ")
print(testFillScreen())
time.sleep(.5) 
for rotation in range(0, 4):
    if (rotation == 1 or rotation == 3):
        gfx.setWrapErase(False)
    else:
        gfx.setWrapErase(True)
    gfx.setRotation(rotation)
    testText()
    time.sleep(5) 
print("Lines                                ")
print(testLines(CYAN))  # cyan lines
time.sleep(.5)

print("Horiz/Vert Lines                    ")
print(testFastLines(RED, BLUE))
time.sleep(.5)

print("Rectangles (outline)                ")
print(testRects(GREEN))
time.sleep(.5)

print("Rectangles (filled)                 ")
print(testFillRects(YELLOW, MAGENTA))
time.sleep(.5)

print("Circles (filled )                   ")
print(testFilledCircles(10, MAGENTA))
time.sleep(.5)

print("Circles (outline)                   ")
print(testCircles(10,     WHITE))
time.sleep(.5)

print("Triangles (outline)                 ")
print(testTriangles())
time.sleep(.5)

print("Triangles (filled)                  ")
print(testFilledTriangles())
time.sleep(.5)

print("Rounded rects (outline)             ")
print(testRoundRects())
time.sleep(.5)

print("Rounded rects (filled)                ")
print(testFillRoundRects())
time.sleep(.5)


print("Done!")