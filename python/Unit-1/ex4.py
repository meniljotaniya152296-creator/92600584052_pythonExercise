#  Write a program to demonstrate string operations including slicing formatting and built-in string functions


x = input("enter your name: ")

print(x.upper())

print(x.lower())

print(x.capitalize())

print(x.title())

print(x.strip())    # remove inknown spaces

print(x.replace(x,"Jotaniya"))

print(x.find("i"))

print(x.count("i"))

print(x.split(" "))

print("-".join(x))

print(x.startswith("men"))

print(x.endswith("ya"))

print(x.isalpha())

print(x.isdigit())

print(len(x))

print({x[1:3]})
