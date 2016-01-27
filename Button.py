__author__ = 'Romain'

color = input("What is the color? ")[0]
text = input("What is the text? ")[0].lower()
batteries = int(input("How many batteries are there? "))
lit = input("Is the indicator lit? y/n ") == 'y'
indic_text = "null"
if lit:
    indic_text = input("What does it say? " )


def hold():
    print("Hold the button".upper())
    stripe = input("What color comes on? ")
    num = 0
    if stripe == 'b': num = 4
    elif stripe == 'w': num = 1
    elif stripe == 'y': num = 5
    else: num = 1
    print("Release the button when the countdown timer has a")
    print(str(num) + " in any position")

if color == 'b' and text == 'a':
    hold()
elif batteries > 1 and text == 'd':
    print("click the button".upper())
elif color == 'w' and lit and indic_text.lower() == 'car':
    hold()
elif batteries <= 2 and lit and indic_text.lower() == "frk":
    print("click the button".upper())
elif color == 'y':
    hold()
elif color == 'r' and text == 'h':
    print("click the button")
else:
    hold()