from collections import deque
import functools

with open('input.txt', 'r') as f:
    lines = [line[:-1].split() for line in f]
    
connections = dict()
flow_rates = dict()
open_valve = dict()
valves = []
for tokens in lines:
    valve = tokens[1]
    rate = int(tokens[4][5:-1])
    tunnels = tokens[9:]
    for i in range(len(tunnels)):
        tunnels[i] = tunnels[i].replace(',', '')
    connections[valve] = tunnels
    flow_rates[valve] = rate
    open_valve[valve] = False
    valves.append(valve)

move_cost = [[999]*len(valves) for _ in range(len(valves))]
for i in range(len(valves)):
    move_cost[i][i] = 0
explore_queue = deque()
for i, valve in enumerate(valves):
    explored = set(connections[valve].copy() + [valve])
    to_explore = [(valve, x) for x in connections[valve]]
    while to_explore:
        prev, next_valve = to_explore.pop()
        for v in connections[next_valve]:
            if v not in explored:
                explored.add(v)
                to_explore.append((next_valve, v))
        move_cost[i][valves.index(next_valve)] = move_cost[i][valves.index(prev)] + 1

# undesirable_valves = [x for x in flow_rates if flow_rates[x] == 0]
# def pressure_from_move(time, a, b):
#     if time <= 0:
#         return 0, 0
#     cost = move_cost[valves.index(a)][valves.index(b)]
#     return (time - cost - 1) * flow_rates[b], (time-cost-1)

# @functools.lru_cache(1024)
# def get_max_pressure_r(pos, time, visited_set):
#     pressure_scores = []
#     for valve in valves:
#         if valve not in visited_set and valve not in undesirable_valves:
#             new_visited = visited_set + (valve,)
#             pressure, new_time = pressure_from_move(time, pos, valve)
#             pressure_scores.append(get_max_pressure_r(valve, new_time, new_visited) + pressure)
#     return max(pressure_scores + [0])

# max_score = get_max_pressure_r('AA', 30, tuple(['AA']))
# print(max_score)

_seen = {}
m = 0
def f(t, pos, flow):
    global m, connections, open_valve, _seen
    
    if _seen.get((t, pos), -1) >= sum(flow):
        return
    _seen[t, pos] = sum(flow)
    
    #
    if t == 30:
        m = max(m, sum(flow))
        print(m)
        return
    
    # Open valve here?
    for k in (0, 1):
        if k == 0:
            if open_valve[pos] or flow_rates[pos] <= 0:
                continue
                
            open_valve[pos] = True
            j = sum(flow_rates[k] for k, v in open_valve.items() if v)
            f(
                t + 1,
                pos,
                flow + [ j ]
            )
            open_valve[pos] = False
        else:
            j = sum(flow_rates[k] for k, v in open_valve.items() if v)
            for v in connections[pos]:
                f(
                    t + 1,
                    v if v is not None else pos,
                    flow + [ j ]
                )

f(1, "AA", [ 0 ])