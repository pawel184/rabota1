#!/usr/bin/env python
import sys

if len(sys.argv) != 3:
    print("Использование: python arguments.py <имя> <фамилия>")
    sys.exit(1)

name = sys.argv[1]
surname = sys.argv[2]

print(f"Hi, my name is {name}. My surname {surname}.")
print("My official credentials My mail address is Denis_Skakalski@gmail.com")
