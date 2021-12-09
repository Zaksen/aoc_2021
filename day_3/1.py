with open('input.txt', 'r') as f:
    numbers = [l.rstrip() for l in f.readlines()]

a = 0
b = 0
c = 0
d = 0
e = 0

for n in numbers:
    a += int(n[0])
    b += int(n[1])
    c += int(n[2])
    d += int(n[3])
    e += int(n[4])

def find_gamma(x):
    if x > len(numbers)/2:
        return 1
    else:
        return 0

gamma = str(find_gamma(a)) + str(find_gamma(b)) + str(find_gamma(c)) + str(find_gamma(d)) + str(find_gamma(e))


print(gamma)