
from collections import deque


with open('input.txt', 'r') as f:
    raw_lines = [line[:-1] for line in f]
    
lines = []
for line in raw_lines:
    line = line.split(':')
    lines.append(line[0])
    for x in line[1].split('.'):
        lines.append(x)

bps = []
for i in range(0, len(lines), 6):
    ore_cost = (int(lines[i+1].split()[4]), 0, 0, 0)
    clay_cost = (int(lines[i+2].split()[4]), 0, 0, 0)
    obs_cost = (int(lines[i+3].split()[4]),  int(lines[i+3].split()[7]), 0, 0)
    geode_cost = (int(lines[i+4].split()[4]), 0, int(lines[i+4].split()[7]), 0)
    bps.append((ore_cost, clay_cost, obs_cost, geode_cost))

bps = bps[:3]

max_robots = dict()
for bp in bps:
    max_spend = [0, 0, 0, 999]
    for recipe in bp:
        for i, val in enumerate(recipe):
            if val > max_spend[i]:
                max_spend[i] = val
    max_robots[bp] = max_spend

MAX_TIME = 32

triangle_nums = [0]
for i in range(1, MAX_TIME+1):
    triangle_nums.append(triangle_nums[-1] + i)

total_seen = 0
def simulate(bp):
    S = (0, 0, 0, 0, 1, 0, 0, 0, 0)
    queue = deque([S])
    best_score = 0
    seen = set()
    Co = bp[0][0]
    Cc = bp[1][0]
    Co1 = bp[2][0]
    Co2 = bp[2][1]
    Cg1 = bp[3][0]
    Cg2 = bp[3][2]
    max_r1, max_r2, max_r3, max_r4 = max_robots[bp]
    while queue:
        state = queue.popleft()
        o, c, ob, g, r1, r2, r3, r4, time = state
        
        # Throw away any excess resources to reduce states
        if o > (MAX_TIME - time) * max_r1 - r1 * (MAX_TIME - time -1):
            # We have more than we need if we build one r1 every turn from here on out
            o = (MAX_TIME - time) * max_r1 - r1 * (MAX_TIME - time -1)
        if c > (MAX_TIME - time) * max_r2 - r2 * (MAX_TIME - time -1):
            c = (MAX_TIME - time) * max_r2 - r2 * (MAX_TIME - time -1)
        if ob > (MAX_TIME - time) * max_r3 - r3 * (MAX_TIME - time -1):
            ob = (MAX_TIME - time) * max_r3 - r3 * (MAX_TIME - time -1)
        
        
        if state in seen:
            continue
        
        if g + r3 *(MAX_TIME - time) + triangle_nums[(MAX_TIME - time -1)] < best_score:
            # Will not beat if we buy a r4 every turn from now on
            continue
        
        if g > best_score:
            best_score = g

        seen.add(state)
        
        if time == MAX_TIME:
             continue
        
        (o+r1, c+r2, ob+r3, g+r4, r1, r2, r3, r4, time+1)
        
        # Can we build r1?
        if r1 < max_r1 and o>=Co:
            queue.append((o-Co+r1, c+r2, ob+r3, g+r4, r1+1, r2, r3, r4, time+1))
        # Can we build r2?
        if r2 < max_r2 and o>=Cc:
            queue.append((o-Cc+r1, c+r2, ob+r3, g+r4, r1, r2+1, r3, r4, time+1))
        # Can we build r3?
        if r3 < max_r3 and o>=Co1 and c>=Co2:
            queue.append((o-Co1+r1, c-Co2+r2, ob+r3, g+r4, r1, r2, r3+1, r4, time+1))
        # Can we build r4?
        if r4 < max_r4 and o>=Cg1 and ob>=Cg2:
            queue.append((o-Cg1+r1, c+r2, ob-Cg2+r3, g+r4, r1, r2, r3, r4+1, time+1))
        
        # Build no robots
        queue.append((o+r1, c+r2, ob+r3, g+r4, r1, r2, r3, r4, time+1))
    global total_seen
    total_seen += len(seen)
    return best_score

scores = []
for i in range(len(bps)):
    print((i*100)//len(bps), '% complete', end = '\r')
    scores.append(simulate(bps[i]))
print('100 % complete')

print('Total number of examined states:', total_seen)

total = 1
for score in scores:
    total *= score
print(total)