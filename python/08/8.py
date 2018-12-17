import sys

class TreeNode:
    def __init__(self, children, metadata):
        self.children = children
        self.metadata = metadata   

    def print_tree(self):
        print(self.metadata)
        for c in self.children:
            c.print_tree()
    
    def sum_metadata(self):
        return sum(self.metadata) + sum([c.sum_metadata() for c in self.children])

    def value(self):
        if len(self.children) == 0:
            return sum(self.metadata)
        else:
            res = 0
            for index in self.metadata:
                i = index - 1
                if i < 0 or i >= len(self.children):
                    continue
                else:
                    res += self.children[i].value()
            return res


def parse_tree(data, low):
    # First two elements make up the header
    num_children, num_metadata = data[low:low + 2]
   
    # Recursively get children and update low index as we go
    children = []
    low = low + 2
    for _ in range(num_children):
        child, low = parse_tree(data, low)
        children.append(child)
    
    # Metadata entries are the last elements
    metadata = data[low:low + num_metadata]

    return TreeNode(children, metadata), low + num_metadata


    


if __name__ == '__main__':
    with open('../../input/8.in') as f:
        line = f.read()
    data = [int(x) for x in line.split(' ')]
    
    root, _ = parse_tree(data, 0)
    print("Sum of metadata entries:", root.sum_metadata())
    print("Value of the root node:", root.value())