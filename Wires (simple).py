__author__ = 'Romain'

print("Color code : ")
print("blue:   b")
print("black:  k")
print("red:    r")
print("white:  w")
print("yellow: y\n")
original_colors = input("What are the colors of your wires? \n")
list_colors = list(original_colors)
list_colors.sort()
list_colors.sort()
sorted_colors = ''.join(list_colors)
serial_number_is_odd = False
if len(sorted_colors) > 3:
    serial_number_is_odd = bool(int(input("What is the last digit of the serial number ? "))%2)
print("Cut the ")


def exactly_one(char):
    return char in sorted_colors and ''.join([char, char]) not in sorted_colors

if len(sorted_colors) == 3:
    if 'r' not in sorted_colors: print("2nd wire")
    elif original_colors[-1] == 'w': print("last wire")
    elif "bb" in sorted_colors: print("last blue wire")
    else: print("last wire")

if len(sorted_colors) == 4:
    if serial_number_is_odd and 'rr' in sorted_colors: print("last red wire")
    elif original_colors[-1] == 'y' and 'r' not in sorted_colors: print("first wire")
    elif exactly_one('b'): print("1rst wire")
    elif 'yy' in sorted_colors: print("last wire")
    else: print("2nd wire")

if len(sorted_colors) == 5:
    if original_colors[-1] == 'k' and serial_number_is_odd: print("4th wire")
    elif exactly_one('r') and 'yy' in sorted_colors: print("1rst wire")
    elif 'k' not in sorted_colors: print("2nd wire")
    else: print("1rst wire")

if len(sorted_colors) == 6:
    if 'y' not in sorted_colors and serial_number_is_odd: print("3rd wire")
    elif exactly_one('y') and 'ww' in sorted_colors: print("4th wire")
    elif 'r' not in sorted_colors: print("last wire")
    else: print("4th wire")