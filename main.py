#!/usr/bin/env python3

import sys
import time
import parser
import player
import threading

class AppIncorrectUsageError(Exception):
    pass

def printInstruction(instruction):
    instructionType, parameter = instruction

    if instructionType == parser.Instruction.note:
        print('Nuta o wartości', parameter)
    elif instructionType == parser.Instruction.rest:
        print('Pauza o wartości', parameter)
    else:
        print('Zmiana dźwięku na', parameter)

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
