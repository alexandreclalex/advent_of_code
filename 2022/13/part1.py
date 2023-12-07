import sys
sys.setrecursionlimit(1500)

with open('input.txt', 'r') as f:
    lines = [line[:-1] for line in f]
    
packets = []
curr_packet = []
for line in lines:
    if line:
        curr_packet.append(line)
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

truth_values = []
for a, b in packets:
    a_tokens = eval(a)
    b_tokens = eval(b)

    truth_values.append(cmp(a_tokens, b_tokens) == 1)
    
print(truth_values)
total = 0
for i, val in enumerate(truth_values, start=1):
    if val:
        total += i
        
print(total)