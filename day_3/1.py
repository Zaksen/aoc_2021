with open('input.txt', 'r') as f:
    numbers = [l.rstrip() for l in f.readlines()]

length = len(numbers)
count = [0 for i in range(len(numbers[0]))]

for n in numbers:
    for i in range(len(count)):
        count[i] += int(n[i])

def to_binary(x, length):
    return int(x // (length  / 2))

gamma = "".join([str(to_binary(e, length)) for e in count])
epsilon = "".join([str(1 - to_binary(e, length)) for e in count])

print(int(gamma, 2) * int(epsilon, 2))
