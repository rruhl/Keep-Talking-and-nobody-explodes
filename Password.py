__author__ = 'Romain'


current_possible_passwords = [
    "about", "after", "again", "below", "could",
    "every", "first", "found", "great", "house",
    "large", "learn", "never", "other", "place",
    "plant", "point", "right", "small", "sound",
    "spell", "still", "study", "their", "there",
    "these", "thing", "think", "three", "water",
    "where", "which", "world", "would", "write"]
new_possible_passwords = []

positions = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth']
i = 0

for position in positions:
    if len(current_possible_passwords) == 1:
        break
    ith_letter = input(str('What are the possible letters for the ' + position + ' position? '))
    for letter in list(ith_letter):
        for password in current_possible_passwords:
            if letter in list(password)[i]:
                new_possible_passwords.append(password)
    current_possible_passwords = new_possible_passwords
    new_possible_passwords = []
    i += 1

if len(current_possible_passwords) > 0:
    print("\n")
    print(str(current_possible_passwords[0] + " is your password"))
else:
    print("FAIL, please start over")