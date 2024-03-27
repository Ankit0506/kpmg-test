import os

def get_nested_value(obj, key):
    keys = key.split('/')
    for k in keys:
        obj = obj.get(k)
        if obj is None:
            return None
    return obj

value = get_nested_value(object2, key2)
print(value) 
