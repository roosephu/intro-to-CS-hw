
## problem 15
# a = "01010111 01101000 01100001 01110100 00100000 01100100 01101111 01100101 01110011 00100000 01101001 01110100 00100000 01110011 01100001 01111001 00111111"
# for x in a.split(' ') :
#     print(chr(int(x, base = 2)), end = '')

## problem 26
# s = "a. 1111 b. 0001 c. 10101 d. 1000 e. 10011 f. 000000 g. 1001 h. 10001 i. 100001 j. 11001 k. 11010 l. 11011"
# for i in s.replace('. ', ':').split(' ') :
#     print('\\item', i[:2], int(i[2:], base = 2))

# problem 54
a = "a. 111010 110110  \
b. 101000 100110 001100  \
c. 011101 000110 000000 010100  \
d. 010010 001000 001110 101111 000000 110111 100110  \
e. 010011 000000 101001 100110"

m = "000000 001111 010011 011100 100110 101001 110101 111010"
F = {}
for x, i in enumerate(m.split(' ')) :
    F[i] = chr(ord('A') + x)

def dist(a, b) :
    return sum([x != y for x, y in zip(list(a), list(b))])

def get(x) :
    return min([(dist(x, y), z) for y, z in F.items()])[1]

for s in a.split('  ') :
    print ('\item', ''.join([get(x) for x in s[3:].split(' ')]))
