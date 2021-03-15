from platform import *

print(platform())
print(machine())
print(processor())

import sys

for i in sys.path :
    print(i)

import os

print(os.getcwd())