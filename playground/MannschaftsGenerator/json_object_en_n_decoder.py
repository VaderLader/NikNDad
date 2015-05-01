# following an example from:
# http://pymotw.com/2/json/
#
import json
from collections import OrderedDict

class OrderedEncoder(json.JSONEncoder):
    ''' Encoding objects by using a OrderedDict
        Any object can be passed to this class and it becomes encoded
    '''
        #: Example for encoding myObject and writing it to file: 
        #: encoded_object = OrderedEncoder().encode(self.__dict__['myObject'])
        #: f = open("c:\file.json","w")
        #: f.write(encoded_object)
        #: f.flush()
    
    def default(self, obj):
        ''' This method defines how the object is encoded
        
        :param obj: object you want to serialize
        :type obj:  object
        :returns: other object wich can be serialized
        :rtype: object
        
        '''
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
    ''' Decoding objects by using OrderedDict
        Any object which was encoded by the "OrderedEncoder" can be decoded 
    '''    
       
       # Example for decoding from file and creating myObject: 
               
        #f = open("c:\file.json","r")
        #self.__dict__["myObject"] = OrderedDecoder().decode(f.read())        
        
        

    
    def __init__(self):
        json.JSONDecoder.__init__(self, object_pairs_hook=self.dict_to_object)

    def dict_to_object(self, dd):
        ''' Instantiates the object using the encoded data
        
        :param dd: dictionary with all memberattributes necessary to construct the object
        :type obj:  OrderedDict
        :returns: encoded object
        :rtype: type of the object

        '''        
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
        
    