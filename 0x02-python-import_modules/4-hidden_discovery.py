#!/usr/bin/python3
import sys
import hidden_4

if __name__ == "__main__":
    names = sorted(dir(hidden_4))
    for name in names:
        if name[:2] != "__":
            print(name)
