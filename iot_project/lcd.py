import lcd

import digitalio
import board
import adafruit_pcd8544
import busio
from datetime import datetime
import time

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

# import st7565

# creds to ya boi https://www.google.com/search?q=raspberry+pi+draw+on+lcd&rlz=1C1GEWG_nlNL982NL982&oq=raspberry+pi+draw+on+lcd&aqs=chrome..69i57j33i22i29i30l9.3960j0j9&sourceid=chrome&ie=UTF-8#kpvalbx=_uHhhYqCwBsT2sAea75W4CA16

def initialize_display():
    # Initialize SPI bus
    spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)

    # Initialize display
    dc = digitalio.DigitalInOut(board.D20)  # data/command
    cs1 = digitalio.DigitalInOut(board.CE1)  # chip select CE1 for display
    reset = digitalio.DigitalInOut(board.D16)  # reset
    display = adafruit_pcd8544.PCD8544(spi, dc, cs1, reset, baudrate= 1000000)
    display.bias = 4
    display.contrast = 60
    display.invert = True

    return display

def print_message(message):
    display = initialize_display()


    #  Clear the display.
    display.fill(0)
    display.show()
    
    # Load default font.
    font = ImageFont.load_default()

    # Get drawing object to draw on image
    image = Image.new('1', (display.width, display.height)) 
    draw = ImageDraw.Draw(image)

    # Draw a white filled box to clear the image.
    draw.rectangle((0, 0, display.width, display.height), outline=255, fill=255) 

    draw.text((1,10), message, font=font)

    display.image(image)
    display.show()  

def print_current_time():
    while(True):
        now = datetime.now()

        current_time = now.strftime("%H:%M:%S")
        lcd.print_message("current time:\n" + current_time)
        print("current time:\n" + current_time)
        time.sleep(13)

def clear_display():
    display = initialize_display()
    display.fill(0)

    display.show()

clear_display()
