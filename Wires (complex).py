__author__ = 'Romain'

batteries = input("How many batteries are there? ")
parallel = input("Does the bomb has a parallel port? y/n ") == 'y'
last_digit_even = not bool(int(input("What is the last digit of the serial number? "))&2)

print("Describe your wire with this chart :")
print("blue wiring :    b")
print("black wiring :   k")
print("red wiring :     r")
print("white wiring :   w")
print("yellow wiring :  y")
print("LED on :         l")
print("star underneath: s")
instruction = 'c'


def instruction_letter_to_word(instr):
    if instr == 'c' or \
            (instr == 's' and last_digit_even) or \
            (instr == 'p' and parallel) or \
            (instr == 'b' and batteries):
        return "cut the wire"
    else:
        return "do not cut the wire"


while True:
    # We will strip down the color coding to binary
    wire = input("Describe your wire : ")
    red_coloring = 'r' in wire
    blue_coloring = 'b' in wire
    star_symbol = 's' in wire
    LED_is_on = 'l' in wire
    if wire == 'done':
        break

    ID = ''.join([str(int(red_coloring)), str(int(blue_coloring)), str(int(star_symbol)), str(int(LED_is_on))])
    if   ID == '0000': instruction = 'c'
    elif ID == '0001': instruction = 'd'
    elif ID == '0010': instruction = 'c'
    elif ID == '0011': instruction = 'b'
    elif ID == '0100': instruction = 's'
    elif ID == '0101': instruction = 'p'
    elif ID == '0110': instruction = 'd'
    elif ID == '0111': instruction = 'p'
    elif ID == '1000': instruction = 's'
    elif ID == '1001': instruction = 'b'
    elif ID == '1010': instruction = 'c'
    elif ID == '1011': instruction = 'b'
    elif ID == '1100': instruction = 's'
    elif ID == '1101': instruction = 's'
    elif ID == '1110': instruction = 'p'
    elif ID == '1111': instruction = 'd'
    else: print("Fail; start again")
    print(instruction_letter_to_word(instruction))
    print("if you are done, enter \"done\" as the description of the wire")
