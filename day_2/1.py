with open('input.txt', 'r') as f:
    instructions = [l.rstrip() for l in f.readlines()]

x = 0
y = 0

for i in instructions:
    if i[0] == "f":
        x += int(i[-1])
    elif i[0] == "u":
        y -= int(i[-1])
    else:
        y += int(i[-1])

print(x*y)