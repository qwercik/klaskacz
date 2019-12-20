from aenum import MultiValueEnum

class KlpParserReadFileError(Exception):
    pass

class KlpParserEndOfInstructions(Exception):
    pass

class KlpInstruction(MultiValueEnum):
wholeNote = 0x01
    halfNote = 0x02
    quarterNote = 0x04
    eighthNote = 0x08
    sixteenthNote = 0x16
    thirtySecondNote = 0x32
    sixtyFourthNote = 0x64
    wholeRest = 0x81
    halfRest = 0x82
    quarterRest = 0x84
    eighthRest = 0x88
    sixteenthRest = 0x96
    thirtySecondRest = 0xB2
    sixtyFourthRest = 0xE4
    voiceChange = tuple(range(0xC0, 0xD0))

class KlpParser:
    def __init__(self, filename):
        try:
            self.file = open(filename, 'rb')
            self.filename = filename
        except:
            raise KlpParserReadFileError(f'Wystąpił problem z wczytaniem pliku {filename}. Upewnij się, że jest to poprawna nazwa pliku.')
    
        self.bpm = int.from_bytes(self.file.read(2), byteorder='little')

    def readInstruction():
        instructionByte = None
        try:
            instructionByte = self.file.read(1)
        except:
            raise KlpParserEndOfInstructions(f'Nie ma już więcej instrukcji w pliku {self.filename}')

        instructionType = KlpInstruction(instructionByte)
        parameter = instructionByte & 0xF if instructionType == KlpInstruction.voiceChange else None

        return (instructionType, parameter) 
