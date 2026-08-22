# Write a code to accept the string of length 10 from the user and print True if string has any character

# occurring 5 times consecutively in it, otherwise print False.

  
s = input("Enter a string of length 10: ")

found = False

for i in range(len(s) - 4):
    if s[i] == s[i+1] == s[i+2] == s[i+3] == s[i+4]:
        found = True
        break

print(found)