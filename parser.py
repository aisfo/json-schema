
def validate(json, schema):

    parsedSchema = parseSchema(schema)
     
    return 0


def parseSchema(raw_schema):

    schema = ''.join(raw_schema.split()).lower()
    size = len(schema)
    
    assert (size > 0)
    print schema
    
    i = 0
    parsedSchema, i = parseValue(schema, i, size)
    assert(i == size)
    # check parsedSchema
      
    return parsedSchema
    
    
def parseValue(schema, i, size):
    
    value = None
    type = None
    optional = False
    
    while i < size:
        ch = schema[i]
        i += 1
          
        if ch == '{':
            type = 'Object'
            value = {}
            while 1:
                name, val, i = parseProperty(schema, i, size)
                if name == None:
                    break
                value[name] = val
        elif ch == '}':
            if (type == 'Type'):
                i -= 1
            break
        
        elif ch.isalnum():
            if value == None:   
                type = 'Type'
                value = ''
            value += ch
        
        elif ch == '[':
            type = 'Array'
            continue
        elif ch == ']':
            continue
        
        elif ch == '*':
            optional = True
        
        elif ch == ',':
            break

        else:
            raise Exception('invalid syntax. saw ' + ch + ' at ' + str(i))

    return ((value, type, optional), i)

def parseProperty(schema, i, size):

    name = ''
    value = None
    while i < size:
        ch = schema[i]
        i += 1

        if ch.isalnum():
            name += ch
            continue
        elif len(name) and ch == ":":
            value, i = parseValue(schema, i, size)
            break
        elif ch == '}':
            break
        else:
            raise Exception('invalid syntax. saw ' + ch + ' at ' + str(i))
            
    if name == '':
        name = None

    return (name, value, i)


# dev
with open('input.jssc', 'r') as f:
    print parseSchema(f.read())
f.closed
    
