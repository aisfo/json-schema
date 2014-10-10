#!/usr/bin/python
from schema import Schema


if __name__ == '__main__':  
    
    schema = None
    with open('schema.txt', 'r') as f:
        schema = Schema(f.read())
    f.closed
    
    with open('example.json', 'r') as f:
        json = f.read()
    f.closed
    
    print schema.validate(json)