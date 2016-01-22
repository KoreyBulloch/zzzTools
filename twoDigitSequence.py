#! python3

# twoDigitSequence.py
# Counts up from 00 to 99, copying each number to the clipboard
# and waiting for the user before proceeding to the next number.


import pyperclip


# Pads single digit numbers with a 0 (3 becomes 03, 11 stays 11).  
def int_to_str_pad(number):
    if number < 10:
        return "0" + str(number)
    else:
        return str(number)


def enter_to_proceed():
	proceed = "no"
	while proceed == "no":
		print("Press 'Enter' to proceed.")
		proceed = input()

def two_digit_sequence(cap = 99):
	sequence = 0
	while sequence <= cap:
		print("Copying number", int_to_str_pad(sequence))
		pyperclip.copy(int_to_str_pad(sequence))
		sequence += 1
		enter_to_proceed()


two_digit_sequence()