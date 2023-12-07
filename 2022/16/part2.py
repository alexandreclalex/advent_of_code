from collections import deque
import functools

with open('input.txt', 'r') as f:
    lines = [line[:-1].split() for line in f]
    
flow_speed = dict()
connections = dict()
open_state = dict()
valves = []
for tokens in lines:
    valve = tokens[1]
    rate = int(tokens[4][5:-1])
    tunnels = tokens[9:]
    for i in range(len(tunnels)):
        tunnels[i] = tunnels[i].replace(',', '')
    flow_speed[valve] = rate
    connections[valve] = tunnels
    open_state[valve] = False
    valves.append(valve)

_seen = {}
best_found = 0
def f(t, pos1, pos2, flow):
    global best_found, connections, open_state, _seen
    
    # If we already have a better score at this time, stop searching
    if _seen.get((t, pos1, pos2), -1) >= sum(flow):
        return
    _seen[t, pos1, pos2] = sum(flow)
    
    #Out of time, no need to iterate deeper
    if t == 26:
        if sum(flow) > best_found:
            best_found = sum(flow)
            print(best_found, flow)
        return
    
    # No need to do anything if all valves are open
    if all(v for k, v in open_state.items() if flow_speed[k] > 0):
        tf = sum(flow_speed[k] for k, v in open_state.items() if v)
        f(t + 1, pos1, pos2, flow + [tf])
        return
    
    for k in (0, 1):
        if k == 0:
            if open_state[pos1] or flow_speed[pos1] <= 0:
                continue
                
            open_state[pos1] = True
            
            for k2 in (0, 1):
                if k2 == 0:
                    if open_state[pos2] or flow_speed[pos2] <= 0:
                        continue
                    
                    open_state[pos2] = True
                    j = sum(flow_speed[k] for k, v in open_state.items() if v)
                    f(t + 1, pos1, pos2, flow + [ j ])
                    open_state[pos2] = False
                else:
                    j = sum(flow_speed[k] for k, v in open_state.items() if v)
                    for v2 in connections[pos2]:
                        f(t + 1, pos1, v2, flow + [ j ])
            open_state[pos1] = False
        else:
            j = sum(flow_speed[k] for k, v in open_state.items() if v)
            for v in connections[pos1]:
                for k2 in (0, 1):
                    if k2 == 0:
                        if open_state[pos2] or flow_speed[pos2] <= 0:
                            continue

                        open_state[pos2] = True
                        j = sum(flow_speed[k] for k, v in open_state.items() if v)
                        f(t + 1, v, pos2, flow + [ j ])
                        open_state[pos2] = False
                    else:
                        j = sum(flow_speed[k] for k, v in open_state.items() if v)
                        for v2 in connections[pos2]:
                            f(t + 1, v, v2, flow + [ j ])

f(1, "AA", "AA", [ 0 ])
