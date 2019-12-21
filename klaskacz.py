#!/usr/bin/env python3

import sys
import time
import threading

from app import parser, player

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

def noteDuration(bpm, note):
    return 60 / (note / 4) / bpm

def main():
    try:
        if len(sys.argv) != 2:
            raise AppIncorrectUsageError('Niepoprawne użycie programu. Zajrzyj do instrukcji obsługi')

        klpFilename = sys.argv[1]
        klpParser = parser.Parser(klpFilename)
        
        print(f'Odtwarzanie pliku {klpFilename}')
        print(f'Tempo: {klpParser.bpm} BPM')
        
        sound = player.Sound('assets/0.mp3')
        
        while True:
            instruction = klpParser.readInstruction()
            # DBG: printInstruction(instruction)

            if instruction[0] == parser.Instruction.note:
                sound.play()
            time.sleep(noteDuration(klpParser.bpm, instruction[1]))


    except AppIncorrectUsageError as error:
        print(error)
    except parser.ReadFileError:
        print(error)
    except parser.EndOfInstructionsError:
        pass

if __name__ == '__main__':
    main()
