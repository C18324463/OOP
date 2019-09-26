binary = input("Enter a binary number\n")

i = 0
integer = 0
powers = 0

while i < len(binary):
    if binary[i] == '1':
        integer = integer + 2*powers
    i = i + 1
    powers = powers + 1
print(integer)