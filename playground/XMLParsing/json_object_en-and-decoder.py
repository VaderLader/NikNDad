# following an example from:
# http://pymotw.com/2/json/
#
import json


class DemoClass(object):
    def __init__(self, n, beg="Hallo"):
        self.name = n
        self.begruessung = beg
        
    def __repr__(self):
        return '<DemoClass(%s)>' % self.name


class MyEncoder(json.JSONEncoder):
    
    def default(self, obj):
        print ('default(', repr(obj), ')')
        # Convert objects to a dictionary of their representation
        d = { '__class__':obj.__class__.__name__, 
              '__module__':obj.__module__,
              }
        d.update(obj.__dict__)
        print("After encoding d = \n",d)
        return d


class MyDecoder(json.JSONDecoder):
    
    def __init__(self):
        json.JSONDecoder.__init__(self, object_hook=self.dict_to_object)

    def dict_to_object(self, d):
        print("=== MyDecoder.dict_to_object()")
        if '__class__' in d:
            class_name = d.pop('__class__')
            module_name = d.pop('__module__')
            module = __import__(module_name)
            print ('MODULE:', module)
            #class_ is of type 'type'
            class_type = getattr(module, class_name)
            print ("type(class_type):" , type(class_type))
            rt = "trztrzr"
            print ("type(rt):" , type(rt))
            print ('CLASS:', class_type)
            #args = dict( (key.encode('ascii'), value) for key, value in d.items())
            print ("d.items()", d.items())
            args = dict( d.items())
            print ('INSTANCE ARGS:', args)
            print ('args.values():', args.values())
            #args.values(): dict_values(['Otto', 'Hola'])

            print ('*args.values():', *args.values())
            
            inst = class_type(*args.values())
            #inst = class_('Otto', 'Hola')
                        
        else:
            inst = d
            
        print("==============\n")
        return inst


        
print("----- Start -----")
obj = DemoClass('Otto', 'Hola')

print ("---- The test object for encoding/decoding is this one:\n", obj)
print ("----\n")
print ("----Calling encoder ----")
print (MyEncoder().encode(obj))


encoded_object = MyEncoder().encode(obj)
print ("-----\nencoded_object:\n")
print (encoded_object)
print ("----- Endocing finished !!-----------\n")


#encoded_object = '[{"s": "instance value goes here", "__module__": "json_myobj", "__class__": "MyObj"}]'

print ("----Calling decoder ----")
myobj_instance = MyDecoder().decode(encoded_object)
print ("---- decoded object:\n")
print (myobj_instance)

newobj = ()

