#!/usr/bin/env python3

import sys
import time
import parser
import player
import threading

class AppIncorrectUsageError(Exception):
    pass

def main():
    try:
        if len(sys.argv) != 2:
            raise AppIncorrectUsageError('Niepoprawne użycie programu. Zajrzyj do instrukcji obsługi')

        klpFilename = sys.argv[1]
        klpParser = parser.Parser(klpFilename)

        print('BPM: ', klpParser.bpm)

        while True:
            instruction = klpParser.readInstruction()
            print('Instrukcja:', repr(instruction[0]), ('parametr: ' + str(instruction[1])) if not not instruction[1] else '')

    except AppIncorrectUsageError as error:
        print(error)
    except parser.ReadFileError:
        print(error)
    except parser.EndOfInstructionsError:
        pass

if __name__ == '__main__':
    main()
