import CPtGFX as CPtGFX
import ariali12pt7b as ariali12pt7b
from Adafruit_rgb_display import ili9341 as ili9341, color565
import busio
import board
import time
import digitalio

cs = digitalio.DigitalInOut(board.D2)
dc = digitalio.DigitalInOut(board.D7)

ILI9341_RDMODE    = 0X0A
ILI9341_RDMADCTL = 0X0B
ILI9341_RDPIXFMT = 0X0C
ILI9341_RDIMGFMT = 0X0D
ILI9341_MADCTL   = 0X36

# MADCTL values
MADCTL_MY   =   0X80
MADCTL_MX   =   0X40
MADCTL_MV   =   0X20
MADCTL_ML   =   0X10
MADCTL_RGB  =   0X00
MADCTL_BGR  =   0X08
MADCTL_MH   =   0X04


# Setup hardware SPI at 32mhz on ESP8266 MicroPython.

spi = busio.SPI(clock=board.SCK, MOSI=board.MOSI, MISO=board.MISO)

print("time                 %f" % time.monotonic())
# Setup ILI9341 display using TFT FeatherWing pinout for CS & DC pins.
display = ili9341.ILI9341(spi, cs=cs, dc=dc)  
black = color565(0, 0, 0)
# print("black=%d" % black)
white = color565(255, 255, 255)
# print("white=%d" % white)
green = color565(0, 255, 0)
# print("green=%d" % green)
blue = color565(0, 0, 255)
# print("blue=%d" % blue)
gfx = CPtGFX.GFX(240, 320, pixel=display.pixel, font_name=ariali12pt7b, 
                 read=display.read,
                 write=display.write, 
                 fill=display.fill, 
                 scroll=display.scroll)
                    
print(gfx.readDisplayCommand(ILI9341_RDMODE))  
print(gfx.readDisplayCommand(ILI9341_RDMADCTL))
gfx.setFill(0)
gfx.setRotation(1) 
# mba = bytearray([MADCTL_MX | MADCTL_BGR])
# display.write(command=ILI9341_MADCTL, data=mba)
print(gfx.readDisplayCommand(ILI9341_RDMADCTL))
gfx.setTextSize(1)
gfx.setCursor(0, 20)
gfx.setTextColor(color565(0, 255, 0))
gfx.setBgColor(color565(0, 0, 0))
gfx.setFill(0)
gfx.text('Landscape')
time.sleep(5)
# gfx.setFill(black)
gfx.setCursor(0, 20)
gfx.setRotation(0)
gfx.text('Normal...')
time.sleep(3)
gfx.setRotation(2)
gfx.setCursor(0, 20)
gfx.text('Portrait Inverted...')
gfx.setRotation(3)
gfx.setCursor(0, 20)
gfx.text('landscape rev...')

# gfx.setRotation(1)
# gfx.fill(black)
# gfx.text('Randi')
# time.sleep(4)
# cx, cy = gfx.getCursor()
# print(cx, cy)
# gfx.setCursor(0, 160)
# gfx.setTextSize(1)
# display.fill(0)
# y = 160
# x = 0
# x1, y1, w, h = gfx.getTextBounds('John', x, y)
# print(x1, y1, w, y)
# gfx.fillRect(x, y1 , w, h, color565(255, 0, 0))
# gfx.setCursor(x, y)
# gfx.setTextColor(color565(0, 0, 255))
# gfx.setBgColor(0)
# gfx.text('John')
# tx, ty = gfx.getCursor()
# print(tx, ty)
# gfx.setCursor(x, y + 30)

# i = 0
# while i < 20:
#     gfx.setScroll(3)
#     i += 1
#     time.sleep(1)

# gfx.text('JB')
# gfx.setCursor(x+40, y)
# gfx.text('JB')
# gfx.setTextColor(color565(255, 0, 0))
# gfx.setTextSize(1)
# display.pixel(150, 150, color565(255, 0, 0))

# value = gfx.getBitmap('E')
# print(value)
# for byte in range(0, len(value)):
# print(bin(value[byte]).replace('1','*').replace('0',' '))
# print(bin(value[byte]))
# print("END OF bitmap print in binary *************")
# gfx.setCursor(0, 30)
# gfx.setBgColor(color565(0, 0, 0))
# gfx.setTextColor(color565(0, 255, 50))
# gfx.text('John ROCKS! This is an extremely long line of text...')
# gfx.text('This begins where the other ends...I hope!')
# gfx.setTextColor(color565(100, 255, 100))
# gfx.setTextSize(1)
# tin = time.monotonic()

# gfx.text('Liberals are disgusting')
# tout = time.monotonic() - tin
# print(time.monotonic() - tin)
# gfx.drawRect(120, 170, 50, 50, color565(0, 0, 255))
# gfx.drawCircle(50, 50, 25, color565(0, 255, 0))
# time.sleep(2)
#gfx.setTextColor(color565(0,0,255))
# gfx.fillTriangle(100, 100, 125, 75, 150, 100, color565(0, 0, 255))

# time.sleep(2)
# gfx.drawRect(150, 200, 50, 40, color565(255, 100, 255))
# gfx.fillRoundRect(50, 200, 80, 50, 10, color565(244, 155, 66))
# time.sleep(2)
# gfx.setTextColor(color565(244, 244, 66))
# gfx.writeFillRect(175, 100, 40, 40, color565(255,255, 255))

# gfx.fillCircle(75, 80, 25, color565(244, 244, 66))
# gfx.fillRoundRect(75, 80, 50, 50, 10, color565(50, 200, 150))
# time.sleep(2)
# cx = gfx._width / 2
# cy = gfx._height / 2
# print(cx, cy)
# display.fill(0)
# n = min([gfx._width, gfx._height])

# for i in range(2, n, 20):
#     i2 = i / 2
#     gfx.drawRect(cx-i2, cy-i2, i, i, color565(0, 0, 255))

# end of program