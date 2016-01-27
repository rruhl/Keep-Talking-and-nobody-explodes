__author__ = 'Romain'

current_words = [
    "shell",
    "halls",
    "slick",
    "trick",
    "boxes",
    "leaks",
    "strobe",
    "bistro",
    "flick",
    "bombs",
    "break",
    "brick",
    "steak",
    "sting",
    "vector",
    "beats"]
new_words = []

inverse_code = {
    '.-'	:	'A',    '-...'	:	'B',   	'-.-.'	:	'C',
    '-..'	:	'D',    '.'		:	'E',     '..-.'	:	'F',
    '--.'	:	'G',    '....'	:	'H',    '..'	:	'I',
    '.---'	:	'J',    '-.-'	:	'K',    '.-..'	:	'L',
    '--'	:	'M',    '-.'	:	'N',    '---'	:	'O',
    '.--.'	:	'P',    '--.-'	:	'Q',    '.-.'	:	'R',
    '...'	:	'S',    '-'		:	'T',     '..-'	:	'U',
    '...-'	:	'V',    '.--'	:	'W',    '-..-'	:	'X',
    '-.--'	:	'Y',    '--..'	:	'Z',

    '-----'	:	'0',    '.----'	:	'1',    '..---'	:	'2',
    '...--'	:	'3',    '....-'	:	'4',    '.....'	:	'5',
    '-....'	:	'6',    '--...'	:	'7',    '---..'	:	'8',
    '----.'	:	'9'
    }

to_frequency = {
    "shell": "3.505 MHz",
    "halls": "3.515 MHz",
    "slick": "3.522 MHz",
    "trick": "3.532 MHz",
    "boxes": "3.535 MHz",
    "leaks": "3.542 MHz",
    "strobe": "3.545 MHz",
    "bistro": "3.552 MHz",
    "flick": "3.555 MHz",
    "bombs": "3.565 MHz",
    "break": "3.572 MHz",
    "brick": "3.575 MHz",
    "steak": "3.582 MHz",
    "sting": "3.592 MHz",
    "vector": "3.595 MHz",
    "beats": "3.600 MHz"}

while len(current_words) > 1:
    letter = input("Give me one letter you could find ")
    try:
        letter = inverse_code[letter].lower()
        print(str("That was an " + letter))
    except:
        letter = letter
    for word in current_words:
        if letter in word:
            new_words.append(word)
    current_words = new_words
    new_words = []
print("\n")

if len(current_words) > 0:
    print(str(to_frequency[current_words[0]]) + " is your frequency and your word was " + current_words[0])
else:
    print("FAIL, please start over")