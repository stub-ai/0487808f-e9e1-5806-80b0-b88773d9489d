import pandas as pd
import xml.etree.ElementTree as ET

def parse_xml(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()

    data = []
    for element in root:
        row_data = {}
        for child in element:
            row_data[child.tag] = child.text
        data.append(row_data)

    return data

def write_to_excel(data, excel_file):
    df = pd.DataFrame(data)
    df.to_excel(excel_file, index=False)

def main():
    xml_file = 'input.xml'  # replace with your xml file
    excel_file = 'output.xlsx'  # replace with your desired output excel file

    data = parse_xml(xml_file)
    write_to_excel(data, excel_file)

if __name__ == "__main__":
    main()