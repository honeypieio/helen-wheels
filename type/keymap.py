def flipByte(byte):
    return int('{:08b}'.format(byte)[::-1], 2)

def combineBytes(byte1, byte2):
  newByte = ""
  for i in range(8):
    bit1 = str((byte1 >> i) & 1)
    bit2 = str((byte2 >> i) & 1)
    if bit1 == "0" and bit2 == "0":
        newByte += "0"
        #print("0")
    else:
        newByte += "1"
        #print("1")

  return flipByte(int(newByte, 2))

keymap = {
    "1": {
        "scan": 0b00000001,
        "return": 0b00000001
    },
    "2": {
        "scan": 0b00000010,
        "return": 0b00000010
    },
    "3": {
        "scan": 0b00000001,
        "return": 0b00000010
    },
    "4": {
        "scan": 0b00000010,
        "return": 0b00000100
    },
    "5": {
        "scan": 0b000000001,
        "return": 0b00000100
    },
    "6": {
        "scan": 0b000000010,
        "return": 0b00001000
    },
    "7": {
        "scan": 0b000000001,
        "return": 0b00001000
    },
    "8": {
        "scan": 0b000000010,
        "return": 0b00010000
    },
    "9": {
        "scan": 0b000000001,
        "return": 0b00010000
    },
    "0": {
        "scan": 0b00000010,
        "return": 0b00100000
    },
    "=": {
        "scan": 0b00000010,
        "return": 0b01000000
    },
    "q": {
        "scan": 0b00001000,
        "return": 0b00000001
    },
    "w": {
        "scan": 0b00000100,
        "return": 0b00000010
    },
    "e": {
        "scan": 0b00001000,
        "return": 0b00000010
    },
    "r": {
        "scan": 0b000000100,
        "return": 0b00000100
    },
    "t": {
        "scan": 0b00001000,
        "return": 0b00000100
    },
    "y": {
        "scan": 0b00000100,
        "return": 0b00001000
    },
    "u": {
        "scan": 0b00001000,
        "return": 0b00001000
    },
    "i": {
        "scan": 0b00000100,
        "return": 0b00010000
    },
    "o": {
        "scan": 0b00001000,
        "return": 0b00010000
    },
    "p": {
        "scan": 0b00000100,
        "return": 0b00100000
    },
    "-": {
        "scan": 0b00001000,
        "return": 0b00100000
    },
    "[": {
        "scan": 0b00000100,
        "return": 0b01000000
    },
    "a": {
        "scan": 0b00100000,
        "return": 0b00000001
    },
    "s": {
        "scan": 0b00100000,
        "return": 0b00000010
    },
    "d": {
        "scan": 0b00010000,
        "return": 0b00000010
    },
    "f": {
        "scan": 0b00100000,
        "return": 0b00000100
    },
    "g": {
        "scan": 0b00010000,
        "return": 0b00000100
    },
    "h": {
        "scan": 0b00100000,
        "return": 0b00001000
    },
    "j": {
        "scan": 0b00010000,
        "return": 0b00001000
    },
    "k": {
        "scan": 0b00100000,
        "return": 0b00010000
    },
    "l": {
        "scan": 0b00010000,
        "return": 0b00010000
    },
    ";": {
        "scan": 0b00100000,
        "return": 0b00100000
    },
    "]": {
        "scan": 0b00010000,
        "return": 0b00100000
    },
    "z": {
        "scan": 0b01000000,
        "return": 0b00000001
    },
    "x": {
        "scan": 0b01000000,
        "return": 0b00000010
    },
    "c": {
        "scan": 0b01000000,
        "return": 0b00000100
    },
    "v": {
        "scan": 0b10000000,
        "return": 0b00001000
    },
    "b": {
        "scan": 0b01000000,
        "return": 0b00001000
    },
    "n": {
        "scan": 0b10000000,
        "return": 0b00010000
    },
    "m": {
        "scan": 0b01000000,
        "return": 0b00010000
    },
    ",": {
        "scan": 0b10000000,
        "return": 0b00100000
    },
    ".": {
        "scan": 0b01000000,
        "return": 0b00100000
    },
    "½": {
        "scan": 0b01000000,
        "return": 0b01000000
    },
    " ": {
        "scan": 0b10000000,
        "return": 0b01000000
    },
    "{{{enter}}}": {
        "scan": 0b00100000,
        "return": 0b10000000
    },
    "{{{LSH}}}": {
        "scan": 0b10000000,
        "return": 0b00000001
    },
    "{{{CODE}}}": {
        "scan": 0b10000000,
        "return": 0b00000100
    },
    "{{{caps}}}": {
        "scan": 0b00010000,
        "return": 0b00000001
    }

}

