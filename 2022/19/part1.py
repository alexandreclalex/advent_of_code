
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

best_score = 0

max_robots = dict()
for bp in bps:
    max_spend = [0, 0, 0, 999]
    for recipe in bp:
        for i, val in enumerate(recipe):
            if val > max_spend[i]:
                max_spend[i] = val
    max_robots[bp] = max_spend

def simulate(bp, time, robots, resources):
    assert all([x>=0 for x in resources])
    # print(time, robots, resources)
    
    if (bp, time, robots, resources) in seen:
        return seen[(bp, time, robots, resources)]
    if time == 23:
        return resources[3] + robots[3]
    
    sim_results = []
    for index, recipe in enumerate(bp):
        if max_robots[bp][index] <= robots[index]:
            continue
        for i in range(4):
            if resources[i] < recipe[i]:
                break
        else:
            new_robots = tuple([robots[i] if i != index else robots[i]+1 for i in range(4)])
            new_resources = tuple([resources[i] - recipe[i] + robots[i] for i in range(4)])
            sim_results.append(simulate(bp, time+1, new_robots, new_resources))
    
    new_resources = tuple([resources[i] + robots[i] for i in range(4)])
    sim_results.append(simulate(bp, time+1, tuple([x for x in robots]), new_resources))

    result = max(sim_results)
   
    seen[(bp, time, robots, resources)] = result
    return result

scores = []
for i in range(len(bps)):
    print((i*100)//len(bps), '% complete', end = '\r')
    seen = {}
    scores.append(simulate(bps[i], 0, (1, 0, 0, 0), (0, 0, 0, 0)))
print('100 % complete')

quality = []
for i, score in enumerate(scores, start=1):
    quality.append(score*i)

print(sum(quality))