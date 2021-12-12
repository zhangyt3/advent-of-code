if __name__ == "__main__":
    lines = []
    with open("12.in") as f:
        lines = [x.strip() for x in f.readlines()]
    lines = list(map(lambda line: line.split("-"), lines))

    adj = dict()
    for start, end in lines:
        if start not in adj:
            adj[start] = []
        if end not in adj:
            adj[end] = []
        adj[start].append(end)
        adj[end].append(start)

    routes = 0
    stack = []
    stack.append(("start", set(), False))
    while stack:
        curr, visited, used_small_visit = stack.pop()

        if curr == "end":
            routes += 1
            continue
        
        visited.add(curr)
        for dest in adj[curr]:
            if dest == "start":
                continue
            if dest in visited and dest.islower() and used_small_visit:
                continue
            if dest in visited and dest.islower() and not used_small_visit:
                stack.append((dest, visited.copy(), True))
            else:
                stack.append((dest, visited.copy(), used_small_visit))
    print(f"Paths: {routes}")
