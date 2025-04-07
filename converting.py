def get_user_input():
    user_input = input("Enter the roman numerals you want to convert (Q to quit): ")
    return user_input

def roman_to_int(numeral):
    # A set of valid roman numerals
    valid_roman_numerals = set("IVXLCDM")

    final_result = 0

    if "CM" in numeral:
        final_result += 900
        numeral = numeral.replace("CM", "")
    if "CD" in numeral:
        final_result += 400
        numeral = numeral.replace("CD", "")
    if "XC" in numeral:
        final_result += 90
        numeral = numeral.replace("XC", "")
    if "XL" in numeral:
        final_result += 40
        numeral = numeral.replace("XL", "")
    if "IX" in numeral:
        final_result += 9
        numeral = numeral.replace("IX", "")
    if "IV" in numeral:
        final_result += 4
        numeral = numeral.replace("IV", "")


    for i in numeral:
        if i == "M":
            final_result += 1000
        elif i == "D":
            final_result += 500
        elif i == "C":
            final_result += 100
        elif i == "L":
            final_result += 50
        elif i == "X":
            final_result += 10
        elif i == "V":
            final_result += 5
        elif i == "I":
            final_result += 1
    print("The roman numerals you entered translate to: " + str(final_result) + ".")

def is_valid_roman(numeral):
    # Verify if every character of the string is a valid Roman Numeral (I, V, X, L, C, D or M)
    return all(char in "IVXLCDM" for char in numeral)

while True:
    user_input = get_user_input()

    if user_input.upper() == "Q":
        print("Exiting the program.")
        break

    if is_valid_roman(user_input.upper()):
        roman_to_int(user_input.upper())
    else:
        print("Invalid Roman numeral. Please try again.")