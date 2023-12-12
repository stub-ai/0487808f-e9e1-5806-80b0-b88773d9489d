import pandas as pd
import xml.etree.ElementTree as ET

def parse_XML(xml_file):
    tree = ET.ElementTree(file=xml_file)
    root = tree.getroot()
    data = []

    for item in root:
        elements = {}
        for child in item:
            elements[child.tag] = child.text
        data.append(elements)

    return data

def convert_to_excel(xml_file, excel_file):
    data = parse_XML(xml_file)
    df = pd.DataFrame(data)
    df.to_excel(excel_file, index=False)

# Usage
convert_to_excel('input.xml', 'output.xlsx')