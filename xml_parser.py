import xml.etree.ElementTree as ET

tree = ET.parse('cities.xml')
root = tree.getroot()

for city in root.iter('city'):
    for child in city:
        print(child.tag, child.text)