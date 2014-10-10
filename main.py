#!/usr/bin/python
from parser import validate


if __name__ == '__main__':  
    
    with open('schema', 'r') as f:
        schema = f.read()
    f.closed
    
    with open('example.json', 'r') as f:
        json = f.read()
    f.closed
    
    print validate(json, schema)