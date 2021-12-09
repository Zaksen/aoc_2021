with open('input.txt', 'r') as f:
    numbers = [int(l.rstrip()) for l in f.readlines()]

count = 0
init = numbers[0]
for i in range(1, len(numbers)):
    if numbers[i] > init:
        count += 1
    init = numbers[i]


print(count)