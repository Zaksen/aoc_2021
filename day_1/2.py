with open('input.txt', 'r') as f:
    numbers = [int(l.rstrip()) for l in f.readlines()]

count = 0
init = sum(numbers[0:3])

print(init)
for i in range(1, len(numbers) - 2):
    if sum(numbers[i:i+3]) > init:
        count += 1
    init = sum(numbers[i:i+3])

print(count)