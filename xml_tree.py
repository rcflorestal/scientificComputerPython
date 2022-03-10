import xml.etree.ElementTree as ET

# data = '''
# <person>
#         <name>Chuck</name>
#         <phone type="intl">
#         +1 734 303 4456
#         </phone>
#         <email hide="yes"/>
# </person>
# '''

data = '''
<person> <!-- Start tag -->
        <name>Chuck</name>
        <phone type="intl"> <!-- type="intl" is an attribute -->
        +1 734 303 4456 <!-- Text content -->
        </phone> 

        <!-- self closing with an attribute -->
        <!-- hide="yes" is an attribute -->
        <email hide="yes"/> 
</person> <!-- end tag -->
'''

tree = ET.fromstring(data)
print('Name: ', tree.find('name').text)
print('Attr: ', tree.find('email').get('hide'), end='\n\n')

## get xml data from a file
xml_file = 'xml_basics.xml'
tree_from_file = ET.parse(xml_file)
root = tree_from_file.getroot()
print(root.tag)
print(root.attrib, end='\n\n')

for child in root:
        print(child.tag, child.attrib, end='\n')

print('Name: ', root[0].text)  # print('Name: ', root.find('name').text)

