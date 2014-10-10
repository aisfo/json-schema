import json
from IPython.config.application import catch_config_error

class Schema():
    
    def __init__(self, _schema):
        
        schema = ''.join(_schema.split())
        size = len(schema)

        assert (size > 0)
        
        i = 0
        parsedSchema, i = parseValue(schema, i, size)
        parsedSchema = parsedSchema[0]
        
        # validate schema  
        assert(i == size)
        assert(parsedSchema['schema'] != None)

        if (parsedSchema['definitions'] != None):
            parsedSchema['definitions'] = parsedSchema['definitions'][0]
            
        #print parsedSchema 
        #todo validate customtypes , upper case
        
        self.schema = parsedSchema

    def validate(self, _json):
        
        valid = True
        j = json.loads(_json)
        _schema = self.schema['schema']
        _definitions = self.schema['definitions']
        
        print " schema"
        valid = validateValue(j, _schema, _definitions, "")
        
        return valid
    
def validateValue(jValue, eType, _definitions, offset):
    valid = True
    
    offset += " -" 
    print offset, "value:", jValue
    
    _type = eType[0]
    _defType = eType[1]
      
    if _defType == 'Type':
        if _type == "String":
            valid = isinstance(jValue, unicode)
            if not valid:
                print offset, "wrong type. expected", _type, "(", unicode, "). got:", type(jValue)
            return valid
        elif _type == "Number":
            valid = isinstance(jValue, int)
            if not valid:
                print offset, "wrong type. expected", _type, "(", int, "). got:", type(jValue)
            return valid
        else:
            _type = _definitions[_type][0] #cleanup definitions
    elif _defType == 'Array':
        return valid
        
    for prop in _type:
        print
        print offset, prop
        eType = _type[prop]
        try:
            _jValue = jValue[prop]
            res = validateValue(_jValue, eType, _definitions, offset)
            if not res:
                valid = False
        except KeyError:
            if not eType[2]:
                valid = False
                print offset, "property missing: ", prop
            else:
                print offset, "optional property missing: ", prop
           
    
    return valid
    
    
def parseValue(schema, i, size):
    
    value = None
    objType = None
    optional = False
    braces = False
    while i < size:
        ch = schema[i]
        i += 1
          
        if ch == '{':
            objType = 'Inline'
            braces = True
            value = {}
            while 1:
                name, val, i = parseProperty(schema, i, size)
                if name == '':
                    break
                value[name] = val
        elif ch == '}':
            if (braces and objType == 'Inline'):
                braces = False
            else:
                i -= 1
                break      
        elif ch.isalnum():
            if value == None:   
                objType = 'Type'
                value = ''
            value += ch
        elif ch == '[':
            objType = 'Array'
        elif ch == ']':
            continue
        elif ch == '*':
            optional = True
        elif ch == ',':
            break
        else:
            raise Exception('invalid syntax. saw ' + ch + ' at ' + str(i))

    return ((value, objType, optional), i)


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

    return (name, value, i)


# debug
s = None
with open('examples/schema_0.txt', 'r') as f:
    s = Schema(f.read())
f.closed

with open('examples/data_0.json', 'r') as f:
    print s.validate(f.read())
f.closed


    
