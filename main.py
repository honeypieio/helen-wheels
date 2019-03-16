import sys, time, datetime


from RPi import GPIO
from type.keymap import keymap

charsPerLine = 65

keyingDelay = 0.05

# Turn off warnings from RPi library
GPIO.setwarnings(False)

# Using Broadcom chip's pin layout
GPIO.setmode(GPIO.BCM)

# Pin definitions
scanRegister = {
    "clock": 17,  # Physical is 11
    "latch": 27,  # "" 13
    "data": 22    # "" 15
}

GPIO.setup(scanRegister["clock"], GPIO.OUT)
GPIO.setup(scanRegister["latch"], GPIO.OUT)
GPIO.setup(scanRegister["data"], GPIO.OUT)

returnRegister = {
    "clock": 18,  # Physical is 12
    "latch": 23,  # Physical is 16
    "data": 24    # "" 18
}

GPIO.setup(returnRegister["clock"], GPIO.OUT)
GPIO.setup(returnRegister["latch"], GPIO.OUT)
GPIO.setup(returnRegister["data"], GPIO.OUT)

def type(toBeTyped):
    # Wrap text.
    count = 0
    for character in toBeTyped:
        count += 1
        print(character)

        upperCase = False

        if character.isupper():
            upperCase = True
            character = character.lower()
            toggleCapslock("on")

        #print(keymap[character])
        try:
            if keymap[character]["method"] == "shift":
                print("Engaging shift key!")
                print(format(keymap["{{{LSH}}}"]["scan"], '#010b'))
                print(format(keymap["{{{LSH}}}"]["return"], '#010b'))
                shift(keymap["{{{LSH}}}"]["scan"], scanRegister)
                shift(keymap["{{{LSH}}}"]["return"], returnRegister)
            elif keymap[character]["method"] == "code":
                print("Engaging code key!")
                shift(keymap["{{{CODE}}}"]["scan"], scanRegister)
                shift(keymap["{{{CODE}}}"]["return"], returnRegister)

            time.sleep(keyingDelay * 3)

        except:
            print()

        print(format(keymap[character]["scan"], '#010b'))
        print(format(keymap[character]["return"], '#010b'))

        print("\n");

        shift(keymap[character]["scan"], scanRegister)
        shift(keymap[character]["return"], returnRegister)

        time.sleep(keyingDelay)

        clearRegisters()

        time.sleep(keyingDelay)

        if count % charsPerLine == 0:
            newLine()

        if upperCase == True:
            toggleCapslock("off")


    newLine()


def newLine():
    print("newline")
    shift(keymap["{{{enter}}}"]["return"], returnRegister)
    shift(keymap["{{{enter}}}"]["scan"], scanRegister)
    time.sleep(keyingDelay)
    clearRegisters()

def toggleCapslock(mode):
    print("Toggle caps lock " + mode)
    if mode == "on":
    	shift(keymap["{{{caps}}}"]["return"], returnRegister)
    	shift(keymap["{{{caps}}}"]["scan"], scanRegister)
    else:
        shift(keymap["{{{LSH}}}"]["return"], returnRegister)
        shift(keymap["{{{LSH}}}"]["scan"], scanRegister)

    time.sleep(keyingDelay)
    clearRegisters()
    time.sleep(keyingDelay)

def flipByte(byte):
    return int('{:08b}'.format(byte)[::-1], 2)


def shift(byte, pinDefinitions):

    GPIO.output(pinDefinitions["latch"], 0)

    for i in range(8):
        #print(byte >> i & 1)
        GPIO.output(pinDefinitions["clock"], 0)
        GPIO.output(pinDefinitions["data"], (byte >> i) & 1)
        GPIO.output(pinDefinitions["clock"], 1)

    #print("\n")
    GPIO.output(pinDefinitions["latch"], 1)


def clearRegisters():
    shift(0b00000000, scanRegister)
    shift(0b00000000, returnRegister)


if sys.argv[1] == "high":
    shift(0b11111111, scanRegister)
    shift(0b11111111, returnRegister)
elif sys.argv[1] == "low":
    shift(0b00000000, scanRegister)
    shift(0b00000000, returnRegister)
elif sys.argv[1] == "return":
    newLine()
elif sys.argv[1] == "caps":
    shift(keymap["{{{caps}}}"]["scan"], scanRegister)
    shift(keymap["{{{caps}}}"]["return"], returnRegister)
    time.sleep(keyingDelay)
    clearRegisters()

elif sys.argv[1] == "startup":
    now = datetime.datetime.now()
    type("HELEN WHEELS v1.0   " + str(now.year) + "." + str(now.month) + "." + str(now.day))
    newLine()
    newLine()

else:
    try:
        shift(int(sys.argv[1],2), scanRegister)
        shift(int(sys.argv[2],2), returnRegister)
        time.sleep(keyingDelay)
        clearRegisters()
    except:
        type(sys.argv[1])

