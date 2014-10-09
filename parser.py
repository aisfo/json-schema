
def parse(schema):
    schema = ''.join(schema.split()).lower()
    size = len(schema)
    assert (size > 0)
    print schema
    
    i = 0
    parsedSchema, i = parseValue(i, schema)
    
    assert(i == size)
    
    return parsedSchema

    
def parseValue(i, schema):
    value = None;
    size = len(schema)

    string = ''
    
    while i < size:
        ch = schema[i]
        i += 1
          
        if ch == '{':
            value = {}
            name = ''
            while 1:
                name, val, i = parseProperty(i, schema)
                if name == None:
                    break
                value[name] = val
        elif ch.isalnum():
            string += ch
            value = string
        elif ch == ',':
            break
        elif ch == '}':
            if (value == string):
                i -= 1
            break

    return value, i

def parseProperty(i, schema):
    size = len(schema)
    name = ''
    value = None
    while i < size:
        ch = schema[i]
        i += 1

        if ch.isalnum():
            name += ch
            continue
        elif len(name) and ch == ":":
            value, i = parseValue(i, schema)
            break
        elif ch == '}':
            break
        else:
            raise Exception('invalid syntax. saw ' + ch + ' at ' + str(i))
            
    if name == '':
        name = None

    return (name, value, i)

with open('input.jssc', 'r') as f:
    print parse(f.read())
f.closed
    
