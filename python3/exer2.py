#!/usr/bin/env python3.6

from os import getenv

from math import pi

digits = int(getenv("DIGITS") or 10)

#print(digits)

print("%.*f" %(digits, pi))
