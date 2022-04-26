
#!/usr/bin/env python3 
import time
import busio
import digitalio
import board
import adafruit_pcd8544
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from adafruit_bus_device.spi_device import SPIDevice


def readadc(adcnum): 
	if ((adcnum > 7) or (adcnum < 0)): 
		return -1 
	with adc:
		r = bytearray(3)
		spi.write_readinto([1,(8+adcnum)<<4,0], r)
		time.sleep(0.000005)
		adcout = ((r[1]&3) << 8) + r[2] 
		return adcout 


# Initialize SPI bus
spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)

# Initialize control pins for adc
cs0 = digitalio.DigitalInOut(board.CE0)  # chip select
adc = SPIDevice(spi, cs0, baudrate= 1000000)

# Initialize display
dc = digitalio.DigitalInOut(board.D20)  # data/command
cs1 = digitalio.DigitalInOut(board.CE1)  # chip select CE1 for display
reset = digitalio.DigitalInOut(board.D16)  # reset
display = adafruit_pcd8544.PCD8544(spi, dc, cs1, reset, baudrate= 1000000)
display.bias = 4
display.contrast = 60
display.invert = True

#  Clear the display.  Always call show after changing pixels to make the display update visible!
display.fill(0)
display.show()

# Load default font.
font = ImageFont.load_default()
#font=ImageFont.truetype("/usr/share/fonts/truetype/freefont/FreeSansBold.ttf", 10)

# Get drawing object to draw on image
image = Image.new('1', (display.width, display.height)) 
draw = ImageDraw.Draw(image)
 	
# Draw a white filled box to clear the image.
draw.rectangle((0, 0, display.width, display.height), outline=255, fill=255)

# Write some text.
nummer=4
# in0=readadc(0)
draw.text((1,0), 'ADC value', font=font)
draw.text((1,8), 'on display', font=font)
# draw.text((1,16), f'in0={in0}', font=font)
# draw.text((1,32), (str(nummer)), font=font)
display.image(image)
display.show()

# print(in0)
