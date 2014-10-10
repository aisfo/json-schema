from schema import Schema

if __name__ == '__main__':  
    
    schema = None
    with open('examples/schema_0.txt', 'r') as f:
        schema = Schema(f.read())
    f.closed
    
    with open('examples/data_0.json', 'r') as f:
        json = f.read()
    f.closed
    
    print schema.validate(json)