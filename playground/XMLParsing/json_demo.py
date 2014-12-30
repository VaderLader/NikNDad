import json
print ("1.) -------------")
data = [ { 'a':'A', 'b':(2, 4), 'c':3.0 } ]
print ('DATA:', repr(data))

data_string = json.dumps(data)
print ('JSON:', data_string)
print ("-----------------")
print ("2.) -------------")

data = [ { 'a':'A', 'b':(2, 4), 'c':3.0 } ]
data_string = json.dumps(data)
print ('ENCODED:', data_string)

decoded = json.loads(data_string)
print ('DECODED:', decoded)

print ('ORIGINAL:', type(data[0]['b']))
print ('DECODED :', type(decoded[0]['b']))
print ("-----------------")

print ("3.) -------------")
class MyObj(object):
    def __init__(self, s):
        self.s = s
    def __repr__(self):
        return '<MyObj(%s)>' % self.s


obj = MyObj('instance value goes here')


try:
    print (json.dumps(obj))
except TypeError, err :
    print ('ERROR:', err)

def convert_to_builtin_type(obj):
    print ('default(', repr(obj), ')')
    # Convert objects to a dictionary of their representation
    d = { '__class__':obj.__class__.__name__, 
          '__module__':obj.__module__,
          }
    d.update(obj.__dict__)
    return d

print ()
print ('With default')
print (json.dumps(obj, default=convert_to_builtin_type))
