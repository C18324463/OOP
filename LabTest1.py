old_row = [1, 1]
j = 0
print([old_row[j]], [old_row[j+1]])

def make_new_row(old_row):
    i = 0
    while i < len(old_row):
        j = i + (i + 1)
        old_row[i+1] = j
        i = i + 1
    return old_row
new_row = make_new_row(old_row)

print(new_row)
