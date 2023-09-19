# Implementing Caesar Cipher in Python
print("Caesar Cipher in Python with Dictionary")

# Making a dictionary
# We are storing both uppercase and lowercase values in this else we have to change message to lowercase
# The Problem with this is that it will have the same value for both uppercase and lowercase letter and thus the output comes in lowercase
def alph_dict_make():
    # First initializing dictionary to store value of alphabet and its corresponding number
    alph_dict = {}

    # Using a loop to assign value of alphabet and number in dictionary
    # chr function is used to get character for that corresponding ASCII value
    for i in range(1, 27):

        # For Lowercase
        alph_lwr = chr(96 + i)
        # Appending in Dictionary
        alph_dict[alph_lwr] = i

        # For Upperrcase
        alph_upr = chr(64 + i)
        # Appending in Dictionary
        alph_dict[alph_upr] = i

    return alph_dict


# Making a function for Caesar Cipher Encryption and Decryption
# Since we only need to subtract shift value, we will pass it as negative for decryption
def Caesar_Cipher(text,n):

    # Now after storing value our next task is to encrypt using this dictionary
    # We can do this according to the formula
    # Convertion of a character (string) to its corresponding ASCII value (integer), can be done using the ord() function

    encryp_text = ''

    # Traversing through all the elements in the given string
    for i in text:

        # We need to add % 26 to wrap alphabets up else for z it will have no values
        char_value = (alph_dict[i] + n) % 26

        # Finding character according to value
        # Since there is no inbuilt function in python to find key for corresponding value we have to define function for that
        # Next is an iterator it finds the first key that matches the value
        # items functions returns both key and value for dictionary
        # if statement is used to compare which key matches with the given value
        val = next(key for key, value in alph_dict.items() if value == char_value)

        # Adding the character in the encrypted text
        encryp_text += val


    return encryp_text

# Taking user input for message
message = input("Enter Message: ")
shift_value = int(input("Enter Shift Value: "))

# Making alphabet and corresponding value dictionary
alph_dict = alph_dict_make()

# Doing Encryption
encryp_text = Caesar_Cipher(message,shift_value)
print(f"Encrypted Text using Caesar Cipher with Shift value {shift_value} is:",encryp_text.upper())

# Decryption
print(f"Decrypted Text using Caesar Cipher with Shift value {shift_value} is:",Caesar_Cipher(encryp_text,-shift_value))