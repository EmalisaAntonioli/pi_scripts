import lcd

import digitalio
import board
import adafruit_pcd8544
import busio
import time
from datetime import datetime

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

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

    # Draw a row of fishes at the top
    for x in range(3, 80, 20):
        draw.polygon([(x, 3), (x+3, 6), (x, 9)], outline=0, fill=0)
        draw.polygon([(x+3, 6), (x+8, 3), (x+8, 9)], outline=0, fill=0)
        draw.polygon([(x+12, 6), (x+8, 3), (x+8, 9)], outline=0, fill=0)
        draw.point((x+15, 3))
        draw.point((x+14, 6))
        draw.point((x+16, 5))

    # Display the message
    draw.text((2, 14), message, font=font)

    display.image(image)
    display.show()  

def print_current_time():
    # Once every 13 seconds print the current time
    while(True):
        # Retrieve current time
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")

        # Print current time
        lcd.print_message("current time:\n" + current_time)
        time.sleep(13)
