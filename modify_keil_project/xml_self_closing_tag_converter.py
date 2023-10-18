"""
XML Empty Tag Converter

This script converts self-closing XML tags in a given XML file to
an open tag followed by a close tag format.

For example, <TagName /> becomes <TagName></TagName>.
"""

import xml.etree.ElementTree as ET

def modify_xml_file(input_file):
    """
    Modify the XML file to transform self-closing tags into open and close tag format.

    Args:
    - input_file (str): Path to the XML file to be modified.
    """
    # Parse the XML file
    tree = ET.parse(input_file)
    root = tree.getroot()

    # Search for all empty tags
    for element in root.iter():
        # If element is an empty tag
        if not list(element) and not element.text:
            element.text = ""

    # Save the modified XML file
    tree.write(input_file, xml_declaration=True, encoding="UTF-8", method="xml")

# Use the function
file_path =r"C:\Doc\pan1080-dk-internal\03_MCU\mcu_samples_hal\PWM\keil\PWM.uvprojx"
# modify_xml_file("your_xml_file_path.xml")
modify_xml_file(file_path)
