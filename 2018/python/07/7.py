import sys
import networkx as nx 
import matplotlib.pyplot as plt

def get_time(letter):
    BASE_TIME = 60
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    return BASE_TIME + 1 + alphabet.index(letter)


if __name__ == '__main__':
    # Read input and build graph
    G = nx.DiGraph()
    for line in sys.stdin:
        tokens = line.split(" ")
        src = tokens[1]
        dst = tokens[-3]
        G.add_edge(src, dst)

    # Visualize
    # plt.subplot(121)
    # nx.draw_networkx(G, with_labels=True)
    # plt.show()

    ordered = []
    for node in nx.algorithms.dag.lexicographical_topological_sort(G):
        ordered.append(node)
    print("Ordered steps: " + "".join(ordered))

    # Part 2
    tasks = []
    time = 0
    free_workers = 5
    while len(tasks) > 0 or len(G) > 0:
        # All tasks with no unfulfilled dependencies
        available = [label for label in G if G.in_degree(label) == 0]  

        # Filter out tasks already running
        running = set()
        for label1 in available:
            for label2, _ in tasks:
                if label1 == label2:
                    running.add(label1)
        available = [label for label in available if label not in running]

        if len(available) > 0 and free_workers > 0:
            # Get next task we should work on
            t = sorted(available)[0]
            tasks.append((t, get_time(t)))
            free_workers -= 1
        else:
            # Fast forward to the next completed task
            tasks = sorted(tasks, key=lambda x: x[1])  # Sort by duration
            label, delta_time = tasks[0]

            # Update the time for all ongoing tasks
            tasks.pop(0)
            tasks = [(l, t - delta_time) for (l, t) in tasks]

            # Update the DiGraph by removing the finished task
            G.remove_node(label)

            time += delta_time
            free_workers += 1
    print("Time to complete all tasks: {}".format(time))


    


