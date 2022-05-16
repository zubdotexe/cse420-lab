""" This is the v2 of Lab task 1 of CSE420 Spring 2022. This works even if there is not space inbetween a variable and comma."""

import re

# Creating lists of all the tokens in JAVA

keywords = ['abstract', 'boolean', 'break', 'byte', 'case', 'catch', 'char', 'class', 'continue', 'default', 
'do', 'double', 'else', 'enum', 'extends', 'final', 'finally', 'float', 'for', 'if', 'implements', 'import',
'instanceof', 'int', 'interface', 'long', 'native', 'new', 'package', 'private', 'protected', 'public', 
'return', 'short', 'static', 'strictfp', 'super', 'switch', 'synchronized', 'this', 'throw', 'throws', 
'transient', 'try', 'void', 'volatile', 'while']
math_op = ['+', '-', '*', '/', '=', '++', '--', '%']
logical_op = ['<', '>', '==', '!=', '<=', '>=']
numeric_val = '\d*\.\d+|\d+'
others = [',', ';', '(', ')', '{', '}', '[', ']']

# Creating empty lists to store the tokens in this file
code_keywords = []
code_math_op = []
code_logical_op = []
code_others = []
code_identifiers = []

with open('Input2.txt', 'r') as code: # Opening the file for reading
    
    code = code.read()  # Reading the file
    code_numeric_val = re.findall(numeric_val, code) # Finding all the numerial values using Re module
    code = re.sub(numeric_val, "", code) # replacing the numerial values w/ a whitespace

    """instantiating an empty variable of string type. This will be used to group up the characters and 
    then check if the group belongs to any of the tokens.
    """
    string = "" 

    for character in code: # A for loop for looping over each and every character of the variable 'code'

        if character == " " or character == "\n": # Will skip the character if it's a whitspace or '\n'
            continue
        
        """ If the string variable in line 63 is not empty, appending it to code_identifier list. 
            E.g. Let the first word of the JAVA file be 'int' 
                Firstly, it will check if 'i' is a whitspace or '\n' 
                Secondly, it will check if 'i' is in math_op or in logical_op or in others
                As, none of the above conditions is true 'i' will be stored in 'string'
                    Then it will check if string is in keywords list
                    If it is, string will be appended to code_keywords list and then the variable will be cleared

            This is how 'int' will be appended to code_keywords list. 

            However, when the character is 'a' it won't be none of whitespace or '\n' or logical_op or math_op or others. 
            As a result, 'a' will be in string. The string won't be in keywords_list. 
            After that, the next character may be a ','. 
                Bc of that, the character in others condition will be true
                    and then the comma will be appended to code_others list
                    
                    then it will check if the string variable is empty or not and
                    as the value of the string variable is 'a', it is not empty 
                    and so string/'a' will be appended to code_identifiers list
                    and then string variable will be cleared.
            """

        if character in math_op: # Checking if the character is in math_op    
            code_math_op.append(character) # If it is, appending it to the code_math_op list
            
            if string != "": # Checking if the string is not empty
                code_identifiers.append(string) 
                string = "" # Always empty the string varialbe after appending the string to any of the lists
            continue

        if character in logical_op:
            code_logical_op.append(character)

            if string != "":
                code_identifiers.append(string)
                string = ""
            continue

        if character in others:
            code_others.append(character)

            if string != "":
                code_identifiers.append(string)
                string = ""
            continue

        string = string + character # Concatenating the string with the character

        if string in keywords: # Checking if the string is in keywords list
            code_keywords.append(string)
            string = ""

def printer(str, list):
    flag = 0
    print(str, end=' ')

    for character in set(list):
        list_len = len(set(list))
        flag += 1

        if character in code_others:
            print(f'{character}', end=' ')
        elif(flag == list_len):
            print(f'{character}', end=' ')
        else:
            print(f'{character}', end=', ')
    
    print(end='\n')

# Creating a big list of all the lists of tokens found in this JAVA file
cat_list = [code_keywords, code_identifiers, code_math_op, code_logical_op, code_numeric_val, code_others]

# Iterating over the big list elements

for character in range(len(cat_list)):
    if character == 0: 
        printer('Keywords:', cat_list[character])
    elif character == 1:
        printer('Identifiers:', cat_list[character])
    elif character == 2:
        printer('Math Operators:', cat_list[character])
    elif character == 3:
        printer('Logical Operators:', cat_list[character])
    elif character == 4:
        printer('Numerical Values:', cat_list[character])
    elif character == 5:
        printer('Others:', cat_list[character])


