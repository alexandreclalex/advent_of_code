from functools import cmp_to_key

with open('input.txt', 'r') as f:
    lines = [line[:-1] for line in f]
    
packets = []
curr_packet = []
for line in lines:
    if line:
        curr_packet.append(eval(line))
    else:
        packets.append(curr_packet)
        curr_packet = []
        
packets.append(curr_packet)
curr_packet = []

def cmp(a, b):
	if isinstance(a, int):
		if isinstance(b, int):
			if a < b:
				return 1
			if b < a:
				return -1
			return 0
		return cmp([a, ], b)
	if isinstance(b, int):
		return cmp(a, [b, ])
	
	for si in range(min((len(a), len(b), ))):
		sr = cmp(a[si], b[si])
		if 1 == sr:
			return 1
		if -1 == sr:
			return -1
	
	if len(a) < len(b):
		return 1
	if len(b) < len(a):
		return -1
	
	return 0
    
temp = []
for a, b in packets:
    temp.append(a)
    temp.append(b)
packets = temp

packets.append([[2]])
packets.append([[6]])

result= 1
packets = sorted(packets, key=cmp_to_key(cmp), reverse=True)
for i, x in enumerate(packets, start=1):
    kk = ascii(x)
    if kk == '[[2]]':
        result *= i
    if kk == '[[6]]':
        result *= i
print(result)