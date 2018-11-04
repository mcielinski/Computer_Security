import operator


def setCryptograms(path):
    cryptograms = []
    maxLine = 0

    with open(path) as f:
        for line in f:
            splitedLine = line.split()

            for i in range(len(splitedLine)):
                splitedLine[i].strip()

            if len(splitedLine) > maxLine:
                maxLine = len(splitedLine)

            cryptograms.append(splitedLine)

    return cryptograms, maxLine


def generateKey(maxLine, cryptograms, alphabet):
    key = []

    for i in range(maxLine):
        indexKeys = {}

        for cryptogram in cryptograms:

            if len(cryptogram) > i:
                for letter in alphabet.keys():
                    xorKey = operator.xor(int(cryptogram[i], 2), ord(letter))
                    letterFrequency = alphabet.get(letter)

                    if xorKey in indexKeys:
                        indexKeys[xorKey] = indexKeys[xorKey] + letterFrequency
                    else:
                        indexKeys[xorKey] = letterFrequency

        indexKeys = sorted(indexKeys.items(), key=operator.itemgetter(1), reverse=True)
        key.append(findBestKey(i, alphabet, cryptograms, dict(indexKeys)))

    return key


def findBestKey(i, alphabet, cryptograms, indexKeys):
    bestKey = int(ord(' '))
    maxCryptogramsFitted = 0

    for indexKey in indexKeys.keys():
        cryptogramFitted = 0

        for cryptogram in cryptograms:
            if len(cryptogram) > i:
                if isInAlphabet(operator.xor(int(cryptogram[i], 2), indexKey), alphabet):
                    cryptogramFitted += 1

        if cryptogramFitted > maxCryptogramsFitted:
            maxCryptogramsFitted = cryptogramFitted
            bestKey = indexKey

    return bestKey


def isInAlphabet(letter,alphabet):

    return chr(letter) in alphabet.keys()


def printMessage(message,key):

    for i in range(len(message)):
        print(chr(operator.xor(message[i], key[i])), end="")


def getData(path):
    message = []
    with open(path) as f:
        for line in f:
            splitedLine = line.split()

            for i in range(len(splitedLine)):
                splitedLine[i] = int(splitedLine[i], 2)
            message = splitedLine

    return message


alphabet = {
' ': 10.0,
'a': 8.91,
'i': 8.21,
'o': 7.75,
'e': 7.66,
'z': 5.64,
'n': 5.52,
'r': 4.69,
'w': 4.65,
's': 4.32,
't': 3.98,
'c': 3.96,
'y': 3.76,
'k': 3.51,
'd': 3.25,
'p': 3.13,
'm': 2.80,
'u': 2.50,
'j': 2.28,
'l': 2.10,
'ł': 1.82,
',': 1.49,
'b': 1.47,
'g': 1.42,
'ę': 1.11,
'h': 1.08,
'A': 1.0,
'B': 1.0,
'C': 1.0,
'D': 1.0,
'E': 1.0,
'F': 1.0,
'G': 1.0,
'H': 1.0,
'I': 1.0,
'J': 1.0,
'K': 1.0,
'L': 1.0,
'M': 1.0,
'N': 1.0,
'O': 1.0,
'P': 1.0,
'Q': 1.0,
'R': 1.0,
'S': 1.0,
'T': 1.0,
'U': 1.0,
'V': 1.0,
'W': 1.0,
'X': 1.0,
'Y': 1.0,
'Z': 1.0,
'ą': 0.99,
'ó': 0.85,
'ż': 0.83,
'.': 0.84,
'ś': 0.66,
'ć': 0.4,
'f': 0.3,
'ń': 0.2,
'q': 0.14,
'ź': 0.06,
'?': 0.06,
'v': 0.04,
'x': 0.02,
}

cryptograms = []
maxLine = 0

cryptograms, maxLine = setCryptograms("20.txt")
key = generateKey(maxLine,cryptograms,alphabet)
print(key)

message = getData('wiadomosc.txt')
printMessage(message,key)
