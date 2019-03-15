import RPi.GPIO as GPIO

import time
import keymap

CharsPerLine = 65

keyingDelay = 0.1

# Turn off warnings from RPi library
GPIO.setwarnings(False)

# Using Broadcom chip's pin layout
GPIO.setmode(GPIO.BCM)

# Pin definitions
scanRegister = {
    "clock": 17,  # Physical is 11
    "latch": 27,  # "" 13
    "data": 22  # "" 15
}

GPIO.setup(scanRegister["clock"], GPIO.OUT)
GPIO.setup(scanRegister["latch"], GPIO.OUT)
GPIO.setup(scanRegister["data"], GPIO.OUT)

returnRegister = {
    "clock": 18,  # Physical is 12
    "latch": 23,  # "" 16
    "data": 24  # "" 18
}

GPIO.setup(returnRegister["clock"], GPIO.OUT)
GPIO.setup(returnRegister["latch"], GPIO.OUT)
GPIO.setup(returnRegister["data"], GPIO.OUT)

def type(toBeTyped):
    # Wrap text.
    for character in toBeTyped:
        shift(keymap[character]["scan"], scanRegister)
        shift(keymap[character]["return"], returnRegister)
        shift(0b00000000, scanRegister)
        shift(0b00000000, returnRegister)
        time.sleep(keyingDelay)

# Number param must be string!

def shift(byte, pinDefinitions):

    # Reverse bit order.
    byte = int('{:08b}'.format(byte)[::-1], 2)

    GPIO.output(pinDefinitions["latch"], 0b00000000)

    for i in range(8):
        print(byte >> i & 0b00000001)
        GPIO.output(pinDefinitions["data"], byte >> i & 0b00000001)
        GPIO.output(pinDefinitions["clock"], 0b00000001)
        GPIO.output(pinDefinitions["clock"], 0b00000000)

    print("\n\n")
    GPIO.output(pinDefinitions["latch"], 0b00000001)
