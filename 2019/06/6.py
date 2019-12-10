from pprint import pprint
from collections import deque

def count_orbits(orbits, thing_in_orbit):
    count = 0
    while thing_in_orbit:
        thing_in_orbit = orbits.get(thing_in_orbit, None)
        if thing_in_orbit:
            count += 1
    
    return count

def insert(adj, key, val):
    if key in adj:
        adj[key].append(val)
    else:
        adj[key] = [val]

if __name__ == '__main__':
    lines = []
    with open('6.in') as f:
        lines = f.readlines()

    # Part 1
    orbits = dict()
    for line in lines:
        line = line.strip()
        center, orbiting = line.split(")")
        orbits[orbiting] = center

    count = 0
    for thing_in_orbit in orbits.keys():
        count += count_orbits(orbits, thing_in_orbit)
    
    print(f"Orbits: {count}")

    # Part 2
    adj = dict()
    for line in lines:
        line = line.strip()
        x, y = line.split(")")

        insert(adj, x, y)
        insert(adj, y, x)
    
    # BFS
    src = 'YOU'
    dest = 'SAN'
    q = deque()
    q.append((src, 0)) 
    seen = set()
    while q:
        curr, depth = q.popleft()

        if curr == dest:
            print(f"Minimum of {depth - 2} orbital transfers needed")
            break

        if curr in seen:
            continue

        seen.add(curr)
        for n in adj[curr]:
            q.append((n, depth + 1))

