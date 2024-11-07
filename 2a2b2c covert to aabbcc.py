a="2a2b2c"
output=""
char = ""
for char in a:
    if char.isalpha():
         var = char
         output += var * num
    else:
        num = int(char)
print(output)
