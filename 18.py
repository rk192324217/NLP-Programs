import re

# Input FOPC expression
expression = "likes(John, pizza)"

# Regular expression for parsing
pattern = r'(\w+)\(([\w\s,]+)\)'

match = re.match(pattern, expression)

if match:
    predicate = match.group(1)
    arguments = [arg.strip() for arg in match.group(2).split(",")]

    print("Predicate:", predicate)
    print("Arguments:")
    for arg in arguments:
        print(" -", arg)
else:
    print("Invalid FOPC expression")
