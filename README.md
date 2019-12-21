# Klaskacz
Klaskacz to aplikacja, która potrafi wyklaskać sekwencję rytmiczną zapisaną w pliku .klp

## Użycie
Aby odtworzyć sekwencję z pliku *example.klp* należy wykonać następującą komendę:
```bash
$ ./klaskacz example.klp
```

## Struktura pliku klp
Plik .klp jest plikiem binarnym. Pierwsze dwa bajty (zapisane w formie little endian) interpretujemy jako liczbę ćwierćnut w czasie minuty (BPM).
Kolejne bajty oznaczają sekwencję dźwięków.

### Znaczenie poszczególnych wartości bajtów
Wartości te podane są w systemie szesnastkowym - taka konwencja została przyjęta ze względu na przyjemniejsze tworzenie plików przy pomocy hexedytora.

Nuty dźwięczne:
- 0x01 - cała nuta
- 0x02 - półnuta
- 0x04 - ćwierćnuta
- 0x08 - ósemka
- 0x16 - szesnastka
- 0x32 - trzydziestodwójka
- 0x64 - sześćdziesięcioczwórka

Pauzy - mają zapalony najwyższy bit:
- 0x81 - pauza całonutowa
- 0x82 - pauza półnutowa
- 0x84 - pauza ćwierćnutowa
- 0x88 - pauza ósemkowa
- 0x96 - pauza szesnastkowa
- 0xB2 - pauza trzydziestkodwójkowa
- 0xE4 - pauza sześćdziesięcioczwórkowa

