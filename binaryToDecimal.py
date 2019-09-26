binary = input("Enter a binary number\n")

i = 0
integer = 0
power = 0

while i < len(binary):
    if binary[i] == '1':
        integer = integer + 2*power
    i = i + 1
    power = power + 1
print(integer)