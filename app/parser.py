from aenum import MultiValueEnum

class ReadFileError(Exception):
    pass

class EndOfInstructionsError(Exception):
    pass

class Instruction(MultiValueEnum):
    note = (0x01, 0x02, 0x04, 0x08, 0x16, 0x32, 0x64)
    rest = (0x81, 0x82, 0x84, 0x88, 0x96, 0xB2, 0xE4)
    voiceChange = tuple(range(0xC0, 0xD0))

class Parser:
    def __init__(self, filename):
        try:
            self.file = open(filename, 'rb')
            self.filename = filename
        except:
            raise ReadFileError(f'Wystąpił problem z wczytaniem pliku {filename}. Upewnij się, że jest to poprawna nazwa pliku.')
    
        self.bpm = int.from_bytes(self.file.read(2), byteorder='little')

    def readInstruction(self):
        instructionByte = None
        try:
            instructionByte = self.file.read(1)[0]
        except:
            raise EndOfInstructionsError(f'Nie ma już więcej instrukcji w pliku {self.filename}')

        instructionType = Instruction(instructionByte)
        parameter = instructionByte & 0xF if instructionType == Instruction.voiceChange else int(hex(instructionByte & 0x7F)[2:])
        # Return sound number or note name (in integer)

        return (instructionType, parameter) 