keymap["*"] = {
        "method": "shift",
        "scan": combineBytes(keymap["1"]["scan"], keymap["{{{LSH}}}"]["scan"]),
        "return": combineBytes(keymap["1"]["return"], keymap["{{{LSH}}}"]["return"])
}

keymap["\""] = {
	"method": "shift",
        "scan": combineBytes(keymap["2"]["scan"], keymap["{{{LSH}}}"]["scan"]),
        "return": combineBytes(keymap["2"]["return"], keymap["{{{LSH}}}"]["return"])
}

keymap["/"] = {
	"method":"shift",
        "scan": combineBytes(keymap["3"]["scan"], keymap["{{{LSH}}}"]["scan"]),
        "return": combineBytes(keymap["3"]["return"], keymap["{{{LSH}}}"]["return"])
}

keymap["$"] = {
	"method": "shift",
        "scan": combineBytes(keymap["4"]["scan"], keymap["{{{LSH}}}"]["scan"]),
        "return": combineBytes(keymap["4"]["return"], keymap["{{{LSH}}}"]["return"])
}

keymap["£"] = {
	"method":"shift",
        "scan": combineBytes(keymap["5"]["scan"], keymap["{{{LSH}}}"]["scan"]),
        "return": combineBytes(keymap["5"]["return"], keymap["{{{LSH}}}"]["return"])
}

keymap["_"] = {
	"method": "shift",
        "scan": combineBytes(keymap["6"]["scan"], keymap["{{{LSH}}}"]["scan"]),
        "return": combineBytes(keymap["6"]["return"], keymap["{{{LSH}}}"]["return"])
}

keymap["&"] = {
        "scan": (keymap["7"]["scan"] + keymap["{{{LSH}}}"]["scan"]),
        "return": (keymap["7"]["return"] + keymap["{{{LSH}}}"]["return"])
}

keymap["'"] = {
        "scan": (keymap["8"]["scan"] + keymap["{{{LSH}}}"]["scan"]),
        "return": (keymap["8"]["return"] + keymap["{{{LSH}}}"]["return"])
}

keymap["("] = {
        "scan": (keymap["9"]["scan"] + keymap["{{{LSH}}}"]["scan"]),
        "return": (keymap["9"]["return"] + keymap["{{{LSH}}}"]["return"])
}

keymap[")"] = {
        "scan": (keymap["0"]["scan"] + keymap["{{{LSH}}}"]["scan"]),
        "return": (keymap["0"]["return"] + keymap["{{{LSH}}}"]["return"])
}

keymap["+"] = {
        "scan": (keymap["="]["scan"] + keymap["{{{LSH}}}"]["scan"]),
        "return": (keymap["="]["return"] + keymap["{{{LSH}}}"]["return"])
}

keymap["?"] = {
        "scan": (keymap["-"]["scan"] + keymap["{{{LSH}}}"]["scan"]),
        "return": (keymap["-"]["return"] + keymap["{{{LSH}}}"]["return"])
}

keymap["!"] = {

	"method":"shift",
        "scan": combineBytes(keymap["["]["scan"], keymap["{{{LSH}}}"]["scan"]),
        "return": combineBytes(keymap["["]["return"], keymap["{{{LSH}}}"]["return"])
}

keymap[":"] = {
	"method":"shift",
        "scan": combineBytes(keymap[";"]["scan"], keymap["{{{LSH}}}"]["scan"]),
        "return": combineBytes(keymap[";"]["return"], keymap["{{{LSH}}}"]["return"])
}

keymap["@"] = {
        "scan": (keymap["]"]["scan"] + keymap["{{{LSH}}}"]["scan"]),
        "return": (keymap["]"]["return"] + keymap["{{{LSH}}}"]["return"])
}

keymap["<"] = {
	"method":"code",
        "scan": combineBytes(keymap[","]["scan"], keymap["{{{CODE}}}"]["scan"]),
        "return": combineBytes(keymap[","]["return"], keymap["{{{CODE}}}"]["return"])
}

keymap[">"] = {
	"method": "code",
        "scan": combineBytes(keymap["."]["scan"], keymap["{{{CODE}}}"]["scan"]),
        "return": combineBytes(keymap["."]["return"], keymap["{{{CODE}}}"]["return"])
}

keymap["%"] = {
        "scan": (keymap["½"]["scan"] + keymap["{{{LSH}}}"]["scan"]),
        "return": (keymap["½"]["return"] + keymap["{{{LSH}}}"]["return"])
}

keymap["#"] = {
        "scan": (keymap["½"]["scan"] + keymap["{{{CODE}}}"]["scan"]),
        "return": (keymap["½"]["return"] + keymap["{{{CODE}}}"]["return"])
}

'''
FUNCTION KEYS

key	scan		return

CL	00001000	00000000 (0000001?) # flipped.
LSH	00000001	00000001 # flipped.
RSH	00000001	00000010
ENT
CODE 	00000001	00100000
'''
