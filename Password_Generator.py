"""
Password Generator

    If user would like to use only characters or numbers or special characters or combination of these choices when user 
    want to genarate particular password(s), this python algorithm will help user about that.
"""

import random

# LISTS
answer = "Y"
chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
special_chars = "~`!@#$%^&*()_-+={[}]|\:;'<,>.?/"
numbers = "1234567890"

# LOOP
while answer == "Y":
    # PASSWORD TYPE QUESTIONS
    password_chars = input("Would you like to use character? (Y/N) : ")
    password_numbers = input("Would you like to use numbers? (Y/N) : ")
    password_special_chars = input("Would you like to use special character? (Y/N) : ")

    # WARNING
    if password_chars == "N" and password_numbers == "N" and password_special_chars == "N":
        print("\nYOU HAVE TO ENTER 'Y' ONE OF QUESTIONS ABOVE!\n")
    else:
        # PASSWORD PROPERTY QUESTIONS
        password_lenght = int(input("What lenght would you like your password to be? : "))
        password_count = int(input("How many passwords would you like? : "))
        
        # SETTING CHARACTER LIST FOR PASSWORD
        chars_pool = ""
        if password_chars == "Y":
            chars_pool += chars
        if password_numbers == "Y":
            chars_pool += numbers
        if password_special_chars == "Y":
            chars_pool += special_chars
        
        # GENERATING PASSWORD
        for x in range(0, password_count):
            password = ""
            for x in range (0, password_lenght):
                password_char = random.choice(chars_pool)
                password += password_char
            print("Here is your password : ", password)

        # LOOP QUESTION
        answer = input("Would you like to generate another password? (Y/N) : ")

