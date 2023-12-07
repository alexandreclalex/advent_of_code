
with open('input.txt', 'r') as f:
    lines = [line[:-1] for line in f]

mapping = {
    '1':1,
    '2':2,
    '=':-2,
    '-':-1,
    '0':0
}

inv_mapping = {
    1: '1',
    2: '2',
    -2:'=',
    -1:'-',
    0:'0'
}

pow_of_5 = [5**i for i in range(100)][::-1]

def convert_to_decimal(snafu):
    digits = [mapping[x] for x in snafu][::-1]
    total = 0
    for i in range(len(digits)):
        total += 5**i*digits[i]
    return total

def convert_to_snafu(n):
    digits = []
    while n > 0:
        digits.append(n%5)
        n//=5
    digits = digits[::-1]
    print(digits)
    i = 0
    while i< len(digits):
        if digits[i] == 4:
            digits[i-1] += 1
            digits[i] = -1
            i-=1
        elif digits[i] == 3:
            digits[i-1] += 1
            digits[i] = -2
            i -= 1
        else:
            i += 1
    return ''.join([inv_mapping[x] for x in digits]).lstrip('0')

total = sum([convert_to_decimal(line) for line in lines])
print(total)
print(convert_to_snafu(total))