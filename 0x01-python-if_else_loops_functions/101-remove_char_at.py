#!/usr/bin/python3
for n in range(-122, -96):
    print("{}".format(chr(n * -1)) if (n * -1) % 2 == 0
          else "{}".format(chr((n * -1) - 32)), end='')
