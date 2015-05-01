JSON Codierung und Encodierung 
=====================================
Beispiel für eine Codierung in json format für das Object ``myObject``
----------------------------------------------------------------
::
	
	# Example for encoding myObject and writing it to file: 
	encoded_object = OrderedEncoder().encode(self.__dict__['myObject'])
	f = open("c:\file.json","w")
	f.write(encoded_object)
	f.flush()
		
		
Beispiel für das Erzeugen von ``myObject`` aus einem json-file
---------------------------------------------------------------
::
	
	# Example for decoding from file and creating myObject: 
	f = open("c:\file.json","r")
	self.__dict__["myObject"] = OrderedDecoder().decode(f.read())        
        
        


json_object_en_n_decoder module
--------------------------------
.. automodule:: json_object_en_n_decoder
    :members:
    :undoc-members:
    :show-inheritance:
