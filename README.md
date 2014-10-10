json-schema
===========
JSON validator based on following JSON schema format:

```
{
    SCHEMA: { // schema used for validation
        _property_ : _Type_, // single object (custom or built-in type)
        _property_ : _Type_[], // array
        _property_ : _Type_ *, // optional
        _property_ : { ... }, // object defined inline
        ...
    },
    DEFINITIONS: { // custom object type definitions
        _CustomType_: {
            _property_ : _Type_,
            ...
        },
        ...
    }
}
```