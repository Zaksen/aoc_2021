with open('input.txt', 'r') as f:
    numbers = [l.rstrip() for l in f.readlines()]

def filtering(nums, pos, binary):
    length = len(nums) + 1
    count = 0

    for n in nums:
        count += int(n[pos])
    if binary == 1:
        selector = 1 if count >= (length // 2) else 0
    else:
        selector = 0 if count >= (length // 2) else 1  
    return [n for n in nums if n[pos] == str(selector)]

oxygen_rating = numbers[:]
scrubber_rating = numbers[:]

i = 0
while len(oxygen_rating) > 1:
    oxygen_rating = filtering(oxygen_rating, i, 1)
    i += 1

i = 0
while len(scrubber_rating) > 1:
    scrubber_rating = filtering(scrubber_rating, i, 0)
    i += 1

print(int(oxygen_rating[0], 2) * int(scrubber_rating[0], 2))





