# The following string is encoded using the Caesar cipher with a shift of 5: udymts . Decode the string!

s = "udymts"

result = ""

for ch in s:
    result += chr(ord(ch) - 5)

print(result)