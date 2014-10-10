
class Schema():
    
    def __init__(self, raw_schema):
        schema = ''.join(raw_schema.split()).lower()
        size = len(schema)
        
        print schema
        assert (size > 0)
        
        i = 0
        parsedSchema, i = parseValue(schema, i, size)
        parsedSchema = parsedSchema[0]
        
        # validate schema
        print parsedSchema
        assert(i == size)
        assert(parsedSchema['schema'] != None)
        
        self.schema = parsedSchema


    def validate(self, json):
    
        print self.schema

        return 0
    
    
def parseValue(schema, i, size):
    
    value = None
    objType = None
    optional = False
    
    while i < size:
        ch = schema[i]
        i += 1
          
        if ch == '{':
            objType = 'Object'
            value = {}
            while 1:
                name, val, i = parseProperty(schema, i, size)
                if name == None:
                    break
                value[name] = val
        elif ch == '}':
            if (objType == 'Type'):
                i -= 1
            break
        
        elif ch.isalnum():
            if value == None:   
                objType = 'Type'
                value = ''
            value += ch
        
        elif ch == '[':
            objType = 'Array'
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


# debug
with open('schema.txt', 'r') as f:
    s = Schema(f.read())
f.closed
    
