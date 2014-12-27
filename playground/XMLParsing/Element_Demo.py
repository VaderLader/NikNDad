# Import the ElementTree stuff by prefering the fast c-library
try:
    import xml.etree.cElementTree as ET
    #print("Using xml.etree.cElementTree")
except ImportError:
    import xml.etree.ElementTree as ET
    #print("Using xml.etree.ElementTree")
     
    
root = ET.Element("TeamA")
elem = ET.SubElement(root, "team_counter")
elem.text = "1"
elem = ET.SubElement(root, "attackpoints")
elem.text = "2"
elem = ET.SubElement(root, "keeperpoints")
elem.text = "3"

#for child in root:
#    print (child.tag, child.attrib)



outFilename = "./output.xml"
html = ET.Element("html")
body = ET.SubElement(html, "body")
ET.ElementTree(root).write(outFilename)

filename = "./TeamA.xml"

tree = ET.parse(filename)
elem = tree.getroot()

print ("------- child level by child level ------")
print("elem.tag=",elem.tag, "  elem.attrib=", elem.attrib)
for child in elem:
    if child.tag == "players" :
        print ("child.tag=", child.tag,
               " | child.attrib=",child.attrib,
               " | child.text=", child.text)
        for subchild in child:
            print ("subchild.tag=", subchild.tag,
               " | subchild.attrib=",subchild.attrib,
               " | subchild.text=", subchild.text)
    else:
        print ("child.tag=", child.tag,
               " | child.attrib=",child.attrib,
               " | child.text=", child.text)

print ("-----------with getiterator -------------")
walkAll = elem.getiterator()
for element in walkAll:
    print ("element.tag=", element.tag,
               " | element.attrib=",element.attrib,
               " | element.text=", element.text)
