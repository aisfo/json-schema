#!/usr/bin/python
import sys

schema = ""
with open('input.jssc', 'r') as f:
    schema = f.read()
f.closed

schema = ''.join(schema.split()).lower()
size = len(schema)
assert (size > 0)
print schema
print size

currObj = None
parsedObj = None
currProp = None

dictProp = False
prop = False
value = False
openBrace = True
closeBrace = False
openBracket = False
closeBracket = False
colon = False
star = False
obj = False

alnum = ''

i = 0
while i < 50:
    ch = schema[i]
    i += 1

    if openBrace:
        if ch == '{' and dict == None:
            currObj = {}
            parsedObj = currObj
            openBrace = False
            dictProp = True
            continue
        elif ch == '{':
            openBrace = False
            prop = True
            continue
        else:
            print ch
            raise Exception('{ expected') 
    elif dictProp:
        if ch.isalnum():
            alnum += ch
        else:
            if alnum == 'json' or alnum == 'definitions':
                currProp = alnum
                currObj[currProp] = {}
                dictProp = False
                colon = True
                obj = True
                i -= 1
            else:
                print ch
                raise Exception('json or definitions expected')
            alnum = ''
        continue
    elif prop:
        if ch.isalnum():
            alnum += ch
        elif len(alnum) > 0:
            currProp = prop
        else:
            print ch
            raise Exception('property name missing')
    elif colon:
        if ch == ':':
            colon = False
            openBrace = obj
            obj = False
            continue
        else:
            print ch
            raise Exception(': expected')

print parsedObj
            

#raw_input("Press any key to exit...")
