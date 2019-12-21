#!/usr/bin/env python3

import sys
import time
import parser
import player
import threading

class AppIncorrectUsageError(Exception):
    pass

def printInstruction(instruction):
    instructionName = repr(instruction[0])
    parameter = ',parametr: ' + str(instructionName[1]) if instruction[1] else ''
    print(f'Instrukcja: {instructionName}{parameter}')

def main():
    try:
        if len(sys.argv) != 2:
            raise AppIncorrectUsageError('Niepoprawne użycie programu. Zajrzyj do instrukcji obsługi')

        klpFilename = sys.argv[1]
        klpParser = parser.Parser(klpFilename)

        print(f'Odtwarzanie pliku {klpFilename}')
        print(f'BPM (Ćwierćnuty na minutę): {klpParser.bpm}')

        while True:
            instruction = klpParser.readInstruction()
            printInstruction(instruction)


    except AppIncorrectUsageError as error:
        print(error)
    except parser.ReadFileError:
        print(error)
    except parser.EndOfInstructionsError:
        pass

if __name__ == '__main__':
    main()
