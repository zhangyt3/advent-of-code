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

    

    


