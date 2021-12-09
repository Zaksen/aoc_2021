with open('input.txt', 'r') as f:
    instructions = [l.rstrip() for l in f.readlines()]

x = 0
y = 0
z = 0

for i in instructions:
    if i[0] == "f":
        x += int(i[-1])
        y += z * int(i[-1])
    elif i[0] == "u":
        z -= int(i[-1])
    else:
        z += int(i[-1])

print(x*y)