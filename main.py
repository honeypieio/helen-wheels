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

# Number param must be string!

def shift(byte, pinDefinitions):

    #byte = int('{:08b}'.format(byte)[::-1], 2)

    GPIO.output(pinDefinitions["latch"], 0)

    #time.sleep(0.1)

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
    newLine()
    type("3.1415926535897932384626433832795028841 U 6939937510582097494459230781640628620899862803482534211706798214808651328230664709 R 460955058223172535940812848111745028410270193852110555964462294895493038196442881076659334461284756482337867831652712019091456485669234603486104543266482133936072602 M 4127372458700660631558817488152092096282925409171536436789259036001133053054882046 U 1384146951941511609433057270365759591953092186117381932611793105118548074462379962 M 56735188575272489122793818301194912983367336244065664308602139494639522473719070216094370277053921717629317675238467481846766940513200056812714526356082778577134275 G 9609173637178721468440901224953430146549585371050792279689258923542019956112129021 A 8640344181598136297747713099605187072113499999983729780499510597317328160963185950 Y 59455346908302642522308253344685035261931188171010003137838752886587533208381420617177669147303598253490428755468731159562863882353787593751957781857780532171226806613001927876611195909216420198938095257201065485863278865936153381827968230301952035301852968995773622599413891249721775283479131515574857242454150695950829533116861727855889075098381754637464939319255060400927701671139009848824012858361603563707660104710181942955596198946767837449448255379774726847104047534646208046684259069491293313677028989152104752162056966024058038150193511253382430035587640247496473263914199272604269922796782354781636009341721641219924586315030286182974555706749838505494588586926995690927210797509302955321165344987202755960236480654991198818347977535663698074265425278625518184175746728909777727938000816470600161452491921732172147723501414419735685481613611573525521334757418494684385233239073941433345477624168625189835694855620992192221842725502542568876717904946016534668049886272327917860857843838279679766814541009538837863609506800642251252051173929848960841284886269456042419652850222106611863067442786220391949450471237137869609563643719172874677646575739624138908658326459958133904780275900994657640789512694683983525957098258226205224894077267194782684826014769909026401363944374553050682034962524517493996514314298091906592509372216964615157098583874105978859597729754989301617539284681382686838689427741559918559252459539594310499725246808459872736446958486538367362226260991246080512438843904512441365497627807977156914359977001296160894416948685558484063534220722258284886481584560285060168427394522674676788925213852254995466672782398645659611635488623057745649803559363456817432411251507606947945109659609402522887971089314566913686722874894056010150330861792868092087476091782493858900971490967598526136554978189312978482168299894872265880485756401427047755513237964145152374623436454285844479526586782105114135473573952311342716610213596953623144295248493718711014576540359027993440374200731057853906219838744780847848968332144571386875194350643021845319104848100537061")

else:
    try:
        shift(int(sys.argv[1],2), scanRegister)
        shift(int(sys.argv[2],2), returnRegister)
        time.sleep(keyingDelay)
        clearRegisters()
    except:
        type(sys.argv[1])


##type("Hello world!")
