#!/usr/bin/env python3

import os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

with open(os.path.join(__location__, "test.txt")) as f:
    print(f.readline())
    print(f.readline())
    print(f.readline())
    print(f.readline())
    print(f.readline())