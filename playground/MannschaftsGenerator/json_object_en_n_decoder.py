# following an example from:
# http://pymotw.com/2/json/
#
import json
from collections import OrderedDict

class OrderedEncoder(json.JSONEncoder):
    ''' Encoding objects by using OrderedDict'''
    
    def default(self, obj):
        #print ('default(', repr(obj), ')')
        d = OrderedDict()
                
        #__class__ and __module__ do come first
        d['__class__'] = obj.__class__.__name__
        d['__module__'] = obj.__module__
        arg_dict = OrderedDict(obj.__dict__)

        #print(arg_dict)        
        #Then the arguments are added              
        d.update(arg_dict)
        #print("After encoding d = \n",d)
        return d


class OrderedDecoder(json.JSONDecoder):
    ''' Decoding objects by using OrderedDict '''
    
    def __init__(self):
        json.JSONDecoder.__init__(self, object_pairs_hook=self.dict_to_object)

    def dict_to_object(self, dd):
        """ Argument is an dictionary with all memberattributes necessary to
        construct the object
        """        
        #print("___ OrderedDecoder.dict_to_object(dd) ___")
        #print(dd) 
        d = OrderedDict(dd)
        class_name = d.popitem(last=False)[1]        
        module_name = d.popitem(last=False)[1]
        #print("--- class_name", class_name, "module_name", module_name)
        module = __import__(module_name)
        #print("--- module:", module)
        #class_ is of type 'type'
        class_type = getattr(module, class_name)
        #print("--- type(class_type):" , type(class_type))
        #print("--- class_type:", class_type)
        #print("--- d.items()", d.items())
        args = dict(d.items())
        #print("--- args:", args)
        inst = class_type(args)
        #print("==============\n")
        return inst
        
    