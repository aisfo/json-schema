#!/usr/bin/python
from parser import parse


if __name__ == '__main__':  
      
    with open('input.jssc', 'r') as f:
        parse(f.read())
    f.closed