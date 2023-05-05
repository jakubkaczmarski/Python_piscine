import sys

string_to_analyze = ""
if sys.argv.__len__() == 1:
    string_to_analyze = input("What is the text to count\n")
elif sys.argv.__len__() != 2:
    print(AssertionError)
    exit(1)
if sys.argv.__len__() == 2:
    string_to_analyze = sys.argv[1]
    
string_data = {
    "Upper": 0,
    "Lower": 0,
    "Punctuation": 0,
    "Spaces": 0,
    "Digits": 0
}

punctiuation_arr = {",", ".", "\\", "?", "!", "\{", "(", "\}", ")", "[", "]", "-", "~", ";", "*", "-", "@"}

for letter in string_to_analyze:
    if letter.isdigit() :
        string_data["Digits"] += 1
    elif letter.isspace() : 
        string_data["Spaces"] += 1
    elif letter in punctiuation_arr:
        string_data["Punctuation"] += 1
    elif letter.islower():
        string_data["Lower"] += 1
    elif letter.isupper():
        string_data["Upper"] += 1
    elif letter == "\r":
        string_data["Spaces"] += 1

print("The text contains ", string_to_analyze.__len__(), " characters");
print(string_data["Upper"], " upper letters")
print(string_data["Lower"], " lower letters")
print(string_data["Punctuation"], " punctuation marks")
print(string_data["Spaces"], " spaces")
print(string_data["Digits"], " digits")