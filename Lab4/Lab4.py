# import os
# def calculate_page_offset(address):
#     page_size = 4096
#     page_number = address // page_size
#     offset = address % page_size
#     return page_number, offset

# # Get the current working directory
# current_directory = os.getcwd()

# # Create the output file path
# output_file_path = os.path.join(current_directory, "output.txt")

# # Test the function
# addresses = [19986, 347892, 5978]

# with open(output_file_path, "w") as output_file:
#     for address in addresses:
#         page_number, offset = calculate_page_offset(address)
#         output_file.write(f"The address {address} is in:\n")
#         output_file.write(f"Page number = {page_number}\n")
#         output_file.write(f"Offset = {offset}\n")
#         output_file.write("\n")

from asyncio import wait


def calculate_page_offset(address):
    page_size = 4096
    page_number = address // page_size
    offset = address % page_size
    return page_number, offset


wait(1)