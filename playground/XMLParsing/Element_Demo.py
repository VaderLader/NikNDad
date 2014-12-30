# Import the ElementTree stuff by prefering the fast c-library
#from lxml import etree as ET
#try:
#   
    
    #import lxml.etree.cElementTree as ET
    #import xml.etree.cElementTree as ET
#    print("Using xml.etree.cElementTree")
#except ImportError:
#    import xml.etree.ElementTree as ET
#    print("Using xml.etree.ElementTree")

try:
  from lxml import ET
  print("running with lxml.etree")
except ImportError:
  try:
    # Python 2.5
    import xml.etree.cElementTree as ET
    print("running with cElementTree on Python 2.5+")
  except ImportError:
    try:
      # Python 2.5
      import xml.etree.ElementTree as ET
      print("running with ElementTree on Python 2.5+")
    except ImportError:
      try:
        # normal cElementTree install
        import cElementTree as ET
        print("running with cElementTree")
      except ImportError:
        try:
          # normal ElementTree install
          import elementtree.ElementTree as ET
          print("running with ElementTree")
        except ImportError:
          print("Failed to import ElementTree from any known place")





    
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
#ET.ElementTree(root).prettyprint(outFilename)
print(ET.tostring(root, pretty_print=True))

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
