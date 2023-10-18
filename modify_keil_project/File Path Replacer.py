
import os
import xml.etree.ElementTree as ET


def find_file_in_folders(filename, folders):
    for folder in folders:
        for root, dirs, files in os.walk(folder):
            if filename in files:
                return os.path.relpath(os.path.join(root, filename), os.path.dirname(input_file_C))
    return None

# input_folder_A = input("Enter the path of Folder A: ")
# input_folder_B = input("Enter the path of Folder B: ")
# input_file_C = input("Enter the path of the .uvprojx file: ")
input_folder_A = r'D:\_Pro2023\Git\panchip\panplat\pan1080'
input_folder_B = input_folder_A
input_file_C = r'D:\_Pro2023\Git\panchip\panplat\pan1080\_hal_release\mcu_samples_hal\WWDT\keil\__WWDT.uvprojx'



tree = ET.parse(input_file_C)
root = tree.getroot()

for group_element in root.findall(".//Group"):
    group_name = group_element.find("GroupName").text

    # Skip files under the group "User"
    if group_name == "User" or group_name == "usr":
        group_element.find("GroupName").text = "User"
        continue

    for file_element in group_element.findall(".//File"):
        filename = file_element.find("FileName").text

        # If the filename is retarget.c, search for pan_retarget.c instead
        if filename == "retarget.c":
            filename_to_search = "pan_retarget.c"
            new_path = find_file_in_folders(filename_to_search, [input_folder_A, input_folder_B])

            if new_path:
                print(f"Updating path for {filename} to use {filename_to_search} at {new_path}")
                file_element.find("FileName").text = filename_to_search
                file_element.find("FilePath").text = new_path
            else:
                print(f"WARNING: File {filename_to_search} not found in provided folders!")
        else:
            new_path = find_file_in_folders(filename, [input_folder_A, input_folder_B])
            if new_path:
                print(f"Updating path for {filename} to {new_path}")
                file_element.find("FilePath").text = new_path
            else:
                print(f"WARNING: File {filename} not found in provided folders!")

# tree.write(input_file_C)
# Modify IncludePath value under VariousControls tag
for various_controls in root.findall(".//VariousControls"):
    include_path_element = various_controls.find("IncludePath")
    if include_path_element is not None:
        # include_path_element.text = r"..\..\..\..\01_SDK\modules\hal\panchip\panplat\pan1080\bsp\cmsis\include;..\..\..\..\01_SDK\modules\hal\panchip\panplat\pan1080\bsp\peripheral\inc;..\..\..\..\01_SDK\modules\hal\panchip\panplat\pan1080\bsp\device\Include;..\src"
        include_path_element.text = r"..\..\..\..\bsp\cmsis\include;..\..\..\..\bsp\device\Include;..\..\..\..\bsp\peripheral\inc;..\src"

# Save the XML with declaration
with open(input_file_C, "wb") as f:
    f.write(b'<?xml version="1.0" encoding="UTF-8" standalone="no" ?>\n')
    tree.write(f, encoding="utf-8")
