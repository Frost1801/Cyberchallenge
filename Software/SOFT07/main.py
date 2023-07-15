# open t.txt and read only exadecimal values using a regular expression
# and store them in a list
import re


def read_file():
    with open('t.txt', 'r') as f:
        data = f.read()
        return data


def convert_to_hex(data):
    hex_list = re.findall(r'0x[0-9a-fA-F]+', data)
    return hex_list


def convert_to_int(hex_list):
    int_list = []
    for hex in hex_list:
        int_list.append(int(hex, 16))
    return int_list


data = read_file()
hex_list = convert_to_hex(data)
int_list = convert_to_int(hex_list)
for i in int_list:
    print(chr(i), end='')
